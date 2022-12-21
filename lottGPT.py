# (__main__/console) <lottGPT> 
"""lottGPT
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<lottGPT.py is __main__/console>

features
--------
- gen.py <Generative>: connect(url[key]) -> parse(html) -> file_out/__key.html/csv
- pre.py <Pre-trained>
    - pre_ball.py: __spec__ /ball/mega/power/ -> file_out/{key}.csv
    - pre_max.py : __spec__ /max/plus/pro/    -> file_out/{key}.csv
    - pre_keno.py: __spec__ /max/plus/pro/    -> file_out/{key}.csv
- tpu.py <Transformer>
    - tpu_ball.py: __spec__ /ball/mega/power/ -> file_out/{key}__predict.csv
    - tpu_max.py : __spec__ /max/plus/pro/    -> file_out/{key}__predict.csv
    - tpu_keno.py: __spec__ /max/plus/pro/    -> file_out/{key}__predict.csv
"""

def lott(key):
    # <Generative>: connect(url[key]) -> parse(html) -> file_out/__key.html/csv
    from core import gen
    gen.requests(key)
    
    # <Pre-trained>
    from core import pre
    pre.pandas(key)

    # <Transformer>
    from core import tpu
    tpu.counter_most_common(key)

__doc__ = """
Usage
-----
$ lottGPT.py
> Keyword: <mega/power/plus/pro/keno/bingo/all>
<file_out>
"""

# __main__
keylist = ["mega","power","plus","pro","keno","bingo"]
keyword = input("Keyword: ")
if keyword in keylist: lott(keyword)
elif keyword == "all":
    for key in keylist: lott(key)
else: print(__doc__)