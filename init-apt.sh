#! /bin/bash
# author:phenix3443@gmail.com
# desc: 初始化系统环境

PROJECT_DIR=$(cd $(dirname $0);pwd)

echo "creat github dir"
GITHUB_PATH="~/github/"
mkdir ${GITHUB_PATH}

echo "create gitlab dir"
GITLAB_PATH="~/gitlab/"
mkdir ${GITLAB_PATH}

echo "install softwares"
sudo apt update && \
    apt upgrade -y && \
    apt install -y shutter alacarte chromium-browser smplay wine-development \
        zssh sshfs tmux aria2 curl shadowsocks-libev proxychains4


echo "install zeal" && \
    sudo add-apt-repository ppa:zeal-developers/ppa && \
    sudo apt install -y zeal

# https://software.opensuse.org/download.html?project=home:manuelschneid3r&package=albert
echo "install albert" && \
    echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' | sudo tee /etc/apt/sources.list.d/home:manuelschneid3r.list && \
    curl -fsSL https://download.opensuse.org/repositories/home:manuelschneid3r/xUbuntu_18.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home:manuelschneid3r.gpg > /dev/null && \
    sudo apt update && sudo apt install albert


# https://www.sublimetext.com/docs/3/linux_repositories.html
echo "install sublime" && \
    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add - && \
    sudo apt-get install apt-transport-https && \
    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list && \
    sudo apt-get update && apt-get install sublime-text



echo "config develop enviroments"
sudo apt install -y build-essential automake autoconf libtool gcc cmake bash-completion powerline fonts-powerline python3-pygit2 git git-flow silversearcher-ag python-pygments


echo "common IDE"
sudo apt install -y global

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
sudo apt install -y markdown

echo "install php"
apt install php phpmd php-codesniffer

echo "config open-jdk"
# apt install -y default-jdk

echo "config oracle-jdk"
# add-apt-repository ppa:linuxuprising/java
# apt update
# apt install -y oracle-java11-installer oracle-java11-set-default



echo "install ctags for global"
ctags for gtags
cd ${GITHUB_PATH}
git clone git@github.com:universal-ctags/ctags.git
cd ctags
./autogen.sh
./configure && make -j4 && make install && cd -
cd ${PROJECT_DIR}

echo "install pgFormatter for sqlformater"
cd ${GITHUB_PATH}
git clone git@github.com:darold/pgFormatter.git && \
    cd pgFormatter && \
    perl Makefile.PL && make && sudo make install && \
    cd ${PROJECT_DIR}




echo "config proxychains4"
mkdir ~/.proxychains
cp dotfiles/_proxychains/proxychains.conf ~/.proxychains

echo "config powerline"
mkdir ~/.config/powerline
ln dotfiles/_config/powerline/config.json ~/.config/powerline/config.json
