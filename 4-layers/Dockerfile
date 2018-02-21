# 4-layers/Dockerfile
FROM  python:3.6   

COPY ./src /app                               
WORKDIR /app   

RUN pip install -r requirements.txt    

EXPOSE 5000
CMD python server.py

