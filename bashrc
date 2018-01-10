# --------------------------------- Auto generated code -----------------------------------#
# Git folder status on terminal
# Terminal Customization
RS="\[\033[0m\]"    # color reset
get_git_branch()
{
	branch=$(git branch 2>/dev/null | sed -n "s/* \(.*\)/\1/p")
	if [ ! $branch == "" ]
	then
		printf "\033[0m <|\e[33m\e[1m$branch\033[0m|> "
	else
		echo ""
	fi
}

USERNAME="\[\033[1;32m\]\u"
AT="$RS@"
HOSTNAME="\[\033[1;35m\]\h"
SEMICOLON="$RS:"
CWD="\[\033[1;36m\]\W"
DOLLER="$RS$ "
PS1="${debian_chroot:+($debian_chroot)}[$USERNAME$AT$HOSTNAME$RS]$SEMICOLON$CWD\`get_git_branch\`$DOLLER"

# Timestamp on terminal start
date "+%d %B %r" | toilet -f term -F border --gay