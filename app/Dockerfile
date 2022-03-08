FROM python:3.8-slim
LABEL VERSION=1.0
LABEL NAME=app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY app.py .
EXPOSE 8000
ENTRYPOINT ["gunicorn", "app:app", "--bind=0.0.0.0:8000", "--workers=4", "--reload"]
CMD ["--log-level=info"]