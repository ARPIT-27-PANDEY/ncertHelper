FROM python:3.11

WORKDIR /app

# Update package lists and install any necessary dependencies
RUN apt-get update \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -U --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Set the entry point to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "server.py", "--server.port=8501", "--server.address=0.0.0.0"]
