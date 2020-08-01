echo "export GO111MODULE=on" >> ~/.profile && \
echo "export GOPROXY=https://goproxy.cn" >> ~/.profile && \
source ~/.profile && \
GO111MODULE=on go get golang.org/x/tools/gopls@latest && \
GO111MODULE=on go get mvdan.cc/sh/v3/cmd/shfmt && \
    go get github.com/jessfraz/dockfmt
