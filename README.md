# test_test
## Introduction
This Dockerfile sets up an environment for running a Python application using a specified Python version. It ensures that the application runs under a non-privileged user (appuser) to enhance security.

### What to do ?
This setup enables easy building and running of your Python application using Docker and Docker Compose. By following these instructions, you can ensure a consistent environment for your application, making it easier to test

## Steps to Setup:
Fork this repo.
* Clone on your local machine. `git clone https://github.com/andriimu/test_test`

* Navigate to project directory. `cd test_task`

* Create a new virtualenv. `python -m venv venv`

* Commit your changes on UNIX. `source venv/bin/activate` or for Windows `.\venv\Scripts\activate `

* Create a new image for docker. `docker build -t (name_of_your_image) .`

* Run a new image for docker on preferred port. `docker run -p (preferred_available_port):8001 (name_of_your_image)`

* Builds the Docker image using the Dockerfile. `docker compose build`

* Run the application. `docker compose up`

