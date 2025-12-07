# Use a small official Python image
FROM python:3.11-slim

# Avoid Python writing .pyc files and using stdin buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (if needed for reportlab / pillow fonts etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better build caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code into the container
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Streamlit: disable opening browser automatically, listen on all interfaces
CMD ["streamlit", "run", "daa_streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
