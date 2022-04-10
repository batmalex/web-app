FROM python:3.8-slim

WORKDIR /opt/app
COPY . /opt/app

# Install app dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8899

#CMD ["/bin/bash", "-c", "sleep 5000"]
CMD ["python3", "app.py"]