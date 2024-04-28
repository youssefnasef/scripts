sudo apt install zsh curl wget unzip

wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip

unzip Hack.zip 


sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
### Set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.
echo 'Set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.'
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions

## Add it to FPATH in your .zshrc by adding the following line before source "$ZSH/oh-my-zsh.sh":
echo 'Add it to FPATH in your .zshrc by adding the following line before source "$ZSH/oh-my-zsh.sh":'
### fpath+=${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions/src
echo 'fpath+=${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions/src'
# git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
# echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
# source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

echo 'Activate the plugin in ~/.zshrc

plugins=( [plugins...] zsh-syntax-highlighting)'

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

echo 'Add the plugin to the list of plugins for Oh My Zsh to load (inside ~/.zshrc) 
plugins=( 
    # other plugins...
    zsh-autosuggestions
)'