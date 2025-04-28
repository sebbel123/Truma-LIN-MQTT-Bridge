FROM ghcr.io/hassio-addons/debian-base/amd64:7.2.0

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip py3-serial

COPY run.sh /run.sh
COPY truma_lin_bridge.py /truma_lin_bridge.py

CMD [ "/run.sh" ]
