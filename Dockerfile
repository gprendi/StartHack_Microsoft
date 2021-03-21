FROM python:latest

COPY . /WebAPP

WORKDIR /WebAPP

RUN apt update -y && apt upgrade -y

RUN pip3 install -r requirements.txt

EXPOSE 5000/tcp

CMD python3 app.py --no-debugger