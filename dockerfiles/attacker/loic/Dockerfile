FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y git sudo apt-transport-https ca-certificates netcat xvfb python3 python3-pip python3-venv

# Install Mono for LOIC
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-xenial main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && \
    apt-get install -y mono-complete liblog4net-cil-dev

# prepare LOIC
RUN git clone https://github.com/NewEraCracker/LOIC.git /loic

WORKDIR /loic

# get correct commit, use correct HTTP version and compile LOIC
RUN git checkout 6edd91c &&\ 
    sed -i "s/HTTP\/1.1/HTTP\/1.0/" ./src/Functions.cs &&\
    cd src && xbuild /p:TargetFrameworkVersion="v4.5"

COPY entrypoint.sh .

# prepare python environment for the bot
RUN python3 -m venv .venv && . .venv/bin/activate && pip3 install irc3
COPY bot /bot
