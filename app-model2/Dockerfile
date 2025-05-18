FROM python:3.13-slim

# Set the working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "app.py", "run", "--port=5001" ]