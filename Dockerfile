FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY ./django/Pipfile /

# Install dependencies.
RUN pip install pipenv
RUN pipenv install

# Set work directory.
RUN mkdir /hackertrailassessment
WORKDIR /hackertrailassessment

# Copy project code.
COPY . /hackertrailassessment_copy/

EXPOSE 8000