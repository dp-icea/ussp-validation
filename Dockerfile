FROM python:3.12-slim
USER root

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv
RUN pip install pip-tools && pip-compile --generate-hashes --output-file=requirements.txt requirements.in \
    && pip install -r requirements.txt

CMD ["pytest", "tests/api/test.py"]

