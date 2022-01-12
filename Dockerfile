FROM ubuntu:latest
RUN apt-get update && apt-get autoclean
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install -y --no-install-recommends python3-pip
RUN pip3 install image
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "./main.py" ]