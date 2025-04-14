#!/bin/bash

mkdir -p /home/youssef/Documents/reports/ls
mkdir -p /home/youssef/Documents/reports/tree

#######################
tree -h --du /mnt/2tb_ar/Mediaa > /home/youssef/Documents/reports/tree/ar.txt
tree -h --du /mnt/4tb_en/mediaa2 > /home/youssef/Documents/reports/tree/en.txt
tree -h --du /mnt/2tb_mix/media > /home/youssef/Documents/reports/tree/mix.txt


###################
ls /mnt/2tb_ar/Mediaa/2\ -\ مسلسلات > /home/youssef/Documents/reports/ls/tv-ar.txt
tree -h --du /mnt/2tb_ar/Mediaa/2\ -\ مسلسلات > /home/youssef/Documents/reports/tree/tv-ar.txt

#####################
ls /mnt/4tb_en/mediaa2/1\ -\ افلام > /home/youssef/Documents/reports/ls/movies-ar.txt
tree -h --du /mnt/4tb_en/mediaa2/1\ -\ افلام > /home/youssef/Documents/reports/tree/movies-ar.txt

##################
ls /mnt/2tb_ar/Mediaa/3\ -\ مسرحيات > /home/youssef/Documents/reports/ls/tv-m-ar.txt
tree -h --du /mnt/2tb_ar/Mediaa/3\ -\ مسرحيات > /home/youssef/Documents/reports/tree/tv-m-ar.txt

####################
ls /mnt/4tb_en/mediaa2/6\ -\ tv\ show > /home/youssef/Documents/reports/ls/tv-en.txt
tree -h --du /mnt/4tb_en/mediaa2/6\ -\ tv\ show > /home/youssef/Documents/reports/tree/tv-en.txt

#########################
ls /mnt/4tb_en/mediaa2/8\ -\ movies > /home/youssef/Documents/reports/ls/movies-en.txt
tree -h --du /mnt/4tb_en/mediaa2/8\ -\ movies > /home/youssef/Documents/reports/tree/movies-en.txt

######################
ls /mnt/2tb_mix/media/4\ -\ anime > /home/youssef/Documents/reports/ls/anime.txt
tree -h --du /mnt/2tb_mix/media/4\ -\ anime > /home/youssef/Documents/reports/tree/anime.txt

############
ls /mnt/2tb_mix/media/5\ -\ افلام\ كرتون > /home/youssef/Documents/reports/ls/cartoon-movies.txt
tree -h --du /mnt/2tb_mix/media/5\ -\ افلام\ كرتون > /home/youssef/Documents/reports/tree/cartoon-movies.txt

###############
ls /mnt/2tb_mix/media/7\ -\ anime\ movies > /home/youssef/Documents/reports/ls/anime-movies.txt
tree -h --du /mnt/2tb_mix/media/7\ -\ anime\ movies > /home/youssef/Documents/reports/tree/anime-movies.txt
