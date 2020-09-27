FROM python3

ADD datetime_script.py /

RUN apt-get update
RUN spt-get install -y python python-pip
RUN pip install flask 
RUN pip install pystrich

COPY datetime.py home/lir/datetime-app/datetime.py

#ENTRYPOINT FLASK_APP=datetimeapp.py flask run --host=0.0.0.0

CMD [ "python", "./datetime_script.py" ]

