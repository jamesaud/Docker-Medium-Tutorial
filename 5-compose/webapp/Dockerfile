FROM  python:3.6 
  
COPY ./src/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt 

COPY ./src /app
WORKDIR /app

EXPOSE 5000
CMD python server.py