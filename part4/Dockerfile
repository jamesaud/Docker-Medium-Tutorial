FROM  python:3.6   
WORKDIR /app

# Install requirements before copying over the app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

# Copy over all app files
COPY . ./
EXPOSE 5000
CMD python server.py
