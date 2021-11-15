#!/bin/sh

apt install wget

# EN
mkdir models/en/
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.1/deepspeech-0.9.1-models.pbmm -O models/en/output_graph.pbmm

# zh-CN
mkdir models/zh-CN/
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models-zh-CN.pbmm -O models/zh-CN/output_graph.pbmm

# IT
wget https://github.com/MozillaItalia/DeepSpeech-Italian-Model/releases/download/2020.08.07/model_tensorflow_it.tar.xz -O models/it.tar.xz
mkdir models/it/
tar xvf models/it.tar.xz -C models/it/
rm models/it.tar.xz
