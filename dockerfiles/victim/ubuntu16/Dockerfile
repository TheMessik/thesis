FROM ubuntu:16.04 AS bootstrap

# install the required packages
RUN apt-get update \
	&& apt-get install -y vsftpd db-util build-essential python python-dev libgnutls-dev libacl1-dev libldap2-dev netcat

### FTP setup
ENV FTP_USER victim
ENV FTP_PASS victim

COPY ftp/vsftpd.conf /etc/vsftpd/
COPY ftp/vsftpd_virtual /etc/pam.d/
COPY ftp/run-vsftpd.sh /usr/sbin/

RUN chmod +x /usr/sbin/run-vsftpd.sh && \
	mkdir -p /var/run/vsftpd/empty

VOLUME /home/vsftpd
VOLUME /var/log/vsftpd


### SSH setup
# copyright Miel Verkerken
ENV DEBIAN_FRONTEND=noninteractive
COPY ssh/src/ /tmp/bin
RUN apt-get -f install -y /tmp/bin/openssh-client_7.2p2-4ubuntu2.2_amd64.deb && \
	apt-get -f install -y /tmp/bin/openssh-sftp-server_7.2p2-4ubuntu2.2_amd64.deb && \
	apt-get -f install -y /tmp/bin/openssh-server_7.2p2-4ubuntu2.2_amd64.deb && \
	rm -rf /var/lib/apt/lists* && \
	rm -rf /tmp/bin

RUN mkdir /var/run/sshd

ARG SETUP_SCRIPT=ssh/config/password-setup.sh
COPY --chmod=0755 ${SETUP_SCRIPT} /usr/local/bin/setup.sh

RUN /usr/local/bin/setup.sh victim victim

# ========================= HTTP setup ============================================ #
FROM bootstrap AS build_apache
WORKDIR /apache
COPY apache/httpd-2.2.32.tar.gz .
RUN tar -xzf ./httpd-2.2.32.tar.gz \
	&& ./httpd-2.2.32/configure --prefix="/usr/local/apache2" \
	&& make \
	&& make install

# ========================= Final setup =========================================== #
FROM bootstrap AS final

COPY --from=build_apache /usr/local/apache2 /usr/local/apache2

# wrapper to run all services
COPY --chmod=0755 wrapper.sh /wrapper.sh

# Expose all services
EXPOSE 20 21 22 80 139 445

CMD ["/wrapper.sh"]
