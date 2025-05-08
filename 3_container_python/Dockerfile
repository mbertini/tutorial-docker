# Use an official Python runtime as a parent image
# check the available tags at https://hub.docker.com/_/python/tags
FROM python:3.7-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy only requirement file in order to optmizize build process
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable. = is a more modern style
ENV NAME=PPM

# Run app.py when the container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]