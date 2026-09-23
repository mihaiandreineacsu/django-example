FROM python:3.13.3-alpine3.22


ARG OUR_ARG=test_value

RUN echo "The value of OUR_ARG is: $OUR_ARG"

# Set environment variables
# Prevents Python from writing .pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures that Python output is sent straight to the terminal without buffering.
ENV PYTHONUNBUFFERED=1

ENV OUR_ENV=${OUR_ARG:-test_value}

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

# Dockerfile CMD doesn't understand ENV variables
# See Issue: https://github.com/moby/moby/issues/5509
CMD ["sh", "-c", "python manage.py migrate ; exec python manage.py runserver 0.0.0.0:8000"]
