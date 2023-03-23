# base image
FROM python:3.9

# set working directory
WORKDIR /app

# copy project files to working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# expose port 5000 for the Flask app
EXPOSE 5000

# run the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
