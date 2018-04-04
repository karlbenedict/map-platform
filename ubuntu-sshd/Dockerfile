FROM       ubuntu:16.04
MAINTAINER Karl Benedict 

RUN apt-get update

RUN apt-get install -y openssh-server
RUN apt-get install -y python3
RUN apt-get install -y unzip
RUN mkdir /var/run/sshd

# default root password is 'laugh-dallas-finger'
# change root password on startup with a new hashed passwordbuild
ENV pwhash='$6$UH.XvgqL1fMI2zQa$l1T5Hdzj214I6wGQRC3cMMu6m3ORaKfCqW2wTgLvccEUQZxlcBTAZlUyKmST3/FIk4ev/CcYyf0BFvlzPivXW1'

RUN echo 'root:'${pwhash} | chpasswd -e

RUN groupadd students
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN mkdir -p /opt/geoserver/data_dir/general
RUN chown -R :students /opt/geoserver/data_dir/general


RUN mkdir /startup
WORKDIR /startup
COPY GenerateUsers.py /startup
COPY words.txt /startup
RUN ./GenerateUsers.py

RUN chmod g+rw /opt/geoserver/data_dir/general
RUN chmod o-rwx /startup
WORKDIR /opt/geoserver/data_dir/general

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
