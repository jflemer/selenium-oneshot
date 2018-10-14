FROM python:alpine3.7

WORKDIR /opt/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HUB_HOST hub
ENV HUB_PORT 4444

CMD [ "python", "./runner.py" ]
