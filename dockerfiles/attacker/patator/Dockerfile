# Dockerfile for conducting attacks
# Based on https://github.com/mielverkerken/student-host-space-concap/blob/main/container_images/patator/Dockerfile.cic, extended with custom wordlists

# Credits and thanks to Miel Verkerken
FROM ubuntu:18.04

RUN apt update && apt install python3 python3-pip git libcurl4-openssl-dev libmysqlclient-dev libpq-dev -y

WORKDIR /patator

RUN git clone --depth 1 --branch 0.8 https://github.com/lanjelot/patator.git .

RUN sed -i "s/paramiko/paramiko==2.0.0/" requirements.txt \
    && echo "validators" >> requirements.txt \ 
    && pip3 install -r requirements.txt

# include security lists in the image
COPY run.py usernames.txt passwords.txt /tmp/

ENTRYPOINT ["/bin/bash"]
# ENTRYPOINT ["python3", "patator.py"]