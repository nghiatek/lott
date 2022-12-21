# (__module__/snippet) <pre-trained_ball> 
"""pre-trained_ball
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<pre_ball.py is __module__ of lottGPT //__spec__ of pre.py>

feature
-------
- stringProcess /accessor/
- frameProcess  /reshape/
"""
# config
filepath = "./data/"

# /ball/mega/power/
def pandas(key):
    import pandas as pd
    # read_csv 
    # file_in /__{key}.csv
    global filename
    filename = key
    file = filepath + f"__{filename}.csv"
    # case: table_has_header /ball/mega/power/keno/bingo/
    df = pd.read_csv(file)
    # print(f"== <pre_ball.pandas> \n>> df_in \n{df}")

    # prefix /stringProcess/
    df = df.rename(columns={"Ngày":"n","Kỳ":"k","Bộ số":"boso"})
    if key == "mega":
        df["boso"] = "0" + df["boso"].map(str)
        df["boso"] = df["boso"].str[-12:]
    if key == "power":
        # case: df[boso]_has_space /123456.. |07/ -> pattern = "\s|"
        # case: df[boso]_not_space /123456..|07/ -> pattern = "\|"
        df["boso"] = df["boso"].str.replace("\|","",regex=True)
    # print(f">> df_prefixed \n{df}")

    # reshape /frameProcess/
    ## slice_[boso] -> [b1,b2,b3,b4,b5,b6,b7] //new_table = slice_table
    # slice_table = []
    # for item in df["boso"]:
        # new_row = []
        ## slice_item
        ## item = 012456.. -> cell = [0/1,2/3,4/5]  -> [i]ndex/[i]ndices/position = 0,2,4,..
        ## i in range(start=0,stop=len(item),step=2) -> i = 0,2,4,..
        # for i in range(0,len(item),2):
            ## get_new_cell = slice_item[start=i : stop=i+2]
            # new_cell = item[i:i+2]
            # new_row.append(new_cell)
        # slice_table.append(new_row)
    ## shorthand/nested-for/complex/
    slice_table = [[item[i:i+2] for i in range(0,len(item),2)] for item in df["boso"]]
    # print(f">> slice_table = {slice_table}")

    ## [slice_table]_to_df //bonus: add_header
    if key == "mega" : df_slice_table = pd.DataFrame(slice_table, columns=["b1","b2","b3","b4","b5","b6"])
    if key == "power": df_slice_table = pd.DataFrame(slice_table, columns=["b1","b2","b3","b4","b5","b6","b7"])

    ## join(df,df_slice_table) /concat/hstack/join_column/axis=1
    df = pd.concat([df,df_slice_table],axis=1)
    ## del_[boso] /drop/
    df = df.drop(columns=["boso"])
    ## convert_[n]_to_datetime
    df["n"] = pd.to_datetime(df["n"],dayfirst=True)
    ## sort_df_by_[n] /sort_values/ //newest_on_bottom
    df = df.sort_values(by=["n"])
    # print(f">> df_out \n{df}")

    # file_out /{key}.csv
    file_out = filepath + f"{filename}.csv"
    df.to_csv(file_out,index=False)
    # print(f">> file_out = {file_out}")