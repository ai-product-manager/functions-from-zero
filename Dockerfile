FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" , "--port", "8080" ]