# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
COPY ./img /code/img
COPY ./db/generate_db.py /code/db/generate_db.py

RUN python /code/db/generate_db.py
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
