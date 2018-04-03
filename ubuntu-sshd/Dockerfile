FROM       ubuntu:16.04
MAINTAINER Karl Benedict 

RUN apt-get update

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# default root password is 'nintendo-lending-evening'
# change root password on startup with a new hashed passwordbuild
ENV pwhash='$6nh0R1XSq.Dk'

RUN echo 'root:'${pwhash} |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
