FROM ghcr.io/hassio-addons/debian-base/amd64:7.2.0

ENV LANG C.UTF-8

# Update und Installation mit apt-get
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-serial \
    && rm -rf /var/lib/apt/lists/*

COPY run.sh /run.sh
COPY truma_lin_bridge.py /truma_lin_bridge.py

CMD [ "/run.sh" ]
