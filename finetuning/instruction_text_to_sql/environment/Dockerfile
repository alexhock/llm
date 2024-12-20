FROM pytorch/pytorch:2.1.2-cuda11.8-cudnn8-devel

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN pip3 install flash-attn --no-build-isolation