#!/bin/bash

# A wrapper script to startup multiple processes in the container
# start up all processes
# ftp
/usr/sbin/run-vsftpd.sh &

# ssh
/usr/sbin/sshd -D &

# http
/usr/local/apache2/bin/httpd

nc -l -p 139 &
nc -l -p 445 &

wait -n

exit $?
