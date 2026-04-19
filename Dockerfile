FROM ghcr.io/astral-sh/uv:0.4.20 AS uv

FROM python:3.13-slim


ENV PYTHONUNBUFFERED=1

ENV UV_LINK_MODE=copy \
  UV_COMPILE_BYTECODE=1 \
  UV_PYTHON_DOWNLOADS=never \
  UV_PROJECT_ENVIRONMENT=/.venv \
  UV_LOCKED=1




RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  # Runtime operation and debug tools
  curl \
  psmisc \
  tree \
  \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/cache/apt/*


COPY --from=uv /uv /usr/local/bin/uv

WORKDIR /app