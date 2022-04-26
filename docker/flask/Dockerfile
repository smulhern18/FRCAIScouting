# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR .
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY .. .
CMD ["flask", "run", "--host", "0.0.0.0", "-p", "80"]