# (__module__/api) <transformer>
"""
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<tpu.py is __module__/api of lottGPT>
""" 
from core import tpu_ball
from core import tpu_max
from core import tpu_keno
from core import tpu_bingo

def counter_most_common(key):
    if key in ["mega","power"]: tpu_ball.counter_most_common(key)
    if key in ["plus","pro"]: tpu_max.counter_most_common(key)
    if key == "keno": tpu_keno.counter_most_common(key)
    if key == "bingo": tpu_bingo.counter_most_common(key)