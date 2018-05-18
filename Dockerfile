FROM python:3-slim

COPY . /src

RUN pip install /src && \
    cp /usr/local/bin/xmrig_exporter /xmrig_exporter

EXPOSE 9189

ENTRYPOINT ["/xmrig_exporter"]
