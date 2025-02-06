FROM python:3.10.11-alpine

WORKDIR /app

ARG DJANGO_PORT="8000"

COPY . .

RUN pip install -r requirements.txt

EXPOSE ${DJANGO_PORT}

CMD ["python", "manage.py", "runserver", "0.0.0.0:${DJANGO_PORT}"]