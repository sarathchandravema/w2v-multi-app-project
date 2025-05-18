FROM python:3.11.5-slim

# Set the working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "model1.py", "run", "--port=5000", "--host=0.0.0.0" ]