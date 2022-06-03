#!/bin/bash

video_input = ""

while IFS= read -r line; do
    if  [[ $line == test* ]] ;
    then
        video_input=${line:4}
        echo $video_input
    fi
    if [[ $line == cut* ]] ;
    then
        comeco_corte=${line:3:8}
        fim_corte=${line:12:8}
        titulo_corte=${line:21}
        echo $comeco_corte
        echo $fim_corte
        echo $titulo_corte
        ffmpeg -ss "${comeco_corte}" -to "${fim_corte}" -i "${video_input}".mp4 -c copy "${titulo_corte}".mp4
        echo "corte gerado!"
    fi
done < videocuts.txt

