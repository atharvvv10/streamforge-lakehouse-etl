
FROM alpine:3.18 AS connector-fetcher
RUN apk add --no-cache curl
ENV MAVEN_JARS_PATH=/tmp/jars
RUN mkdir -p ${MAVEN_JARS_PATH} && \
    curl -fSL https://repo1.maven.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.1.0-1.18/flink-sql-connector-kafka-3.1.0-1.18.jar -o ${MAVEN_JARS_PATH}/kafka.jar && \
    curl -fSL https://repo.maven.apache.org/maven2/org/apache/flink/flink-json/1.18.1/flink-json-1.18.1.jar -o ${MAVEN_JARS_PATH}/json.jar && \
    curl -fSL https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-flink-runtime-1.18/1.5.0/iceberg-flink-runtime-1.18-1.5.0.jar -o ${MAVEN_JARS_PATH}/iceberg.jar && \
    curl -fSL https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/2.20.18/bundle-2.20.18.jar -o ${MAVEN_JARS_PATH}/aws-s3.jar && \
    curl -fSL https://repo.maven.apache.org/maven2/org/apache/flink/flink-shaded-hadoop-2-uber/2.8.3-10.0/flink-shaded-hadoop-2-uber-2.8.3-10.0.jar -o ${MAVEN_JARS_PATH}/hadoop-shaded.jar


FROM flink:1.18.1-scala_2.12-java11
ENV FLINK_CONNECTOR_DIR=${FLINK_HOME}/lib
COPY --from=connector-fetcher /tmp/jars/kafka.jar ${FLINK_CONNECTOR_DIR}/kafka-connector.jar
COPY --from=connector-fetcher /tmp/jars/json.jar ${FLINK_CONNECTOR_DIR}/json-format.jar
COPY --from=connector-fetcher /tmp/jars/iceberg.jar ${FLINK_CONNECTOR_DIR}/iceberg-runtime.jar
COPY --from=connector-fetcher /tmp/jars/aws-s3.jar ${FLINK_CONNECTOR_DIR}/s3-bundle.jar
COPY --from=connector-fetcher /tmp/jars/hadoop-shaded.jar ${FLINK_CONNECTOR_DIR}/hadoop-uber.jar
WORKDIR /opt/flink
CMD ["/bin/bash", "-c", "exec ${FLINK_HOME}/bin/sql-client.sh & wait $! || tail -f /dev/null"]