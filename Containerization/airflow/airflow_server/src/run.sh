#!/bin/bash

airflow initdb

if [[ $SETTING = scheduler ]]
then
  airflow scheduler
elif [[ $SETTING = webserver ]]
then
  airflow webserver -p 8080
else
  nohup airflow scheduler $* >> ~/airflow/logs/scheduler.log &

  airflow webserver -p 8080
fi
