FROM python:3.8 as build
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
build-essential gcc

WORKDIR /opt/app
RUN python3 -m venv /opt/app/venv
ENV PATH="/opt/app/venv/bin:$PATH"
COPY requirements.txt /opt/app

# Install app dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM python:3.8-slim

RUN groupadd -g 999 python && useradd -r -u 999 -g python python
RUN mkdir -p /opt/app && chown python:python /opt/app
WORKDIR /opt/app

COPY --chown=python:python --from=build /opt/app/venv ./venv
COPY --chown=python:python . .

USER 999
ENV PATH="/opt/app/venv/bin:$PATH"

CMD ["python3", "app.py"]