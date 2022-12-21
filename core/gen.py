# (__module__/snippets) <generative> 
"""generative
__version__: "2022.12.20"
<model: chatGPT by OpenAI /Generative Pre-trained Transformer/>
<gen.py is __module__/snippet of lottGPT>

features
--------
- http.client: open(url[key]) /requests/ -> file_out/__{key}.html
- html.parser: parse(html)    /bs4/      -> file_out/__{key}.csv

options
-------
- http.client: /urllib3/requests/selenium/pandas/
- html.parser: /bs4/pandas/

usage
-----
>>> from core import gen
>>> gen.requests(key)
<file_out>
"""
# config
url = {
    "mega"  : "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-645",
    "power" : "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655",
    "plus"  : "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-max-3D",
    "pro"   : "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-max-3Dpro",
    "keno"  : "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno",
    "bingo" : "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18"
    }
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Cookie":"D1N=2b2539267fd5d415c6612fca144300c5"
    }
filepath = "./data/"

# http.client
# def urllib3(key):
#     import urllib3
#     # build_[b]rowser
#     b = urllib3.PoolManager()
#     # open(url) -> get_[r]esponse /html/
#     r = b.request("GET",url[key],headers)
#     # /out/
#     return bs4(r.data)

def requests(key):
    # import requests
    # open(url) -> get_[r]esponse /html/
    # r = requests.get(url[key],headers=headers)
    # print(f"== <gen.requests> \n>> url = {r.url} \
            # \n>> headers = {r.request.headers} \n>> status_code = {r.status_code}")

    # file_out /__{key}.html
    global filename
    filename = key
    file_out = filepath + f"__{filename}.html"
    # with open(file_out,"w",encoding="utf-8") as f: f.write(r.text)
    # print(f">> file_out = {f}")

    # for-dev/lab/test /skip-requests/
    with open(file_out,"r",encoding="utf-8") as f: bs4(f)
    # /out/
    # return bs4(r.text)

# def selenium(key):
#     from selenium import webdriver
#     # start_[b]rowser
#     b = webdriver.Chrome()
#     # open(url) -> get_[r]esponse /html/
#     # /default/
#     b.get(url[key])
#     # /option/
#     # from selenium.webdriver.chrome.options import Options
#     option = Option()
#     # disable_notice_bar
#     # options.add_experimental_option("excludeSwitches",["enable-automation"])
#     # b = webdriver.Chrome(options=options)
#     r = b.page_source
#     # quit_browser
#     b.quit()
#     # /out/
#     return bs4(r)

# html.parser
def bs4(html):
    from bs4 import BeautifulSoup
    # read_html/[s]tring/[s]ource
    # s = BeautifulSoup(html,"html.parser")
    # case: /keno/ /if use html.parser -> error: duplicate_header/
    s = BeautifulSoup(html,"lxml")

    # get_html_table [0]
    html_table = s.find("table")
    ## get_html_thead
    html_thead = html_table.find("thead")
    ## get_html_tbody
    html_tbody = html_table.find("tbody")

    ## make_new_array = tbody
    tbody = []
    ## add_new_row /to_[tbody]/
    for tr in html_tbody.find_all("tr"):
        new_row = []
        ## add_new_cell /to_[new_row]/
        ## case: /special/ <th>_in_<tbody>/<tr> /keno/bingo/
        if tr.find("th"):
            for th in tr.find_all("th"):
                new_cell = th.get_text(strip=True)
                # print(f">> new_cell = {new_cell}")
                new_row.append(new_cell)
        ## case: /default/ <td>_in_<tbody>/<tr>
        else:
            for td in tr.find_all("td"):
                new_cell = td.get_text(strip=True)
                new_row.append(new_cell)
        tbody.append(new_row)
    
    # join(thead,tbody) /new_table = join_table
    ## case: /default/ <table>_has_<thead> /ball/mega/power/
    if html_thead:
        thead = [th.get_text(strip=True) for th in html_thead.find_all("th")]
        join_table = [thead] + tbody
    ## case: /special/ <table_not_<thead> /max/plus/pro/keno/bingo/
    else: join_table = tbody

    # [join_table]/array-2d/ -> to_[s]tring_csv //new_string = string_csv
    string_csv = ""
    for item in join_table:
        string_csv += ",".join(item) + "\n"

    # file_out /__{key}.csv
    file_out = filepath + f"__{filename}.csv"
    with open(file_out,"w",encoding="utf-8") as f: f.write(string_csv)
    # print(f"== <bs4> \n>> string_csv \n{string_csv} \n>> file_out = {f}")

# def pandas(key):
#     import pandas as pd
#     # http.client -> html.parser -> file_out
#     # case: server_not_request_headers/cookies
#     df = pd.read_html(url[key])
#     # file_out
#     df.to_csv(file_out)
# end