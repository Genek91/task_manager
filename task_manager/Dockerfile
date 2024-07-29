FROM python:3.12

WORKDIR /task_manager

COPY ./requirements.txt /task_manager/requirements.txt
# COPY ./.env /task_manager/.env

RUN pip install -r /task_manager/requirements.txt --no-cache-dir

COPY . /task_manager

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
