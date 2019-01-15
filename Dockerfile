FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
ENV ENV=someLicenseInfo
RUN pip install -r requirements.txt
EXPOSE 5000

CMD [ "python", "app.py" ]
