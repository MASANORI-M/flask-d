FROM python:3.10.0

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", ":5001", "run:run"]