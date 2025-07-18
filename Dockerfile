FROM python:3.10

WORKDIR /app
COPY . .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

# execute ls command
RUN ls -l

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]