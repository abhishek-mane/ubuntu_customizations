# COMMAND

uuidgen

dconf write /org/gnome/terminal/legacy/profiles:/:9c8a72fb-6bdd-4c6e-8b69-b41b1217827d/visible-name "'Custom Profile 1'"

dconf load /org/gnome/terminal/legacy/profiles:/:9c8a72fb-6bdd-4c6e-8b69-b41b1217827d/ < material-theme-profile.dconf

dconf


https://askubuntu.com/questions/270469/how-can-i-create-a-new-profile-for-gnome-terminal-via-command-line