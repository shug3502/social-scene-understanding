FROM python:3.6.4

# Set the working directory to /app
WORKDIR /social-scene-understanding

# Copy the current directory contents into the container at /app
ADD . /social-scene-understanding

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

# ensure local python is preferred over distribution python
#ENV PATH /usr/local/bin:$PATH
ENV NAME World

CMD "./run_training_part_a.sh"
