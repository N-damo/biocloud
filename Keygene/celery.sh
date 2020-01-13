#!/bin/bash


if [[ $1 == stop ]]
then
echo 'kill celery worker'
ps auxww|grep "celery worker"|grep -v grep|awk '{print $2}'|xargs kill -9 ;
exit
else
ps auxww|grep "celery worker"|grep -v grep|awk '{print $2}'|xargs kill -9 ;
celery worker -A Keygene -l info &
fi
