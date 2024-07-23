FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install development dependencies for hot reloading
RUN pip install --no-cache-dir uvicorn[standard] watchgod

# Copy the rest of the application
COPY . .

# Command to run the application with hot reloading
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
