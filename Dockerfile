FROM python:3.12-slim
WORKDIR /app
COPY . .
ENTRYPOINT ["python","-m","src.cli"]
CMD ["examples/postgres_failure.log"]
