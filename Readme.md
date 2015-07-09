# Pipeline

Download video

  youtube-dl <URL> -f best

Convert to images

  ffmpeg -i <filename> -vf fps=1 out%03d.png
