# Base image
FROM python:3.9

# Working directory
WORKDIR /app

# Copy 
COPY . /app/

# Run
RUN pip install -r requirements.txt

# Ports
EXPOSE 5000

# Command
CMD [ "python","./app.py" ]