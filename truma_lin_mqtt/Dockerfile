ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Installiere Python 3 + PySerial im Alpine-basierten Container
RUN apk add --no-cache python3 py3-pip py3-pyserial

# Skripte kopieren
COPY run.sh /run.sh
COPY truma_lin_bridge.py /truma_lin_bridge.py

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
