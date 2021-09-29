FROM python:3.9
COPY . /app
WORKDIR /app
RUN apt-get update -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system
CMD [ "python", "run.py"]