FROM python:3.9-slim

RUN python -m venv /opt/venv
ENV PATH = "/opt/venv/bin:$PATH"

WORKDIR /home/
COPY garmin_redis/ $WORKDIR/garmin_redis
COPY setup.py $WORKDIR
COPY requirements.txt $WORKDIR

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .