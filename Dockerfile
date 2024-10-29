
FROM jupyter/pyspark-notebook:spark-3.5.0

USER root
RUN pip install delta-spark==3.2.0

USER $NB_UID
