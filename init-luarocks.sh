luarocks install --local luacheck # 代码检查
mkdir -p ~/.config/luacheck/
ln dotfiles/_config/luacheck/.luacheckrc ~/.config/luacheck/.luacheckrc
luarocks install lanes
luarocks install checks # Formatter 依赖
luarocks install Formatter # 代码格式化 for lua5.1
luarocks install lcf # 代码格式化 for lua5.3
luarocks install ldoc
luarocks install lua-discount # for ldoc
luarocks install lunamark     # for ldoc
luarocks install --server=http://luarocks.org/dev lua-lsp

luarocks install lua-cjson
luarocks install penlight
