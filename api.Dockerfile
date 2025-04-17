FROM python:3.13.3-alpine

WORKDIR /app

ARG ARG_DJANGO_PORT="8000"
ENV ENV_DJANGO_PORT=${ARG_DJANGO_PORT}

COPY . .

RUN pip install -r requirements.txt

EXPOSE ${ENV_DJANGO_PORT}


# Dockerfile CMD doesn't understand ENV variables
# See Issue: https://github.com/moby/moby/issues/5509
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${ENV_DJANGO_PORT}"]
