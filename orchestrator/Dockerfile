FROM baseimage:latest
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y curl
CMD ["python", "app.py"]