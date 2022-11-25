FROM python:3.9.10

LABEL maintener="koura <koura@weg.net>"

ENV PYTHONBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV USER_NAME=sales_wmo_mi
ENV USER_PASSWORD=sales_wmo_mi
ENV DB_HOST=racdev01
ENV DB_PORT=1521
ENV DB_SERVICE=DWA


EXPOSE 8000:8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]