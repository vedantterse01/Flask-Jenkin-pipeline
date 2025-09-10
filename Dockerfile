
# Use a small Python base image
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 8000

# Use gunicorn in production; bind to 0.0.0.0 so container is reachable
# 'app:app' refers to the Flask instance 'app' in app.py
CMD ["gunicorn", "-b", "0.0.0.0:8000", "--workers", "2", "--threads", "4", "app:app"]
