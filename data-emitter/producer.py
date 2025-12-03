import os
import sys
import json
import time
import random
import logging
import signal
from datetime import datetime, timezone
from faker import Faker
from confluent_kafka import Producer, KafkaException

logging.basicConfig(level=logging.WARNING)
LOG = logging.getLogger('DataEmitter')
KAFKA_TARGET_TOPIC = 'user-activity-stream'
KAFKA_ADDRESS = os.getenv("KAFKA_BROKER_HOST")

if not KAFKA_ADDRESS:
    raise RuntimeError("KAFKA_BROKER_HOST environment variable missing.")

data_generator = Faker('en_US')
EVENT_TYPES = ["page_view", "add_to_cart", "purchase", "logout", "login"]

producer_config = {
    'bootstrap.servers': KAFKA_ADDRESS,
    'client.id': 'clickstream-simulator-v2',
    'acks': 'all',
    'retries': 3
}

try:
    data_stream_publisher = Producer(producer_config)
except KafkaException as e:
    LOG.error(f"Kafka client initialization failed: {e}")
    sys.exit(1)


def assemble_click_event():
    current_time_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    should_purchase = data_generator.boolean(chance_of_getting_true=30)
    transaction_amount = round(random.uniform(5.0, 450.0), 2) if should_purchase else None
    
    user_event_record = {
        "event_identifier": data_generator.uuid4(),
        "account_id": data_generator.uuid4(),
        "action_name": data_generator.random_element(elements=EVENT_TYPES),
        "source_path": data_generator.uri_path(),
        "session_token": data_generator.uuid4(),
        "platform_type": data_generator.random_element(elements=("mobile", "desktop", "tablet")),
        "timestamp_utc": current_time_str,
        "location": {
            "latitude": float(data_generator.latitude()),
            "longitude": float(data_generator.longitude())
        },
        "monetary_value": transaction_amount
    }
    return user_event_record

def on_delivery_success(err, msg):
    if err is not None:
        LOG.warning(f"Message delivery failed to {msg.topic()}: {err}")
    else:
        LOG.debug(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def initiate_graceful_exit(producer_instance, sig, frame):
    pending_count = producer_instance.flush(timeout=10)
    if pending_count > 0:
        LOG.error(f"WARNING: {pending_count} messages were not delivered.")
    sys.exit(0)

signal.signal(signal.SIGINT, lambda s, f: initiate_graceful_exit(data_stream_publisher, s, f))
signal.signal(signal.SIGTERM, lambda s, f: initiate_graceful_exit(data_stream_publisher, s, f))


if __name__ == "__main__":
    LOG.warning(f"Data Emitter starting. Target: {KAFKA_ADDRESS} Topic: {KAFKA_TARGET_TOPIC}")
    
    try:
        while True:
            new_event = assemble_click_event()
            
            try:
                data_stream_publisher.produce(
                    topic=KAFKA_TARGET_TOPIC,
                    key=str(new_event["session_token"]).encode('utf-8'),
                    value=json.dumps(new_event).encode('utf-8'),
                    callback=on_delivery_success
                )
                
                data_stream_publisher.poll(0)
                
                time.sleep(0.5)
                
            except BufferError:
                data_stream_publisher.flush(timeout=1.0)
                time.sleep(1) 
            
            except Exception as e:
                LOG.error(f"Error during message production: {e}")
                
    except Exception as e:
        LOG.critical(f"Main loop failed unexpectedly: {e}")
    finally:
        initiate_graceful_exit(data_stream_publisher, None, None)