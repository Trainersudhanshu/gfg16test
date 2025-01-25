FROM python:3.9-slim

# Create a non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies as root user first (this step needs root permissions)
RUN pip install -r requirements.txt

# Give the appuser full permissions on the /app directory
RUN chown -R appuser:appuser /app

# Expose port 80
EXPOSE 80

# Switch to the non-root user
USER appuser

# Run the application as the non-root user
ENTRYPOINT ["python", "app.py"]
