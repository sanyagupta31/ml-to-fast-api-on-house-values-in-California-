#Dcokerfile
# 1. Use an official Python runtime as a parent image
FROM python:3.9-slim
#2. set the working directory inside the container
WORKDIR /app
#3.copy the dependencies file and install them 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#4.copy the rest of the application code into the container
COPY . .
#5. Expose the port that the application will run on
EXPOSE 80
#6. Set the command to run the application
CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "10000"]
