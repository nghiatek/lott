# (__module__/snippet) <transformer_bingo> 
"""transformer_bingo
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<tpu_bingo.py is __module__ of lottGPT //__spec__ of tpu.py>

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
    # print(f"== <tpu_bingo.load_file> \n>> df_in \n{df}")

    # /bingo/
    ## suffix ## del_[n,k]
    df = df.drop(columns=["n","k"])

    ## to_list /[list-2d]/
    ls_b1 = df["b1"].values.tolist()
    ls_b2 = df["b2"].values.tolist()
    ls_b3 = df["b3"].values.tolist()
    ls = [ls_b1,ls_b2,ls_b3]
    # print(f">> ls/[list-2d] = {ls}")

    # /out/ls/[list-2d]/[b1=[0,1],b2=[1,2],b3=[2,3]]
    return ls

def counter_most_common(key):
    # load_file -> ls/[list-2d]
    ls = load_file(key)

    # max/plus/pro/bingo
    # counter
    from collections import Counter
    ## read_list /ls/[list-2d]/ //[[b1],[b2],[b3]]
    counter_b1 = Counter(ls[0])
    counter_b2 = Counter(ls[1])
    counter_b3 = Counter(ls[2])
    ## get_most_common /1-item/
    most_common_b1 = counter_b1.most_common(1)
    most_common_b2 = counter_b2.most_common(1)
    most_common_b3 = counter_b3.most_common(1)
    ## get_item_in_[(item,count)] /new-list = predict-num
    predict_num = [most_common_b1[0][0],most_common_b2[0][0],most_common_b3[0][0]]
    print(f">> predict_num = {predict_num}")

    # /out/[predict_num]/list-1d
    # return predict_num

    # import pandas as pd
    # [predict_num]_to_df -> df_predict //bonus: add_header
    df_predict = pd.DataFrame([predict_num],columns=["b1","b2","b3"])
    print(f">> df_out \n{df_predict}")

    # file_out /{key}__predict.csv
    file_out = filepath + f"{filename}__predict.csv"
    df_predict.to_csv(file_out,index=False)
    print(f">> file_out = {file_out}")