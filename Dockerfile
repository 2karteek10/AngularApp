FROM python:3.9-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ ./backend
#COPY frontend/dist/frontend ./frontend

# The CMD remains the same
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]