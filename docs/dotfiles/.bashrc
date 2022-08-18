export TERM=xterm-color
export GREP_OPTIONS='--color=auto' GREP_COLOR='1;32'
export CLICOLOR=1

# ls colors
# 1. directory
# 2. symbolic link
# 3. socket
# 4. pipe
# 5. executable
# 6. block special
# 7. character special
# 8. executable with setuid bit set
# 9. executable with setgid bit set
# 10. directory writable to others, with sticky bit
# 11. directory writable to others, without sticky
export LSCOLORS=CxFxCxDxBxegedabagaced

# prompt setting
export PS1="\e[0;32m[\u@\h \W]\$ \e[m "

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/sungj4/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/sungj4/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/sungj4/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/sungj4/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

#
if ! df | awk '{print $9}' | grep -Ex "/mnt/D1"; then
    sshfs -o allow_other sungj4@sungj4-server:/mnt/D1 /mnt/D1
fi


# prompt setting
#export PS1="\e[0;32m[\u@\h \W]\$ \e[m "

# Alias
alias ..='cd ..'
alias ll='ls -alF'
alias gdm3='conda activate gdm3'
alias acap='conda activate acap'
alias jmsung='conda activate jmsung'
alias smb='conda activate smb'
alias sandalo='conda activate sandalo'
alias simc2='ssh -XY simc2'
alias sungj4-server='ssh -XY sungj4-server'
alias sungj4-sim96='ssh -XY sungj4-sim96'
alias sungj4-deb9='ssh -XY sungj4-deb9'
alias gpristine='git reset --hard && git clean -dfx'
alias build='git reset --hard && git clean -dfx; python setup.py develop'
alias htop='htop --sort-key PERCENT_CPU'
