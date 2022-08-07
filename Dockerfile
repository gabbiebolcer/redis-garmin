FROM python:3.9-slim

RUN python -m venv /opt/venv
ENV PATH = "/opt/venv/bin:$PATH"

WORKDIR /home/
COPY setup.py .
COPY requirements.txt .
COPY garmin_redis/ garmin_redis/

RUN chmod +x garmin_redis/redis_hello_world.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .