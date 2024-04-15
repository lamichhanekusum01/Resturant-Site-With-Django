# base image  
FROM python:3.11.4
# setup environment variable  
ENV DockerHOME=/usr/src/app

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

COPY ./entrypoint.sh ${DockerHOME}
# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  

# RUN python manage.py makemigration
# RUN python manage.py migrate

#ENTRYPOINT [ "usr/src/app/entrypoint.sh" ]