# (__module__/snippet) <transformer_keno> 
"""transformer_keno
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<tpu_keno.py is __module__ of lottGPT //__spec__ of tpu.py>

feature
-------
- counter_most_common
- numpy_random
"""
# config
filepath = "./data/"
import pandas as pd

def load_file(key):
    # import pandas as pd
    # file_in /{key}.csv
    global filename
    filename = key
    file = filepath + f"{filename}.csv"
    df = pd.read_csv(file)
    print(f"== <tpu_keno.load_file> \n>> df_in \n{df}")

    # ball/mega/power/keno
    ## suffix ## del_[n,k]
    df = df.drop(columns=["n","k"])
    ## to_list /[list-2d]/
    ls = df.values.tolist()

    # /out/ls/[list-2d]/[k1=[1,2,..],..,k8=[1,2,..]]
    return ls

def counter_most_common(key):
    # load_file -> ls/[list-2d]
    ls = load_file(key)

    # ball/mega/power/keno
    # prefix
    ## [list-2d]_to_[list-1d] /flatten/ //[[0,1,..],[1,2,..],..] -> [0,1,..,1,2,..,..]
    ## new-list = lst
    # lst = []
    # for sublist in ls:
        # for item in sublist:
            # lst.append(item)
    ## shorthand/nested-for
    lst = [item for sublist in ls for item in sublist]

    # counter
    from collections import Counter
    ## read_list /lst/[list-1d] //[0,1,..]
    counter = Counter(lst)
    ## get_most_common /6-item/
    most_common = counter.most_common(6)
    ## get_item_in_[(item,count)] /new-list = predict-num
    # predict_num = []
    # for item,count in most_common:
    #     predict_num.append(item)
    ## shorthand/for
    predict_num = [item for item,count in most_common]
    predict_num.sort()
    print(f">> predict_num = {predict_num}")

    # /out/[predict_num]/list-1d
    # return predict_num

    # import pandas as pd
    # [predict_num]_to_df -> df_predict //bonus: add_header
    df_predict = pd.DataFrame([predict_num],columns=["b1","b2","b3","b4","b5","b6"])
    print(f">> df_out \n{df_predict}")

    # file_out /{key}__predict.csv
    file_out = filepath + f"{filename}__predict.csv"
    df_predict.to_csv(file_out,index=False)
    print(f">> file_out = {file_out}")