# install brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo "creat github dir"
GITHUB_PATH="~/github/"
mkdir ${GITHUB_PATH}

echo "create gitlab dir"
mkdir ${GITLAB_PATH}
GITLAB_PATH="~/gitlab/"

echo "common"
brew install zssh tmux the_silver_searcher sshfs git git-flow

echo "for bash"
brew install bash-completion

echo "for emacs"
brew install the_silver_searcher

echo "for c/cpp"
brew install cppcheck

echo "for lua"
brew install lua5.1 lua5.3 luarocks

echo "for python"
brew install python3

echo "for golang"
brew install golang

echo "for ruby"

echo "for javascript"
brew install yarn npm node

echo "for makrdown"
brew install markdown

echo "for java"

echo "for swift"

echo "for mysql"
brew install mysql mysql-client

echo "for IDE"
brew cask install android-studio dash shadowsocksx-ng chromium iina emacs beyond-compare mysqlworkbench proxifier
