FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
ARG UBUNTU_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install python3.7
RUN apt-get install python3-pip -y
RUN apt-get install tesseract-ocr -y

WORKDIR /usr/bot/src

COPY requirements.txt ./

RUN pip install Pillow

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "./main.py"]