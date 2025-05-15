FROM python:3.11-slim

# Set environment variables
# Set PYTHONUNBUFFERED=1 to ensure logs are output immediately.
# Set PIP_NO_CACHE_DIR=1 to prevent caching, reducing image size.
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# set the  working directory
WORKDIR /code

# Install system dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/