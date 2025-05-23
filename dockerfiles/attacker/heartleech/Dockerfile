FROM ubuntu:16.04

WORKDIR /openssl

RUN apt update && apt install -y build-essential git

# compile specific OpenSSL version to make heartleech work
RUN git clone https://github.com/openssl/openssl.git . \
    && git checkout c4afc40a9b6ca3481642e1bc58164108ee700445 \
    && ./config \
    && make depend \
    && make

COPY heartleech.c /openssl/

# link heartleech against these versions
RUN gcc heartleech.c libssl.a libcrypto.a -ldl -lpthread -o heartleech -I./include

CMD ["/bin/bash", "-c"]
