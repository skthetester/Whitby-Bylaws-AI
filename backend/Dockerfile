# Use official Python image
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
# EXPOSE 5000
# CMD ["python", "main.py"]
