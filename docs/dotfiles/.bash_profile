# Update in .bashrc and source it into .bash_profile

if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

test -e "${HOME}/.iterm2_shell_integration.bash" && source "${HOME}/.iterm2_shell_integration.bash"
