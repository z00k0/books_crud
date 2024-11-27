FROM python:3.11-slim

# Эта переменная окружения устанавливает флаг для интерпретатора Python, чтобы не создавать .pyc файлы (компилированные файлы байткода) при выполнении Python-скриптов
ENV PYTHONDONTWRITEBYTECODE=1
# Когда флаг установлен в 1, вывод Python не будет буферизоваться, и данные будут сразу же выводиться на стандартные потоки вывода (например, на терминал или в лог-файл)
ENV PYTHONUNBUFFERED=1

WORKDIR /books

COPY ./entrypoint.sh .
COPY ./.env .

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./books ./books
