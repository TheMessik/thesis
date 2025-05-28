#!/bin/bash

IRC_PORT="6667"
IRC_TOPIC="#loic"

# start the bot
# set the correct IP of IRC server
sed -i "s/host = localhost/host = $TARGET_IP_0/g" /bot/config.ini

export LOIC_USEGET=1
export LOIC_METHOD="$1"

source .venv/bin/activate
irc3 /bot/config.ini &

echo "Waiting for bot to boot up"
sleep 15

echo "Running loic with IRC $TARGET_IP_0:$IRC_PORT, topic $IRC_TOPIC, method $LOIC_METHOD"
xvfb-run mono src/bin/Debug/LOIC.exe /hidden /hivemind $TARGET_IP_0 $IRC_PORT $IRC_TOPIC
 