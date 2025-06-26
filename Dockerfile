FROM python:3.13.3-alpine

# Set environment variables
# Prevents Python from writing .pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures that Python output is sent straight to the terminal without buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

# Dockerfile CMD doesn't understand ENV variables
# See Issue: https://github.com/moby/moby/issues/5509
CMD ["sh", "-c", "python manage.py makemigrations ; python manage.py migrate ; exec python manage.py runserver 0.0.0.0:8000"]
