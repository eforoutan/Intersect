FROM python:3.9-slim

RUN pip install geopandas

WORKDIR /app

COPY intersect_shp.py /app/intersect_shp.py

ENTRYPOINT [ "python3", "/app/intersect_shp.py" ]