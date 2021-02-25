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
    # 'mtgsig': '{"a0":"1.5","a1":"e68c4c18-35ec-4972-84e4-32a0836455a8","a2":"9c62a006c5776a9f82529e6ab74b07af08621a9b","a3":2,"a4":1614177446,"a5":"Qhv5cejhqeoLHPc7wuuwnBL/AALpXENkr1orKCYCJ+6niOo6IMvS9xYEAD9wvd1yPyPMVmDWz5vJbBev28pxGbC2WmquCkrSIoL+w1+dkDP5Irzeqvk2X22u1Na3QIyITtsb2tc72mHJID8DaVgP/L7hVn2wICcgVMoOGQuDFJxNO6VWtW9aSugFqfbMDIRlNjg6DAB58MIOLHDzAPHrRKUiOmEApMmE8oSfQnOrzJNtlPmiM316Df6pdmFBQQYryX/mKD7lFip7k7F4TBF4TRoT56Z2Q7nykB2w9MJcDPGmTPWcOIQyu86jM3tNqRHnu6VADPeB664SB6WkedEDao0E3bC3pLbWejFaavadbyDSLxmB3+xRGCvsHI6ZL+o=","a6":0,"d1":"9af2f469f29993642f3365511950371d927ecca6"}',
    # 'siua': 'a2.0+JXBEcOxn9Ita2OtFryXwHSE5Efab4YoJhuNWVlGems+Ur4pKtdFhTiBmcMsw+GHHF0z/TJgGVKRPSpjJSUBnt54dvopPgLXv4CysPr4t4Y+3ysHHFGHC2QQLaGcvtdoy8d0Ef6KvUQUfa/9oFX1R4Rp5VH4fep8S0nTMf9T+t5fwJpqCbi2/Jc6GDulf+yxMjNzts0+5JWhZTlRnuoBE1AW0VHm2aR7YgLBd+ySdQFyoavoESRXt1xa5yupd8+56PxpDItNYEf55f4JaHw2eKw80H8ehlpmDu1IsjMtq+62cKIDwMFrX4Tc/uo88sT/PRbSjBHdQOMysqLTYGv3fs1y3rsONmp/1LB0N9SsOOMJqMvXjriAIN0HkvVsQKeOM8ep2JnfEleTU/zBsPcfwgHv/4YbhEJTl6cl4DHnM2MAheU+embremBSwitRuH5CCa/hY3BypfG9LvkrCE/MibmDpFVftATimkHw64gF2IvCdUI4boaWn0fTl8DKZa001BirOJOsOZquMX0RPK3usIdSTJeU+jYddOL0DiOPwN7i1NaixPPdX9UxgJm68mPWnjGPPeDEylk3MwADZRvnvrW72M8K6i/3uXI1ANlxIr98lidy0GSTdt7rGKKcYnqTbh6fSNT5EP6jZnS2AB9dvlsSQ0FMoFgbE0WkjKIaZSA=',
    'Content-Type': 'application/x-www-form-urlencoded',
    'retrofit_exec_time': '1614177446772',
    'Accept-Encoding': 'gzip',
    'M-SHARK-TRACEID': '',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/9.8.29)',
    'Host': 'wmapi.meituan.com',
    'Connection': 'Keep-Alive',
}


uuid = "12dkslajdsahduisayd98a78978213789dusa9ds98aud98saud98saud98asud9"
params = (
    ('utm_medium', 'android'),
    ('utm_content', '868415032525454'),
    ('utm_source', '1011'),
    ('utm_term', '75303'),
    ('ci', '45'),
    ('utm_campaign', 'AwaimaiBwaimai'),
    ('uuid', uuid),
    ('region_version', '1614177415914'),
    ('region_id', '1000530100'),
)

data = {
    'wm_poi_id': '912917998037218',
    'product_spu_id': '0',
    'recall_type': '0',
    'search_word': '',
    'search_log_id': '',
    'page_index': '0',
    'source_page_type': '0',
    'style_template_ids': '',
    'allowance_alliance_scenes': '',
    'content_info': '',
    'ad_activity_flag': '',
    'brand_page_type': '0',
    'wm_latitude': '29436013',
    'wm_logintoken': 'zUE16KqZ3XFQ1WtRdl0OvroChE8AAAAAzAwAAJ378QLes7UuG4MjeSNM9grqW-8mQt4inMbTJ90dx8mBWKppFx6exnYK5wIHtAG2jE',
    'wm_mac': '02:00:00:00:00:00',
    'poilist_mt_cityid': '45',
    'request_id': 'F1FCDF5E-7F9A-4551-A96E-B823BEDBF7E3',
    'uuid': uuid,
    'wm_actual_longitude': '106534937',
    'wm_actual_latitude': '29435075',
    'wm_ctype': 'android',
    'app': '4',
    'wm_visitid': '',
    'userid': '',
    'wm_did': '',
    'platform': '4',
    'seq_id': '57',
    'wm_dversion': '25_7.1.1',
    'wm_longitude': '106535180',
    'oa_id': '',
    'wm_channel': '1011',
    'wm_uuid': uuid,
    'poilist_wm_cityid': '500100',
    'wm_dtype': 'MI MAX 2',
    'version': '7.53.3',
    'push_token': '',
    'personalized': '1',
    'partner': '4',
    'wm_appversion': '7.53.3',
    'waimai_sign': '',
    'wm_seq': '39',
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
Signature("POST", "/api/v8/poi/food", dataString, paramsString, script, "shopDetail").getMtgSig()
headers.update({
    "mtgsig": rpc_result
})

response = requests.post('https://wmapi.meituan.com/api/v8/poi/food', headers=headers, params=params, data=data)

print(response.json())

with open("shopDetail.json", 'w', encoding="UTF-8") as f:
    f.write(json.dumps(
        response.json(),
        ensure_ascii=False,
        indent=4
    ))
