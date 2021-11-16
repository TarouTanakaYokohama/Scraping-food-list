FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install beautifulsoup4
RUN pip install requests

RUN pip install --upgrade firebase-admin
RUN pip install google-cloud-firestore
RUN pip install janome

# RUN pip install -U -y ginza ja-ginza-electra
# RUN pip install -U ginza https://github.com/megagonlabs/ginza/releases/download/latest/ja_ginza_electra-latest-with-model.tar.gz
# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -U ginza ja-ginza