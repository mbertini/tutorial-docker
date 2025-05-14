FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3-pip python3-dev

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python3", "app.py"]
