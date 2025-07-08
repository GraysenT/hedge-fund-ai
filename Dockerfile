# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for production mode (optional)
ENV ENV=production

# Run the main execution loop
CMD ["python3", "runloop.py"]