DeepSpeech REST API
===================

Simple API over Mozilla DeepSpeech voice recognition engine with support for multiple languages.

## Supported languages
- en
- it
- zh-CN

## Endpoints
```
POST /api/v1/stt - Just look at curl command below.
Speech data may be provided in whatever audio format which ffmpeg is able to convert to wav,
so you probably don't have to worry about this at all.

$ curl -X POST -F "speech=@speech.mp3" -F "lang=en" http://127.0.0.1:12367/api/v1/stt 

{
    "status": "success",
    "text": "experience proves this",
    "time":0.9638644850056153
}
```

## Setup

### 0. Checkout repository
`git clone git@github.com:tgaru/deepspeech-rest-api.git`

### 1. Download deepspeech data models
1. Enter `<repository_root>`
2. Run `/bin/sh load_models.sh`

### 2 Running
1. Enter `<repository_root>`
2. Run `docker-compose up`
