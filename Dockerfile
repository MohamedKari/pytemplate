FROM python:3.8-alpine
LABEL maintainer="Mohamed Kari <contact@mkari.de>"

# Use caching if dependencies did not change
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY dist dist
RUN pip install /dist/*.whl

RUN mkdir -p /logs

ENTRYPOINT [ "python", "-m", "PKG_NAME", "-l", "/logs"]