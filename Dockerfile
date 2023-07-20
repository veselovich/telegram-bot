# Use the Python base image
FROM python:3.10.2

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN apt-get update && pip install -r requirements.txt

# Copy the rest of application code
COPY . .

# Activate the virtual environment and set the CMD to run main.py script
CMD ["/bin/bash", "-c", "source /Users/romanveselov/Documents/Python/telegram-bot/telegram-bot/venv/bin/activate && python main.py"]