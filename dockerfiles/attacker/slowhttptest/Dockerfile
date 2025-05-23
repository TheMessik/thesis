FROM debian:stable-slim

RUN apt-get update && apt-get install -y g++ openssl libssl-dev make git

WORKDIR /slowhttptest

RUN git clone https://github.com/shekyan/slowhttptest.git . && git checkout 0bacd4ea1490a5151372c7fb76ff0cece03ca017

RUN ./configure --prefix=/usr/local && make && make install

ENTRYPOINT ["sh", "-c"]

# RUN mkdir /slowhttptest
# WORKDIR /slowhttptest
# COPY . /slowhttptest
# RUN ./configure --prefix=/usr/local
# RUN make && make install
# ENTRYPOINT ["sh", "-c"]
