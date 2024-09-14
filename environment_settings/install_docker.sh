#!/usr/bin/env bash

# git lfs install
sudo apt update
suto apt install git-lfs
git lfs install

# docker install
## set up repository
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

## install docker ce
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose -y

## join docker group
sudo gpasswd -a $USER docker

# make no need to enter password for "sudo service docker start"
echo "$USER ALL=(ALL:ALL) NOPASSWD: /usr/sbin/service docker start" | sudo EDITOR="tee" visudo -f /etc/sudoers.d/service_docker_start

# docker service run
cat << '#end' >> ~/.bashrc

# start docker only when docker daemon is not running
if test $(service docker status | awk '{print $4}') = 'not'; then
    sudo service docker start
fi
#end
