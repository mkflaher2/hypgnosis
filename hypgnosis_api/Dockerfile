FROM python:3.10

WORKDIR /src/

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# setup codebase

COPY . /src/

# setup environment and run
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ["python", "-m", "hypgnosis_api.api"]
