FROM python:3.12.0-slim

WORKDIR /ba

COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn && pip install psycopg2-binary

RUN apt update

COPY . .

EXPOSE 8000

RUN chmod a+x /ba/start.sh

ENTRYPOINT ["./start.sh"]