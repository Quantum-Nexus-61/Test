# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy your script and dependencies into the container
COPY llm.py /app/
COPY requirements.txt /app/

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Run your script when the container launches
CMD ["python", "llm.py"]