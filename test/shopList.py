import requests
import time

from init import js_code
from sign import Signature
import frida
import requests
import json

rpc_result = ''


def on_message(message, data):
    global rpc_result
    if message["type"] == "send":
        print("[*] {0}".format(message["payload"]))
        rpc_result = str(message["payload"])

    elif message['type'] == "error":
        print("[ERROR] " + message["description"])

    else:
        print(message)


process = frida.get_remote_device().attach("com.sankuai.meituan.takeoutnew")

script = process.create_script(js_code)  # 创建js脚本
script.on("message", on_message)
script.load()  # 加载脚本

headers = {
    # 'mtgsig': '{"a0":"1.5","a1":"e68c4c18-35ec-4972-84e4-32a0836455a8","a2":"ab1118d1d5b21d59685f2cf87581b3b107bd7c34","a3":2,"a4":1613546146,"a5":"y4q52hF++BS5gVtI1Jz5LYikq1O2PG2awwvixOFLK55b2sDHboeI0GWosci7yO10l6iaqS90tFCqaPQLQJ2+moA+crU1QIBqxgxTI0BK8TdfFsoiIVbC9Rhk4XQ8w1uQbHnP978+pxS8jaf6YOGv6edZp/gW73sMuU9Co9Qr/IrzDWQxrDi1QESmEgirHPJ7bmTEtcvabqrBYbiqMYxWntUkKbek6YE9jrfdqbcI6zSP38LGWl/S+7GzmlbZkR3Xi7Be8vsU/Ce5hT7gdUP2aN3Q2x0ThV1b2QQxA2DuCYQZsPRu02iogjM6IoxYE43dT0cwWlxzVTUh+gxzT1jk/OzybHQ9Ru4ocvVnO3vfZft0OcXPQPrsHf9FNaOB6E0=","a6":0,"d1":"f7e9f88ad691d4668358ace2c3bb696cb19a5018"}',
    # 'siua': 'a2.0jC7INHKC2FDIqUsFt0RH2O/nQbNp/NfHpaFFZsvA9bFSCbdj2JLoViR5G2AXBNomaSnRmtKYNIrVwdRO9+C1wf+Swb55PrRIAw9k4HhZrbFq3QAK3mDWxlNLqbM3s+xkZLTS4ZaUrDJo/PQpUW0a/YWeBkqgrgEB85GUhxP1zbJbappZt77Bw+LzMm13xX7p97BSmICsanY+Bs7t/wVkFy9OQBLQPYr5TnQ/J6R77/l5C0u/woAQUtXJrfD7irqRC+i6v20CaC5s/7W84a6j5QBXBxnJNhXUwbt6yb5sodVB1hE1lZKC8BRAKUyrM//6C/ks8zMzVT87JaId3cXC/YgdsDqXJUn5y3aibTqVWcQrzPC/dw493PXUrcgOsbfP2Sc9Iq2YkX8w00HMXQrh3IBEzGI0T5z82W/XP872hD2J06yL+gEeiIUmEz2w/GGbKW1y/ZiIdFdTXjA3SWOhT8mU97z3ZRpykcbL3N9DxnT13UH44CYwqIupLdFjYoZdAYioQQl72kHBR5cVntaJkV+YZkzMyyym+k/dMakhj6tMdG7dHCdWjbU42CrwVH4GCI058cmKVsSrPFdQYj4p6Wp+7pkgSGvyKRoXiQLzDC0yOgrbCzOlqxi7qAZCB3Z2mkoHcdCkeg80tGUd+LyN1HHWLIyn3potgjqClp8x/A5=',
    'Content-Type': 'application/x-www-form-urlencoded',
    'retrofit_exec_time': '1613546146445',
    'Accept-Encoding': 'gzip',
    'M-SHARK-TRACEID': '',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/9.8.29)',
    'Host': 'wmapi.meituan.com',
    'Connection': 'Keep-Alive',
}

params = (
    ('utm_medium', 'android'),
    ('utm_content', ''),
    ('utm_source', '1011'),
    ('utm_term', '75204'),
    ('ci', '45'),
    ('utm_campaign', 'AwaimaiBwaimai'),
    ('uuid', ''),
    ('region_version', '1613545977790'),
    ('region_id', '0'),
)

data = {
    'seq_num': '0',
    'offset': '0',  # 奇怪的参数
    'dynamic_page': 'true',
    'latitude': '',
    'longitude': '',
    'page_index': '0',  # 似乎与seq_num同步，大过 1 就要登陆
    'page_size': '0',
    'sort_type': '0',
    'category_type': '910',
    'filter_type': '0',
    'second_category_type': '0',
    'navigate_type': '910',
    'activity_filter_codes': '',
    'slider_select_data': '',
    'load_type': '3',
    'preload': '0',
    'trace_tag': '',
    'rank_trace_id': '',
    'rank_list_id': '',
    'session_id': '',
    'union_id': '',
    'behavioral_characteristics': json.dumps(
        {
            "module_action": {
                "extra_info": {
                    "factlist_offset_after_dedup": 80
                },
                "request_type": 2
            },
            "exp_info": {
                "exp_group_name": "poilist_dynamicPaging_exp",
                "exp_name": "B",
                "scene_name": "poilist_dynamicPaging",
                "jsBundle_id": "alita_waimai-ad-interaction-rmd"
            }
        }
    ).replace(' ', ''),
    'wm_logintoken': '',
    'wm_mac': '02:00:00:00:00:00',
    'poilist_mt_cityid': '45',
    'request_id': '',
    'uuid': '',
    'wm_actual_longitude': '',
    'wm_actual_latitude': '',
    'wm_ctype': 'android',
    'app': '4',
    'wm_visitid': '',
    'userid': '',
    'wm_did': '',
    'platform': '4',
    'seq_id': '755',
    'wm_dversion': '25_7.1.1',

    'wm_longitude': '104066363',  # 这个来定位纬度！！！   9位
    'wm_latitude': '30657353',  # 这个来定位经度！！！    8位

    'oa_id': '',
    'wm_channel': '1011',
    'wm_uuid': '',
    'poilist_wm_cityid': '500100',
    'wm_dtype': 'MI MIX 2',
    'version': '7.54.2',
    'push_token': '',
    'personalized': '1',
    'partner': '4',
    'wm_appversion': '7.53.3',
    'waimai_sign': '',
    'wm_seq': '387',
    'req_time': ''
}

# =================================
nt = int(str(time.time()).replace('.', '')[:13])
data.update({
    'req_time': str(nt)  # 更新data里的时间戳
})

# 更新params里的时间戳
params = dict(params)
params['region_version'] = str(nt)
params = tuple([(k, params.get(k)) for k in params])

# 更新headers里面的时间戳
headers['retrofit_exec_time'] = str(nt)
# ================================

paramsString = (''.join([string[0] + "=" + string[1] + "&" for string in list(params)]))
dataString = (''.join([key + '=' + data.get(key) + "&" for key in data]))

# 得到 mtgsig 并加入headers里
Signature("POST", "/api/v7/poi/channelpage", dataString, paramsString, script, "shopList").getMtgSig()
headers.update({
    "mtgsig": rpc_result
})

# 执行请求
response = requests.post(
    'https://wmapi.meituan.com/api/v7/poi/channelpage', headers=headers, params=params, data=data
)

print(json.dumps(response.json(), indent=4, ensure_ascii=False))

with open('shopList.json', 'w', encoding="UTF-8") as f:
    json.dump(response.json(), fp=f, indent=4, ensure_ascii=False)
