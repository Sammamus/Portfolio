FROM python:3.8.3
MAINTAINER Darian Raffle

RUN pip3 install flask==1.1.2
RUN pip3 install botocore==1.16.25
RUN pip3 install apache-airflow==1.10.10
RUN pip3 install 'apache-airflow[postgres, aws, kubernetes, mysql]==1.10.10'
RUN pip3 install typing_extensions==3.7.4.2
RUN pip3 install mysqlclient==1.3.14
RUN pip3 install psycopg2==2.8.5

ADD src/run.sh /root/run.sh

CMD ["/bin/bash", "./root/run.sh"]
