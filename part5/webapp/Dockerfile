FROM  python:3.6   

# Create a directory
WORKDIR /app                  

# Copy the app code
COPY . ./                                  

# Install Requirements
RUN pip install -r requirements.txt  

# Expose flask's port
EXPOSE 5000

# Run the server
CMD python server.py 

