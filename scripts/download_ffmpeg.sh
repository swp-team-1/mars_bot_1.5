#!/bin/bash

mkdir -p ffmpeg
cd ffmpeg

# Скачиваем FFmpeg (статически скомпилированную сборку)
curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o ffmpeg.tar.xz

# Распаковываем
tar -xf ffmpeg.tar.xz --strip-components=1

# Удаляем архив
rm ffmpeg.tar.xz

echo "FFmpeg загружен в $(pwd)"
