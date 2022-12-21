# (__module__/api) <pre-trained>
"""
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<pre.py is __module__/api of lottGPT>
""" 
from core import pre_ball
from core import pre_max
from core import pre_keno
from core import pre_bingo

def pandas(key):
    if key in ["mega","power"]: pre_ball.pandas(key)
    if key in ["plus","pro"]: pre_max.pandas(key)
    if key == "keno": pre_keno.pandas(key)
    if key == "bingo": pre_bingo.pandas(key)