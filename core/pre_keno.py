# (__module__/snippet) <pre-trained_keno> 
"""pre-trained_keno
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<pre_keno.py is __module__ of lottGPT //__spec__ of pre.py>

feature
-------
- stringProcess /accessor/
- frameProcess  /reshape/
"""
# config
filepath = "./data/"

# /keno/
def pandas(key):
    import pandas as pd
    # read_csv
    # file_in /__{key}.csv
    global filename
    filename = key
    file = filepath + f"__{filename}.csv"
    # case: table_has_header /ball/mega/power/keno/bingo/
    df = pd.read_csv(file)
    # print(f"== <pre_keno.pandas> \n>> df_in \n{df}")

    # prefix /stringProcess/
    df = df.rename(columns={"Ngày /Kỳ":"n","Kết quả":"boso"})
    ## del_[Chẵn/Lẻ,Lớn/Nhỏ] /drop/
    df = df.drop(columns=["Chẵn/Lẻ","Lớn/Nhỏ"])
    ## insert_[k]
    df.insert(1,"k","")
    ## [k] = [n].clear_string: 17/12/20222# -> pat = "\d+/\d+/\d+#"
    df["k"] = df["n"].str.replace("\d+/\d+/\d+#","",regex=True)
    ## [n] = [n].clear_string: #0123456 -> pat = "#\d+" 
    df["n"] = df["n"].str.replace("#\d+","",regex=True)
    # print(f">> df_prefixed \n{df}")

    # reshape /frameProcess/
    ## slice_[boso] -> [b1,..,b20] //new_table = slice_table
    slice_table = []
    for item in df["boso"]:
        new_row = []
        # slice_item
        ## item = 012456.. -> cell = [0/1,2/3,4/5]  -> [i]ndex/[i]ndices/position = 0,2,4,..
        ## i in range(start=0,stop=len(item),step=2) -> i = 0,2,4,..
        for i in range(0,len(item),2):
            # get_new_cell = slice_item[start=i : stop=i+2]
            new_row.append(item[i:i+2])
        slice_table.append(new_row)
    ## shorthand/nested-for
    # slice_table = [[item[i:i+2] for item in df["boso"] for i in range(0,len(item),2)]]
    # print(f">> slice_table = {slice_table}")

    ## [slice_table]_to_df //bonus: add_header
    df_slice_table = pd.DataFrame(slice_table,columns=["b1","b2","b3","b4","b5","b6","b7","b8","b9","b10",
        "b11","b12","b13","b14","b15","b16","b17","b18","b19","b20"])
    # print(f">> df_slice_table \n{df_slice_table}")

    ## join(df,df_slice_table) /concat/vstack/join_column/axis=1
    df = pd.concat([df,df_slice_table],axis=1)
    ## del_[boso] /drop/
    df = df.drop(columns=["boso"])
    ## convert_[n]_to_datetime
    df["n"] = pd.to_datetime(df["n"],dayfirst=True)
    ## sort_df_by_[k] /sort_values/ //newest_on_bottom
    df = df.sort_values(by=["k"])
    # print(f">> df_out \n{df}")

    # file_out /{key}.csv
    file_out = filepath + f"{filename}.csv"
    df.to_csv(file_out,index=False)
    # print(f">> file_out = {file_out}")