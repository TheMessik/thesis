FROM python:3.11-slim

WORKDIR /app/

RUN apt-get update && apt-get install -y git && git clone https://github.com/TheMessik/GoldenEye.git /app/

ENTRYPOINT ["python", "goldeneye.py"]

