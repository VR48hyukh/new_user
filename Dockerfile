FROM python:3.12-slim

WORKDIR /app
COPY . /app

# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry==1.7.0

CMD ["python", "-m", "src/users"]
