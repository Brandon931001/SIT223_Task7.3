FROM python:3.10-slim
WORKDIR /app
COPY garage/ garage/
CMD ["python3"]
