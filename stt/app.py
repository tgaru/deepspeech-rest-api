from os import getenv

from concurrent.futures import ThreadPoolExecutor
from sanic import Sanic
from sanic.response import json
from sanic.exceptions import InvalidUsage

from .engine import SpeechToTextEngine


MAX_ENGINE_WORKERS = int(getenv('MAX_ENGINE_WORKERS', 2))
LANGUAGES_LIST = ['en', 'it', 'zh-CN']

engine = SpeechToTextEngine()
executor = ThreadPoolExecutor(max_workers=MAX_ENGINE_WORKERS)

app = Sanic()


def error(message):
    return json({
        'status': 'error',
        'message': message
    })

def success(text, time):
    return json({
        'status': 'success',
        'text': text,
        'time': time
    })

@app.route('/api/v1/stt', methods=['POST'])
async def stt(request):
    speech = request.files.get('speech')
    if not speech: return error('The "speech" parameter is missing.')

    lang = request.form.get('lang')
    if not lang: return error('The "lang" parameter is missing.')
    if lang not in LANGUAGES_LIST: return error('The "lang" parameter is not valid. Supported: '+(LANGUAGES_LIST.join(', '))+'.')

    from time import perf_counter
    inference_start = perf_counter()
    engine.setLang(lang)
    text = await app.loop.run_in_executor(executor, lambda: engine.run(speech.body))
    inference_end = perf_counter() - inference_start
    return success(text, inference_end)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
