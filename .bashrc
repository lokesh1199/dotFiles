#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '


# # ex - archive extractor
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# Shell options
shopt -s autocd


# Flutter
export PATH=$PATH:~/AndroidDev/flutter/bin
export PATH=$PATH:~/AndroidDev/cmdline-tools/latest/bin
export CHROME_EXECUTABLE='/usr/bin/brave'

# Miscellaneous
export EDITOR='vim'
alias nap='shutdown now'
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"    # for ssh agent
alias vi='vim'
alias yta="youtube-dl --extract-audio --audio-format best "

# Scripts
export PATH=~/opt/bin:$PATH

# Aliases for python virtual env
alias py="~/env/bin/python3"
alias py-pip="~/env/bin/pip"

# Dotfiles bare repo
alias dotconfig='/usr/bin/git --git-dir=$HOME/Projects/Public/dotfiles --work-tree=$HOME'

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'
alias l='ls --color=auto'
alias ll='ls -lh --color=auto'
alias la='ls -alh --color=auto'

# Adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -h'                      # human-readable sizes

# Functions
# Backup
backup() {
    cp $1 $1.bak
}

# Pyzen
pyzen() {
    zen_strings=(    
        "Beautiful is better than ugly."
        "Explicit is better than implicit."
        "Simple is better than complex."
        "Complex is better than complicated."
        "Flat is better than nested."
        "Sparse is better than dense."
        "Readability counts."
        "Special cases aren't special enough to break the rules."
        "Although practicality beats purity."
        "Errors should never pass silently."
        "Unless explicitly silenced."
        "In the face of ambiguity, refuse the temptation to guess."
        "There should be one-- and preferably only one --obvious way to do it."
        "Although that way may not be obvious at first unless you're Dutch."
        "Now is better than never."
        "Although never is often better than *right* now."
        "If the implementation is hard to explain, it's a bad idea."
        "If the implementation is easy to explain, it may be a good idea."
        "Namespaces are one honking great idea -- let's do more of those!"
    );
    
    length=${#zen_strings[@]}
    index=$(($RANDOM%$length))
    clear
    echo ${zen_strings[$index]} | cowsay -f small
}

# Startup
pyzen
