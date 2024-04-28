wget 'https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip'
sudo apt install zsh curl wget unzip
mkdir /home/youssef/Downloads/Hack -p
unzip Hack.zip -d /home/youssef/Downloads/Hack
sudo cp /home/youssef/Downloads/Hack /usr/share/fonts -r
sudo chsh -s /bin/zsh
echo "change the font of terminal"
echo "logou logou logou logou "
