# TODO: Perhaps get rid of the virtual environment as I don't think it's needed when Docker is used

FROM python:3-onbuild

# Check that WORKDIR is correct - this is the working directory within the container
WORKDIR /usr/src/app

# Copy server_requirements.txt to the working directory of the Docker container?
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy contents of the current directory to the working directory of the Docker container?
COPY . .

# Execute python api.py
CMD ["python", "api.py"]