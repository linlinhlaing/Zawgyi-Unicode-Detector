# Use the official Python image from Docker Hub
FROM python:3.8-slim

# update pip to minimize dependency errors 
RUN pip install --upgrade pip
# define the present working directory
WORKDIR /docker-flask-test

# copy the contents into the working dir
ADD . /docker-flask-test

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable to prevent Python from buffering outputs
ENV PYTHONUNBUFFERED=1

# Run the Flask app
CMD ["python", "app.py"]
