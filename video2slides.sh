#!/bin/bash

youtube-dl $1 -f best

mkdir tmp-ffmpeg-folder
mkdir tmp-output-folder

ffmpeg -threads 6 -i *.mp4 -vf fps=1 tmp-ffmpeg-folder/out%05d.png

echo "Run Python script"
python split_analysis.py tmp-ffmpeg-folder tmp-output-folder > script_for_copying.sh

sh script_for_copying.sh

echo "PNGQuant"
pngquant 256 tmp-output-folder/*.png
echo "Convert to pdf"
convert tmp-output-folder/*-fs8.png -trim slide.pdf

echo "Cleaning up"
rm -R tmp-ffmpeg-folder
rm -R tmp-output-folder
rm script_for_copying.sh
rm *.mp4
