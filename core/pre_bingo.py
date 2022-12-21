# (__module__/snippet) <pre-trained_bingo> 
"""pre-trained_keno
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<pre_bingo.py is __module__ of lottGPT //__spec__ of pre.py>

feature
-------
- stringProcess /accessor/
- frameProcess  /reshape/
"""
# config
filepath = "./data/"

# /bingo/
def pandas(key):
    import pandas as pd
    # read_csv
    # file_in /__{key}.csv
    global filename
    filename = key
    file = filepath + f"__{filename}.csv"
    # case: table_has_header /ball/mega/power/keno/bingo/
    df = pd.read_csv(file)
    # print(f"== <pre_bingo.pandas> \n>> df_in \n{df}")

    # prefix /stringProcess/
    df = df.rename(columns={"Ngày /Kỳ":"n","Kết quả":"boso"})
    ## del_[Tổng,Lớn/Nhỏ/Hòa] /drop/
    df = df.drop(columns=["Tổng","Lớn/Nhỏ/Hòa"])
    ## insert_[k]
    df.insert(1,"k","")
    ## [k] = [n].clear_string: 17/12/20222# -> pat = "\d+/\d+/\d+#"
    df["k"] = df["n"].str.replace("\d+/\d+/\d+#","",regex=True)
    ## [n] = [n].clear_string: #0123456 -> pat = "#\d+" 
    df["n"] = df["n"].str.replace("#\d+","",regex=True)
    # print(f">> df_prefixed \n{df}")

    # reshape /frameProcess/
    ## slice_[boso] -> [b1,b2,b3] //new_table = slice_table
    # slice_table = []
    # for item in df["boso"].map(str):
        # /option/for-learn/funny/ same/pre_bingo/tpu_max/
        # new_row = []
        # for i in range(0,3,1):
            # new_cell = item[i:i+1]
            # new_row.append(new_cell)
        # /option/shorthand/
        # new_row = [item[0],item[1],item[-1]]
        # slice_table.append(new_row)
        # /option/shorthand
        # slice_table.append([item[0],item[1],item[-1]])
    ## shorthand/for
    slice_table = [[item[0],item[1],item[-1]] for item in df["boso"].map(str)]
    # print(f">> slice_table \n{slice_table}")

    ## [slice_table]_to_df //bonus: add_header
    df_slice_table = pd.DataFrame(slice_table,columns=["b1","b2","b3"])
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