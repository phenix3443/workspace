#! /bin/bash
# author:phenix3443@gmail.com
# desc: 初始化系统环境

PROJECT_DIR=$(cd $(dirname $0);pwd)

echo "creat github dir"
GITHUB_PATH="~/github"
mkdir -p ${GITHUB_PATH}

echo "create gitlab dir"
GITLAB_PATH="~/gitlab"
mkdir -p ${GITLAB_PATH}

echo "for application"
sudo apt update && \
    suod apt upgrade -y && \
    suod apt install -y shutter alacarte chromium-browser smplay wine-development \
        aria2 curl snapd

echo "for snap"
sudo apt install -y snapd && sudo systemctl enable --now snapd.socket

echo "for GFW"
sudo apt install shadowsocks-libev proxychains4

echo "for zeal" && \
    sudo add-apt-repository ppa:zeal-developers/ppa && \
    sudo apt install -y zeal

# https://software.opensuse.org/download.html?project=home:manuelschneid3r&package=albert
echo "install albert" && \
    echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' | sudo tee /etc/apt/sources.list.d/home:manuelschneid3r.list && \
    curl -fsSL https://download.opensuse.org/repositories/home:manuelschneid3r/xUbuntu_18.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home:manuelschneid3r.gpg > /dev/null && \
    sudo apt update && sudo apt install albert

echo "for terminal"
sudo apt install tmux bash-completion powerline fonts-powerline

echo "for git"
sudo apt install git git-flow

echo "for ssh"
sudo apt install zssh sshfs

echo "config develop enviroments"
sudo apt install -y build-essential automake autoconf libtool gcc cmake python3-pygit2

echo "common emacs"
sudo apt install -y global ccls

echo "config C/C++"
sudo apt install -y cppcheck clang clang-format

echo "config Lua"
sudo apt install -y lua5.1 luarocks

echo "config Python3"
sudo apt install -y python3 python3-dev python3-pip

echo "config golang"
sudo apt install -y golang

echo "config JavaScript"
sudo apt install -y npm yarn

echo "config markdown"
sudo apt install -y markdown pandoc

echo "install php"
sudo apt install -y php phpmd php-codesniffer

echo "config open-jdk"
# sudo apt install -y default-jdk

echo "config oracle-jdk"
# sudo add-apt-repository -y ppa:linuxuprising/java && sudo apt update && sudo apt install -y oracle-java11-installer oracle-java11-set-default
