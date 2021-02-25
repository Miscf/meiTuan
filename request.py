import requests
import time
import frida
import os

from sign import Signature

os.system("adb forward tcp:27042 tcp:27042")
os.system("adb forward tcp:27043 tcp:27043")
rpc_result = ''
with open("jscode.js", 'r', encoding="UTF-8") as f:
    js_code = f.read()


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
    'mtgsig': '{"a0":"1.5","a1":"e68c4c18-35ec-4972-84e4-32a0836455a8","a2":"6376acd393ebf6d32395353be6d3f14225ec4ef0","a3":2,"a4":1614246247,"a5":"j9tzEdj9gY+I4Khhyn330m8DxMjEoybbJ6oRN1+1qSDH3UcBS3SyMqsulyiCpIkY0dUnP9lpctF6Jn1eyGMe2CCw8mWjhl/5oQ+17M/JsjZSJSzDEotKXUi0r7mcfhIgxuI/HrDCaJwKjBhGisB8gmy7Qsqf89lvr5+s3gpnU+8LizFyya/1iEwGBtUZJuBQsHOlfQCbgQ0jlr+XN18JNEat8Lpo8PhFSMJMZeLndJDaNOuSr1kRurJed5cW4UIpoEhfTARwdar8CV5LH6LMjZDZh1aQbpUXgetsF1xKKF7DS5nn9OKfDb+p8i7aFxhZdpzlm9oDfJovzYVrry5zbCrSb2IPyqSElFwk7ZHvRBbTDuashPRR2jY41Lx47A==","a6":0,"d1":"b664b3ea4dcf2c54f4503e4023764a453c7b870b"}',
    'siua': 'a2.0+X30+K7m/d80owfbU4pPqVkztUv/oBluSGRvIG7A7hd40eXay7YSAZKVtwwJjo1nOR1OnPeEEFMkER/RMLxmd6He5pLJy5hJRNvB8Yo9b86FVj+ZVXddxrtfpzlLqLxgoODhkqpHRijdshFcU8ZrKjB+iB8YiV7J0OfH6BFUcg+ezWbjL94kikWIU9VuHsL+HVj/WwVLF+anQ5Lx6goICMO1/d/b9H1NDAvabbrFz8xD9SBvitnI+i677ceSQe7VN25m7Ka/Nqi0+SnK9W5GCtkOwkL2fyyl9VFZCu8kP1/BECuBsVpr3ivdeVQanjps2wNUW8RSyMekj5u0gnQyL4acIRmhyEU0/ZM0VGleTYeE2x0tQ7RQORIndpPQ5n3Sqzzk2hBtLYZN5vtWN02sx/d2C6N7E7dWWF1dM+hgaVIHNt9e/EKI3DdQ9hTNIljZeOVWNrwkUHuWvd7H1kUSdG372yYBLLcmT8tHtNEQL2LBROtBuQuaW4oj6Dk7GNVmWkMZIQzM/MUu/Iq8n6/NO5amlsvHo49xI7iRFW+4gdHGsanqOwbDNHbo7K28I1lEUUOHMEs0rgdQ+qFGgV+zLuo5FB3QgzlCQcWW8FMQ8k4InEV8bbOH4CKJ/FVerMdicknsmlEKAlv4nZqhg+mjI2Q/92G9zpDr6/Go1vL1eUk=',
    'Content-Type': 'application/x-www-form-urlencoded',
    'retrofit_exec_time': '1614246247095',
    'Accept-Encoding': 'gzip',
    'M-SHARK-TRACEID': '1118c216b6de4e84a60981ed172f5ca81cea161344370271699288a12a481614246247158b27ae3',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/9.8.29)',
    'Host': 'wmapi.meituan.com',
    'Connection': 'Keep-Alive',
}

params = (
    ('utm_medium', 'android'),
    ('utm_content', '868415032525454'),
    ('utm_source', '1011'),
    ('utm_term', '75303'),
    ('ci', '45'),
    ('utm_campaign', 'AwaimaiBwaimai'),
    ('uuid', '00000000000008C216B6DE4E84A60981ED172F5CA81CEA161344370271699288'),
    ('region_version', '1614246134693'),
    ('region_id', '1000530100'),
)

data = {
    'wmpoiid': '908511361599386',
    'page_offset': '0',
    'page_size': '20',
    'comment_score_type': '0',
    'label_id': '0',
    'wm_latitude': '29465667',
    'wm_logintoken': 'zUE16KqZ3XFQ1WtRdl0OvroChE8AAAAAzAwAAJ378QLes7UuG4MjeSNM9grqW-8mQt4inMbTJ90dx8mBWKppFx6exnYK5wIHtAG2jA',
    'wm_mac': '02:00:00:00:00:00',
    'poilist_mt_cityid': '45',
    'request_id': '5E1C692E-4ECE-4858-8980-38974E764D77',
    'uuid': '00000000000008C216B6DE4E84A60981ED172F5CA81CEA161344370271699288',
    'wm_actual_longitude': '106540890',
    'wm_actual_latitude': '29465029',
    'wm_ctype': 'android',
    'app': '4',
    'wm_visitid': '5e80f4ae-b63a-4e23-8517-ae485889b2a2',
    'userid': '911426266',
    'wm_did': '868415032525454',
    'platform': '4',
    'seq_id': '114',
    'wm_dversion': '25_7.1.1',
    'wm_longitude': '106543519',
    'oa_id': '',
    'wm_channel': '1011',
    'wm_uuid': '00000000000008C216B6DE4E84A60981ED172F5CA81CEA161344370271699288',
    'poilist_wm_cityid': '500100',
    'wm_dtype': 'MI MAX 2',
    'version': '7.53.3',
    'push_token': 'dpsh0cf9ffa87d5741e4ba4dc164b5558702atpu',
    'personalized': '1',
    'partner': '4',
    'wm_appversion': '7.53.3',
    'waimai_sign': 'Xqnfwe3wv/f/VuS6UHCAHjz9Lpsqu4h5ut0AxJl+UAT/bi6XXCGhuotkEUQ+fSIrEr17LOU3SzP7gFYk9o7euQ8b+zrTmkLhmcysUzj1BQQhX1feVNWusfAPn3vSUQcQ3FunM6qKt9Ock8uUfGwIn0YVZmddL/vp9+5h8gUDIMg=',
    'wm_seq': '68',
    'req_time': '1614246247039'
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

print(response.text)
