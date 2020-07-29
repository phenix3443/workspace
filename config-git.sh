echo "config git"
git config --global user.name phenix3443
git config --global user.email phenix3443@gmail.com


git config --global diff.tool bc3
git config --global merge.tool bc3
git config --global mergetool.bc3 trustExitCode true
git config --global mergetool.keepBackup false

echo "config git-flow"
git clone git@github.com:bobthecow/git-flow-completion.git && \
sudo cp git-flow-completion/git-flow-completion.bash /etc/bash_completion.d && \
rm -fr git-flow-completion
