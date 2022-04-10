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
WORKDIR /opt/app
COPY --from=build /opt/app/venv ./venv
COPY . .

ENV PATH="/opt/app/venv/bin:$PATH"

EXPOSE 8899
CMD ["python3", "app.py"]