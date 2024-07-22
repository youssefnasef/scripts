#!/bin/bash

cd /tmp

wget https://github.com/ful1e5/Bibata_Cursor/releases/download/v2.0.7/Bibata-Modern-Amber.tar.xz

tar -xvf Bibata-Modern-Amber.tar.xz

rm Bibata-Modern-Amber.tar.xz

sudo mv Bibata-* /usr/share/icons/

echo "done"