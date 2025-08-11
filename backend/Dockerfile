FROM python:3.11-slim
WORKDIR /app
# Install dependencies with no cache to reduce image size
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy only necessary files
COPY app/ app/
COPY main.py .
# Use non-root user
RUN useradd -l -u 1000 -g users -r -d /app appuser && \
    chown -R appuser:users /app
USER appuser
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--timeout", "120", "main:app"]