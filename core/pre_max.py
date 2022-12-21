# (__module__/snippet) <pre-trained_max> 
"""pre-trained_max
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<pre_max.py is __module__ of lottGPT //__spec__ of pre.py>

feature
-------
- stringProcess /accessor/
- frameProcess  /reshape/
"""
# config
filepath = "./data/"

# /max/plus/pro/
def pandas(key):
    import pandas as pd
    # read_csv
    # file_in /__{key}.csv
    global filename
    filename = key
    file = filepath + f"__{filename}.csv"
    # case: table_not_header /max/plus/pro/ -> add_header
    df = pd.read_csv(file,header=None,names=["tbody"])
    # print(f"== <pre_max.pandas> \n>> df_in \n{df}")

    # prefix /stringProcess/ 
    ## clear_text ## patten
    ## clear/ascii/: set [letter_char from a to z /lower/upper/ && spec_char "|" /vertical_bar/] -> [a-zA-Z|]
    ## clear/utf-8/: not ^/caret/ in set [number_char from 0 to 9 && spec_char "/" /slash/] -> [^0-9/]
    ## clear repeat: +/plus/ -> [a-zA-Z|][^0-9/]+
    df["tbody"] = df["tbody"].str.replace("[a-zA-Z|][^0-9/]+"," ",regex=True)
    df["tbody"] = df["tbody"].str.strip()
    # print(f">> df_prefixed \n{df}")

    # reshape /frameProcess/
    ## mission 1/3: split_[tbody] -> [n,k,jp,g1,g2,g3] //new_table = split_table
    split_table = []
    for item in df["tbody"]:
        new_row = item.split(" ")
        split_table.append(new_row)
    ## shorthand/for
    # split_table = [[item.split(" ")] for item in df["tbody"]]
    # print(f">> split_table = {split_table}")

    ## [split_table]_to_df //bonus: add_header
    df_split_table = pd.DataFrame(split_table,columns=["k","n","jp","g1","g2","g3"])
    ## move [n] to [0] /insert(pop)/
    df_split_table.insert(0,"n",df_split_table.pop("n"))
    # print(f">> df_split_table \n{df_split_table}")

    ## mission 2/3: join & slice
    ## [df_split_table] -> [df_join_table] //join_[jp,g1,g2,g3] -> [boso] //for: slice_[boso]
    df_join_table = df_split_table.copy()
    ## join_[jp,g1,g2,g3] -> [boso] /cat/
    df_join_table["boso"] = df_join_table["jp"].str.cat(df_join_table[["g1","g2","g3"]])
    ## del_[jp,g1,g2,g3] /drop/
    df_join_table = df_join_table.drop(columns=["jp","g1","g2","g3"])
    # print(f">> df_join_table \n{df_join_table}")

    # slice_[boso] -> [jp-1,jp-2, g1-1,..,g1-4, g2-1,..,g2-6, g3-1,..,g3-8] //new_table = slice_table
    slice_table = []
    for item in df_join_table["boso"]:
        new_row = []
        ## slice_item
        ## [item] = 012345678.. -> cell = [0/12, 3/45, 6/78, ..] -> [i]ndex/[i]ndices/position= 0, 3, 6, ..
        ## [i] in range(start=0,stop=len(item),step=3)
        for i in range(0,len(item),3):
            # get_new_cell = slice_item[start=i:stop=i+3]
            new_cell = item[i:i+3]
            new_row.append(new_cell)
        slice_table.append(new_row)
    ## shorthand/nested-for
    # slice_table = [[item[i:i+3]] for item in df_join_table["boso"] for i in range(0,len(item),3)]
    # print(f">> slice_table = {slice_table}")

    # [slice_table]_to_df //bonus: add_header
    df_slice_table = pd.DataFrame(slice_table,columns=["jp-1","jp-2","g1-1","g1-2","g1-3","g1-4",
    "g2-1","g2-2","g2-3","g2-4","g2-5","g2-6","g3-1","g3-2","g3-3","g3-4","g3-5","g3-6","g3-7","g3-8"])
    # print(f">> df_slice_table \n{df_slice_table}")

    # join(df_join_table,df_slice_table) /concat/hstack/join_column/axis=1/
    df = pd.concat([df_join_table,df_slice_table],axis=1)
    # del_[boso]
    df = df.drop(columns=["boso"])
    # convert_[n]_to_datetime
    df["n"] = pd.to_datetime(df["n"],dayfirst=True)
    # sort_df_by_[n] //newest_on_bottom
    df = df.sort_values("n")
    # print(f">> df_out \n{df}")

    # file_out /{key}.csv
    file_out = filepath + f"{filename}.csv"
    df.to_csv(file_out,index=False)
    # print(f">> file_out = {file_out}")