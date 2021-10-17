# Dockerfile, Image, Container

FROM python:3.9

ADD factorial-digits.py . 

RUN pip install numpy 

ENTRYPOINT [ "python", "factorial-digits.py" ]