FROM inspircd/inspircd-docker

COPY inspircd.conf /inspircd/conf/

COPY start.sh /

# ENTRYPOINT [ "/bin/sh" ]
ENTRYPOINT [ "/bin/sh", "start.sh" ]