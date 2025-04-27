# Use the official Python 3.12 image from the Docker Hub
FROM 3.13-slim-bookworm AS builder

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory in the container
WORKDIR /app

# Enable bytecode compilation for faster startup time
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM 3.13-slim-bookworm AS runtime

# Copy the application from the builder
COPY --from=builder --chown=app:app /app /app

WORKDIR /app

# Expose the port the app runs on
EXPOSE 8000

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Command to run the application
CMD ["uvicorn","api.app:app", "--host", "0.0.0.0", "--port", "8000"]