import os
import sys
import json

os.system("adb forward tcp:27042 tcp:27042")
os.system("adb forward tcp:27043 tcp:27043")

with open("jscode.js", 'r', encoding="UTF-8") as f:
    js_code = f.read()

HOST = "https://wmapi.meituan.com/api/v7/poi/channelpage"

rpc_result = ''
