# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose port
EXPOSE 8000

# Run the Flask application
CMD ["python", "app.py"]
