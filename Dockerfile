From python:3.9-slim

WORKDIR /app
ADD main.py /app

RUN pip install celery[redis]

CMD ["/bin/bash"]
#CMD [ "celery", "-A", "main", "worker", "-l", "info" ]
