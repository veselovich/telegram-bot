# Use the Python base image
FROM python:3.10.2

# Set the working directory inside the container
WORKDIR .

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of application code
COPY . .

# Activate the virtual environment and set the CMD to run main.py script
CMD python main.py