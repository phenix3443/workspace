echo "install 常用 python 库"

mkdir ~/.config/pip

echo "[global]
index-url=https://mirrors.aliyun.com/pypi/simple
" > ~/.config/pip/pip.conf

pip3 install --user \
     pipenv \
     ipython \
     yapf \
     pylint \
     black \
     cmake-language-server \
     cmake_format \
     pygments
