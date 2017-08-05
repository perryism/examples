FROM ubuntu

MAINTAINER Perry

RUN apt-get update && apt-get install -y \
   python \
   python-dev \
   python-pip \
   bash \
   && rm -rf /var/lib/apt/lists/* \
   && pip install --upgrade pip

VOLUME ["/notebooks"]

ADD requirements.txt . 
RUN pip install -r requirements.txt

WORKDIR /notebooks

EXPOSE 8888

RUN jupyter serverextension enable --py jupyterlab --sys-prefix

CMD jupyter lab --allow-root --ip=* --no-browser
