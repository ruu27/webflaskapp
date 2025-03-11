# base image from hub.docker.com (python image, 3.11-slim tag)
FROM python:3.11-slim

# Empty computer. now create a new folder "flask-app"
WORKDIR /flask-app

# Copy the requirements.txt file and required directories into docker image
# ./ because looking from root folder where Dockerfile is now.
# copy <source> <new path in docker container>
COPY ./requirements.txt /flask-app/requirements.txt
COPY ./src /flask-app/src
COPY ./model /flask-app/model

# Add /src directory to PYTHONPATH, so that model.py Python module can be found
# To add multiple directories, delimit with colon e.g. /flask-app/src:/flask-app
# tells them where the environment variable path is
# ENV PYTHONPATH <path of source folder> === export PYTHONPATH=/flask-app/src
ENV PYTHONPATH=/flask-app/src

# Install python package dependancies, without saving downloaded packages locally
# no-cache-dir if really low on space. cache is to help with installing again in future images
RUN pip install -r /flask-app/requirements.txt --no-cache-dir

# Allow port 80 to be accessed (Flask app)
EXPOSE 80

# Start the Flask app using gunicorn
# runs only when docker run.. is run
CMD ["gunicorn", "--bind=0.0.0.0:80", "src.app:app"]