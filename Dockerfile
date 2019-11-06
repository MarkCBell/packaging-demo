
FROM sagemath/sagemath:latest

RUN sage -pip install pip --upgrade
RUN sage -pip install numpy

COPY ./euler202 ./euler202

CMD ["sage", "-python", "euler202"]
