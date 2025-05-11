FROM --platform=$BUILDPLATFORM apache/airflow:2.7.3-python3.9
ENV AIRFLOW_HOME=/opt/airflow
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
