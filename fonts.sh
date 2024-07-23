#!/bin/bash

cd /tmp

wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/CascadiaMono.zip

mkdir -p CascadiaMono

unzip -d ./CascadiaMono CascadiaMono.zip

sudo mv CascadiaMono /usr/share/fonts

rm -rf CascadiaMono CascadiaMono.zip


wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/CascadiaCode.zip

mkdir -p CascadiaCode

unzip -d ./CascadiaCode CascadiaCode.zip

sudo mv CascadiaCode /usr/share/fonts

rm -rf CascadiaCode CascadiaCode.zip

echo "done"