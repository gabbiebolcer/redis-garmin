FROM python3.9-slim

RUN python -m venv /opt/venv
ENV PATH = "/opt/venv/bin:$PATH"

WORKDIR /home/
COPY garmin_redis/ $WORKDIR/garmin_redis
COPY setup.py $WORKDIR

RUN pip install -e 