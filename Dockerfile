# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /code
WORKDIR /code

# Copy the entrypoint script and grant execution permissions
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

# Copy the current directory contents into the container at /code
COPY ./DjangoChallenge /code/

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
