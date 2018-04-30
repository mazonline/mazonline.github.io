#!/bin/bash 
mkdir /work/
cd /work 
apt-get update 
apt-get install -y wget
apt-get install -y python-pip
apt-get install -y vim
apt-get install -y curl
apt-get install -y firefox
pip install selenium 

#links 
wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux32.tar.gz
wget https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip
