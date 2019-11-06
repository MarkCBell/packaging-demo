
FROM python:latest

RUN pip install pip --upgrade
RUN pip install git+git://github.com/MarkCBell/curver.git@dev

CMD python soln202.py
