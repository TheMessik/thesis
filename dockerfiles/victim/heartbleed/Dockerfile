FROM ubuntu:16.04

# https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/auxiliary/scanner/ssl/openssl_heartbleed.md
RUN apt-get update && apt-get install -y build-essential wget \
    && wget https://github.com/openssl/openssl/releases/download/OpenSSL_1_0_1f/openssl-1.0.1f.tar.gz \
    && tar -zxf openssl-1.0.1f.tar.gz \
    && cd openssl-1.0.1f \
    && ./config \
    && make \
    && make install_sw

WORKDIR /

COPY files/cert.pem files/key.pem /

CMD ["/usr/local/ssl/bin/openssl", "s_server", "-key", "key.pem", "-cert", "cert.pem", "-accept", "443", "-www"]
