import os
from fake_useragent import UserAgent
from init import js_code
import frida
import requests
import time
import json
from sign import Signature

rpc_result = ''


def on_message(message, data):
    global rpc_result
    if message["type"] == "send":
        rpc_result = str(message["payload"])

    elif message['type'] == "error":
        print("[ERROR] " + message["description"])

    else:
        print(message)


process = frida.get_remote_device().attach("com.sankuai.meituan.takeoutnew")

script = process.create_script(js_code)  # 创建js脚本
script.on("message", on_message)
script.load()  # 加载脚本
ua = UserAgent()


class Meituan(object):
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'siua': '',
            'retrofit_exec_time': '',
            'Accept-Encoding': 'gzip',
            'M-SHARK-TRACEID': '',
            'User-Agent': 'hh',
            'Host': 'wmapi.meituan.com',
            'Connection': 'Keep-Alive',
        }
        self.offset = 0
        self.file_save_path = "/Users/mac/Desktop/成都/"

    def getShopList(self):
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
            # 用来计数，你看过多少店铺
            'offset': str(self.offset),  # 奇怪的参数
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
                            "factlist_offset_after_dedup": 100
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
        self.headers['retrofit_exec_time'] = str(nt)

        # 更新 User-Agent
        # self.headers["User-Agent"] = '123'
        # ================================

        paramsString = (''.join([string[0] + "=" + string[1] + "&" for string in list(params)]))
        dataString = (''.join([key + '=' + data.get(key) + "&" for key in data]))

        # 得到 mtgsig 并加入headers里
        Signature("POST", "/api/v7/poi/channelpage", dataString, paramsString, script, "shopList").getMtgSig()
        self.headers.update({
            "mtgsig": rpc_result
        })

        # 执行请求
        response = requests.post(
            'https://wmapi.meituan.com/api/v7/poi/channelpage', headers=self.headers, params=params, data=data
        )

        return response.json()

    def getShopDetail(self, poi_id):
        uuid = "12dkslajdsahduixsayd98a78978213789dusa9ds98aud98saud98saud98asud9"
        params = (
            ('utm_medium', 'android'),
            ('utm_content', ''),
            ('utm_source', '1011'),
            ('utm_term', '75303'),
            ('ci', '45'),
            ('utm_campaign', 'AwaimaiBwaimai'),
            ('uuid', uuid),
            ('region_version', '1614177415914'),
            ('region_id', '1000530100'),
        )

        data = {
            'wm_poi_id': poi_id,
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
            # 这个东西要检测
            'wm_logintoken': 'zUE16KqZ3XFQ1WtRdl0OvroChE8AAAAAzAwAAJ378QLes7UuG4MjeSNM9grqW-8mQt4inMbTJ90dx8mBWKppFx6exnYK5wIHtAG2jE',

            'wm_mac': '02:00:00:00:00:00',
            'poilist_mt_cityid': '45',
            'request_id': '',
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
        self.headers['retrofit_exec_time'] = str(nt)
        # 更新 User-Agent
        # self.headers["User-Agent"] = '123'
        # ================================

        paramsString = (''.join([string[0] + "=" + string[1] + "&" for string in list(params)]))
        dataString = (''.join([key + '=' + data.get(key) + "&" for key in data]))

        # 得到 mtgsig 并加入headers里
        Signature("POST", "/api/v8/poi/food", dataString, paramsString, script, "shopDetail").getMtgSig()
        self.headers.update({
            "mtgsig": rpc_result
        })

        response = requests.post('https://wmapi.meituan.com/api/v8/poi/food', headers=self.headers, params=params,
                                 data=data)
        print(response.json())
        return response.json()

    def getShopComment(self, poi_id, page_offset):
        params = (
            ('utm_medium', 'android'),
            ('utm_content', ''),
            ('utm_source', '1011'),
            ('utm_term', '75303'),
            ('ci', '45'),
            ('utm_campaign', 'AwaimaiBwaimai'),
            ('uuid', ''),
            ('region_version', '1614176032912'),
            ('region_id', '1000530100'),
        )

        data = {
            'wmpoiid': str(poi_id),
            'page_offset': str(page_offset),
            'page_size': '50',
            'comment_score_type': '0',
            'label_id': '0',
            'wm_latitude': '',
            'wm_logintoken': '',
            'wm_mac': '',
            'poilist_mt_cityid': '45',
            'request_id': '',
            'uuid': '',
            'wm_actual_longitude': '',
            'wm_actual_latitude': '',
            'wm_ctype': 'android',
            'app': '4',
            'wm_visitid': '',
            'userid': '372837482832',  # 他对这个有检测
            'wm_did': '',
            'platform': '4',
            'seq_id': '71',
            'wm_dversion': '25_7.1.1',
            'wm_longitude': '',
            'oa_id': '',
            'wm_channel': '1011',
            'wm_uuid': '',
            'poilist_wm_cityid': '500100',
            'wm_dtype': 'Mi MAX 2',
            'version': '7.54.2',
            'push_token': '',
            'personalized': '1',
            'partner': '4',
            'wm_appversion': '7.53.3',
            'waimai_sign': '',
            'wm_seq': '48',
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
        self.headers['retrofit_exec_time'] = str(nt)

        # 更新 User-Agent
        # self.headers["User-Agent"] = '123'
        # ================================

        paramsString = (''.join([string[0] + "=" + string[1] + "&" for string in list(params)]))
        dataString = (''.join([key + '=' + str(data.get(key)) + "&" for key in data]))

        # 得到 mtgsig 并加入headers里
        Signature("POST", "/api/v6/comment/poi", dataString, paramsString, script, "comment").getMtgSig()
        self.headers.update({
            "mtgsig": rpc_result
        })

        response = requests.post(
            'https://wmapi.meituan.com/api/v6/comment/poi',
            headers=self.headers,
            params=params,
            data=data
        )

        return response.json()

    def start(self):
        while True:
            shopListDict = self.getShopList()
            if shopListDict.get('msg') == "成功" and shopListDict.get('data').get('poilist'):
                # 开始在 poilist 中遍历
                for _ in shopListDict.get("data").get('poilist'):
                    poi_save_path = self.file_save_path + str(_.get('id'))
                    if not os.path.exists(poi_save_path):
                        os.mkdir(poi_save_path)

                        # 入袋为安，先写为妙
                        with open(poi_save_path + '/shop.json', 'w', encoding="UTF-8") as f:
                            f.write(json.dumps(
                                _,
                                indent=4,
                                ensure_ascii=False
                            ))
                        print("[*] ", str(_.get('name')) + "粗略数据保存成功！")
                        time.sleep(1)

                        # 获取评论
                        comment_save_path = poi_save_path + '/comments'
                        if not os.path.exists(comment_save_path):
                            os.mkdir(comment_save_path)

                            current_save_num = 0
                            # 进入一个死循环，判断是否把评论json请求完毕
                            # 请求完毕则跳出
                            while True:
                                commentsDict = self.getShopComment(_.get('id'), str(current_save_num * 50))
                                if commentsDict.get("msg") == '成功' and commentsDict.get('data').get('comments'):
                                    # 如果评论返回成功且评论列表不为空
                                    # 就开始保存到文件里
                                    with open(comment_save_path + "/" + str(current_save_num) + ".json", 'w',
                                              encoding="UTF-8") as f:
                                        f.write(json.dumps(commentsDict, indent=4, ensure_ascii=False))
                                    print("[*] ", str(_.get('name')) + "评论 " + str(current_save_num) + " 保存成功！")

                                    if commentsDict.get("data").get("has_more"):
                                        # 如果接下来还存在评论没有爬完的话
                                        # 就自增一，继续爬取
                                        current_save_num += 1
                                        time.sleep(1)

                                    else:
                                        # 不存在的话就跳出循环，结束爬取
                                        break

                                elif commentsDict.get('code') == 801:
                                    # {'data': {'wait_time': 2}, 'subCodeString': '0', 'code': 801, 'msg': '您访问太频繁了，请稍后重试', 'traceid': '-6290469426780653685'}
                                    # 访问太频繁
                                    print("[*] 请求评论频繁，休息5秒...")
                                    time.sleep(5)

                                else:
                                    print("\n一些意料之外的错误发生了：")
                                    print(commentsDict)
                                    time.sleep(5)

                        time.sleep(1)

                        # 获取店铺详细信息
                        shop_detail_save_path = poi_save_path + '/shopDetail.json'
                        if not shop_detail_save_path:
                            os.mkdir(shop_detail_save_path)
                            shopDetail = self.getShopDetail(str(_.get('id')))

                            if shopDetail.get('msg') == "成功" and shopDetail.get('data').get('poi_info'):
                                # 检测请求是否成功
                                # 请求成功则开始保存
                                with open(shop_detail_save_path, 'w', encoding="UTF-8") as f:
                                    f.write(json.dumps(
                                        shopDetail,
                                        indent=4,
                                        ensure_ascii=False
                                    ))

                                print("[*] ", str(_.get("name")) + "详细数据保存完成！")

                    else:
                        # 本来应该检测完整性
                        # 嫌麻烦，先跳过
                        continue

                    print("[***]", str(_.get("name")), "所有数据保存完成！！！", "\n")

                # 遍历完毕，开始判断是否存在下一页
                if shopListDict.get("data").get("poi_has_next_page"):
                    # 改变偏移量
                    # 避免下一次请求到同样的店铺
                    self.offset += len(shopListDict.get('data').get('poilist'))
                    time.sleep(1)
                    print("开始进行下一页shopList！")
                    print("[*] ", self.offset)

                else:
                    print("保存完毕！")
                    print("所有工作都做完了！！")
                    # 保存完毕，跳出死循环
                    break

            elif shopListDict.get('code') == 801:
                print("[*] ", "请求商家列表频繁！休息5秒。。。")
                time.sleep(5)

            elif not shopListDict.get("poi_has_next_page"):
                print("保存完成！！！！")


if __name__ == '__main__':
    Meituan().start()
