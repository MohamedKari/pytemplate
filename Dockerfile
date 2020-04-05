FROM python:3.8-alpine
LABEL maintainer="Mohamed Kari <contact@mkari.de>"

COPY dist dist
RUN pip install /dist/*.whl

RUN mkdir -p /logs

ENTRYPOINT [ "python", "-m", "PKG_NAME", "-l", "/logs"]