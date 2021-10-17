# Dockerfile, Image, Container

FROM python:3.9

ADD corigine.py . 

RUN pip install numpy 

ENTRYPOINT [ "python", "corigine.py" ]