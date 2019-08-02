FROM python:3.7-buster
WORKDIR /srv/http/app
COPY ./requirements.txt /
RUN python -m pip install --no-cache-dir -r /requirements.txt
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
