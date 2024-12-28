# Use the official Python 3.12 image from the Docker Hub
FROM python:3.11-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and .env into the container
COPY pyproject.toml uv.lock ./

# Install the dependencies
RUN uv sync --frozen --no-cache

# Copy the rest of the application code into the container
COPY api ./api
COPY core ./core

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["/app/.venv/bin/uvicorn","api.app:app", "--host", "0.0.0.0", "--port", "8000"]