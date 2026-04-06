# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install flask pymongo python-dotenv selenium webdriver-manager requests

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]