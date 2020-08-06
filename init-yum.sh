
echo "common"
sudo yum install -y redhat-lsb-core

echo "EPEL"
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm


echo "for shell"
sudo yum install -y bash-completion bash-completion-extras
sudo yum install -y gcc gcc-c++ automake autoconf libtool make

echo "for emacs"
brew install global
brew install --HEAD universal-ctags/universal-ctags/universal-ctags
