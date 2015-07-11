#!/bin/bash

youtube-dl $1 -f best

mkdir tmp-ffmpeg-folder
mkdir tmp-output-folder

ffmpeg -threads 4 -i *.mp4 -vf fps=1 tmp-ffmpeg-folder/out%05d.png

python split_analysis.py tmp-ffmpeg-folder tmp-output-folder > script_for_copying.sh

sh script_for_copying.sh

pngquant 256 --speed=1 tmp-output-folder/*.png
convert tmp-output-folder/*-fs8.png -trim slide.pdf

#rm -R tmp-ffmpeg-folder
#rm -R tmp-output-folder
#rm script_for_copying.sh
#rm *.mp4
