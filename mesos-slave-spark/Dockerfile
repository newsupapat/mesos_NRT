FROM datastrophic/mesos-spark

#Docker
RUN apt-get update
RUN apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
RUN apt-get -y update && apt-get install -y docker-ce docker-ce-cli containerd.io

ENV MESOS_CONTAINERIZERS docker,mesos
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins

CMD ["mesos-slave", "--no-systemd_enable_support"]