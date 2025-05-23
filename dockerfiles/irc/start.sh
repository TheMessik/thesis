#!/bin/sh

# start the server
/entrypoint.sh --runasroot &

wait -n

exit 0