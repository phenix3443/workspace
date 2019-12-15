# -*- coding:utf-8 -*-
PREINSTALL = {
    "apt" :{
    "zeal":["add-apt-repository ppa:zeal-developers/ppa"],
    "albert":["curl https://build.opensuse.org/projects/home:manuelschneid3r/public_key | sudo apt-key add -",
"sudo sh -c \"echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list\""]     
}
   
}


devtools = {
    "common":[
              "zssh",
              "sshfs",
              "tmux",
                            "curl",
              "zeal",
              "bash-completion",
              "build-essential",
              "automake",
              "autoconf",
              "libtool",
              "gcc",
              "cmake",
              # cxx

              
]
}

program_language = {
    "cxx":[
                         "cppcheck",
              "clang",
              "clang-format",
           
],
    "lua":[
           "lua", "luarocks",
]
    }

applications = {
    "common":[
              "shutter",
              "shadowsocks-libev",
              "proxychains4",
              "albert",
              "alacarte",
              "aria2",
              "chromium-browser",
              "okular",
              "smplayer",
            
              ],
    "apt":[]
}


POSTINSTALL= {
    "common":{
        "shadowsocks":["./do-config.sh local"],
        "proxychains4":["mkdir ~/.proxychains && cp dotfiles/_proxychains/proxychains.conf ~/.proxychains"],
        "python3":["pip3 install black"]
        
        },
        

    "apt":{

}
}
def main():
    pass

if __name__ == '__main__':
    main()
