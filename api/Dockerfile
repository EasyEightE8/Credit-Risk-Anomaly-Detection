# Dockerfile for the API service
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file source to the container
COPY api/requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY api/ /app/

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]