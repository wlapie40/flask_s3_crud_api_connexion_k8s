FROM python:3.8.1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "appy.py"]