FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN rm .dockerignore
RUN rm Dockerfile
RUN rm requirements.txt

EXPOSE 5055

CMD ["gunicorn", "-b", "0.0.0.0:5055", "app"]