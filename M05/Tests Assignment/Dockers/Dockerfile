FROM python:3

WORKDIR /usr/src/app

COPY tax.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./tax.py"]