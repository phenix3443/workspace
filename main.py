# -*- coding:utf-8 -*-


devtools = {
    "apt-pre": ["add-apt-repository ppa:zeal-developers/ppa"],
    "common": ["zssh", "sshfs", "tmux", "curl", "zeal", "git"],
    "apt": [],
    "yum": [],
    "brew": [],
}

program = {
    "bash": {
        "common": ["bash-completion"],
        "special": ["npm i -g bash-language-server"],
    },
    "cxx": {
        "common": [
            "cppcheck",
            "clang",
            "clang-format",
            "cmake",
            "build-essential",
            "automake",
            "autoconf",
            "libtool",
            "gcc",
        ]
    },
    "lua": {
        "common": ["lua", "luarocks"],
        "PM": [
            "luacheck",
            "lanes",
            "checks",
            "Formatter",
            "ldoc",
            "lua-discount",
            "lunamark",
            "lua-cjson",
            "penlight",
        ],
        "speical": [],
    },
    "python3": {
        "common": ["python3", "python3-pip"],
        "PM": ["pipenv", "ipython", "yapf", "pylint", "black"],
    },
    "golang": {
        "common": ["golang"],
        "PM": [],
        "specail": ["GO111MODULE=on go get golang.org/x/tools/gopls@latest"],
    },
    "js": {"common": ["npm"]},
    "markdown": {
        "common": ["markdown"],
        "special": [
            "npm --registry https://registry.npm.taobao.org install -g livedown"
        ],
    },
}

applications = {
    "apt-pre": [
        "curl https://build.opensuse.org/projects/home:manuelschneid3r/public_key | sudo apt-key add -",
        "sudo sh -c \"echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list\"",
    ],
    "common": [
        "shutter",
        "shadowsocks-libev",
        "proxychains4",
        "albert",
        "alacarte",
        "aria2",
        "chromium-browser",
        "okular",
        "smplayer",
        "silversearcher-ag",
    ],
    "apt": [],
    "yum": [],
    "brew": [],
}


def main():
    pass


if __name__ == "__main__":
    main()
