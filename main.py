# -*- coding:utf-8 -*-

import logging

AptPPA = [
    # zeal
    "add-apt-repository ppa:zeal-developers/ppa",
    "curl https://build.opensuse.org/projects/home:manuelschneid3r/public_key | sudo apt-key add -",
    "sudo sh -c \"echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list\"",
    # apt-fast
    "add-apt-repository ppa:apt-fast/stable",
    "apt update",  # 始终放在最后
]

APT = {
    "app": [
        "alacarte",
        "albert",
        "apt-fast",  # 要选择apt-get，选择apt好像有点问题
        "aria2",
        "bash-completion",
        "curl",
        "emacs",
        "fish",
        "foxitreader",
        "google-chrome-stable",
        "netease-cloud-music",
        "okular",
        "proxychains4",
        "shadowsocks-libev",
        "shutter",
        "silversearcher-ag",
        "smartgit",
        "smplayer",
        "sogoupinyin",
        "sshfs",
        "sublime-text",
        "synergy",
        "tmux",
        "zeal",
        "zssh",
        "wine-development",
    ],
    "cxx": [
        "cppcheck",
        "clang",
        "clang-format",
        "cmake",
        "build-essential",
        "automake",
        "autoconf",
        "libtool",
        "gcc",
    ],
    "lua": ["lua5.1 lua5.3 luarocks"],
    "python": ["python3 python3-pip"],
    "golang": ["golang"],
    "js": ["npm yarn"],
    "markdown": ["markdown"],
    "git": ["git git-flow"],
    "mysql": ["mysql-server mysql-client mysql-utilities mysql-workbench"],
}

YUM = {"app": [], "cxx": [], "lua": [], "python": [], "golang": [], "js": []}

Brew = {
    "app": [
        "zssh",
        "tmux",
        "the_silver_searcher",
        "proxychains-ng",
        "sshfs",
        "markdown",
        "yarn",
        "mysql mysql-client",
    ],
    "bash": ["bash-completion"],
    "cxx": [],
    "lua": ["lua", "luarocks"],
    "python": ["python3"],
    "golang": ["golang"],
    "js": ["npm", "node"],
    "git": ["git", "git-flow"],
}

BrewCask = [
    "dash",
    "shadowsocksx-ng",
    "chromium",
    "iina",
    "emacs",
    "beyond-compare",
    "mysqlworkbench",
    "proxifier",
]

NPM = [
    "livedown",
    "lua-fmt",
    "typescript",
    "bash-language-server",
    "typescript-language-server",
    "vscode-json-languageserver",
    "vscode-css-languageserver-bin",
    "dockerfile-language-server-nodejs",
    "vscode-html-languageserver-bin",
    "vue-language-server",
    "yaml-language-server",
]

YARN = ["prettier"]

LuaRocks = [
    "luacheck",
    "lanes",
    "checks",
    "Formatter",
    "ldoc",
    "lua-discount",
    "lunamark",
    "lua-cjson",
    "penlight",
]


Pip = [
    "pipenv",
    "ipython",
    "yapf",
    "pylint",
    "black",
    "cmake-language-server",
    "cmake_format",
    "pygments",
]

GO = [
    "GO111MODULE=on go get golang.org/x/tools/gopls@latest",
    "GO111MODULE=on go get mvdan.cc/sh/v3/cmd/shfmt",
    "go get github.com/jessfraz/dockfmt",
]

Linux = [
    (
        "mkdir -p ~/github && cd ~/github",
        " && git clone git@github.com:bobthecow/git-flow-completion.git",
        " && cp git-flow-completion/git-flow-completion.bash /usr/local/etc/bash_completion.d/",
    )  # 安装git-flow-completion
]

Shell = [
    # install bash completion
    """echo [[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] \&\& . "/usr/local/etc/profile.d/bash_completion.sh"' >> ~/.bash_profile""",
    # 安装git-flow-completion
    (
        "mkdir -p ~/github && cd ~/github",
        " && git clone git@github.com:bobthecow/git-flow-completion.git",
        " && cp git-flow-completion/git-flow-completion.bash /usr/local/etc/bash_completion.d/",
    ),
    # 设置bcompare
    (
        "git config --global diff.tool bc3",
        "&& git config --global merge.tool bc3",
        "&& git config --global mergetool.bc3 trustExitCode true",
        "&& git config --global mergetool.keepBackup false",
    ),
    # docker
    ("curl -fsSL https://get.docker.com -o get-docker.sh ", "sudo sh get-docker.sh"),
]


def main():
    logging.basicConfig(level=logging.DEBUG)

    for s in AptPPA:
        logging.debug(s)

    for (k, v) in APT.items():
        if v:
            logging.debug("apt install -y {}".format(" ".join(v)))

    for (k, v) in YUM.items():
        if v:
            logging.debug("yum install -y {}".format(" ".join(v)))

    for (k, v) in Brew.items():
        if v:
            logging.debug("brew install {}".format(" ".join(v)))

    if BrewCask:
        logging.debug("brew cask install {}".format(" ".join(BrewCask)))

    if NPM:
        logging.debug(
            "npm --registry https://registry.npm.taobao.org  install -g {}".format(
                " ".join(NPM)
            )
        )

    if YARN:
        logging.debug("yarn add  --dev --exact  {}".format(" ".join(NPM)))

    if LuaRocks:
        logging.debug("luarocks install --local {}".format(" ".join(LuaRocks)))

    if Pip:
        logging.debug("pip3 install --user {}".format(" ".join(Pip)))

    if GO:
        logging.debug(" ".join(GO))


if __name__ == "__main__":
    main()
