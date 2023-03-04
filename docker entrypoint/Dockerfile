FROM python:3.10-slim-buster

RUN apt update && apt install openssh-server sudo -y
RUN apt install git sudo -y

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test 

RUN  echo 'test:test' | chpasswd

RUN service ssh start

ADD entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
# ENTRYPOINT ["git", "clone"]
# CMD tail -f /dev/null
CMD ["/usr/sbin/sshd", "-D"]