import re
import time
from urllib.parse import quote


class Signature(object):
    module = "{method} {url} {bp}"
    MtgSigSignString = str()

    def __init__(self, method, url, body, params, rpc, sign_type):
        self.method = method
        self.url = url
        self.body = body
        self.params = params
        self.rpc = rpc
        self.signType = sign_type

    def structure_shopList_sign_string(self):
        shopList_key_list = [
            'activity_filter_codes', 'app', 'behavioral_characteristics', 'category_type', 'ci', 'dynamic_page',
            'filter_type', 'latitude', 'load_type', 'longitude', 'navigate_type', 'oa_id', 'offset', 'page_index',
            'page_size', 'partner', 'personalized', 'platform', 'poilist_mt_cityid', 'poilist_wm_cityid', 'preload',
            'push_token', 'rank_list_id', 'rank_trace_id', 'region_id', 'region_version', 'req_time', 'request_id',
            'second_category_type', 'seq_id', 'seq_num', 'session_id', 'slider_select_data', 'sort_type',
            'trace_tag', 'union_id', 'userid', 'utm_campaign', 'utm_content', 'utm_medium', 'utm_source',
            'utm_term', 'uuid', 'uuid', 'version', 'waimai_sign', 'wm_actual_latitude', 'wm_actual_longitude',
            'wm_appversion', 'wm_channel', 'wm_ctype', 'wm_did', 'wm_dtype', 'wm_dversion', 'wm_latitude',
            'wm_logintoken', 'wm_longitude', 'wm_mac', 'wm_seq', 'wm_uuid', 'wm_visitid'
        ]
        comment_key_list = [
            'app', 'ci', 'comment_score_type', 'label_id', 'oa_id', 'page_offset', 'page_size',
            'partner', 'personalized', 'platform', 'poilist_mt_cityid', 'poilist_wm_cityid',
            'partner', 'personalized', 'platform', 'poilist_mt_cityid', 'poilist_wm_cityid',
            'push_token', 'region_id', 'region_version', 'req_time', 'request_id', 'seq_id', 'userid',
            'utm_campaign', 'utm_content', 'utm_medium', 'utm_source', 'utm_term', 'uuid', 'uuid',
            'version', 'waimai_sign', 'wm_actual_latitude', 'wm_actual_longitude', 'wm_appversion',
            'wm_channel', 'wm_ctype', 'wm_did', 'wm_dtype', 'wm_dversion', 'wm_latitude',
            'wm_logintoken', 'wm_longitude', 'wm_mac', 'wm_seq', 'wm_uuid', 'wm_visitid', 'wmpoiid'
        ]
        shopDetail_key_list = ['ad_activity_flag', 'allowance_alliance_scenes', 'app', 'brand_page_type', 'ci',
                               'content_info', 'oa_id', 'page_index', 'partner', 'personalized', 'platform',
                               'poilist_mt_cityid', 'poilist_wm_cityid', 'product_spu_id', 'push_token', 'recall_type',
                               'region_id', 'region_version', 'req_time', 'request_id', 'search_log_id', 'search_word',
                               'seq_id', 'source_page_type', 'style_template_ids', 'userid', 'utm_campaign',
                               'utm_content', 'utm_medium', 'utm_source', 'utm_term', 'uuid', 'uuid', 'version',
                               'waimai_sign', 'wm_actual_latitude', 'wm_actual_longitude', 'wm_appversion',
                               'wm_channel', 'wm_ctype', 'wm_did', 'wm_dtype', 'wm_dversion', 'wm_latitude',
                               'wm_logintoken', 'wm_longitude', 'wm_mac', 'wm_poi_id', 'wm_seq', 'wm_uuid',
                               'wm_visitid']

        source_bp = "&" + self.params + self.body

        bp = str()
        if self.signType == "shopList":
            for key in shopList_key_list:
                if key == "behavioral_characteristics" or key == "wm_dtype" or key == "wm_mac":
                    result = re.findall("&" + key + '=(.*?)' + "&", source_bp)
                    bp += (key + "=" + quote(result[0]) + '&' if result else "" + "&")

                else:
                    result = re.findall("&" + key + '=(.*?)' + "&", source_bp)
                    bp += (key + "=" + result[0] + '&' if result else "" + "&")

        elif self.signType == 'comment':
            for key in comment_key_list:
                if key == "behavioral_characteristics" or key == "wm_dtype" or key == "wm_mac":
                    result = re.findall("&" + key + '=(.*?)' + "&", source_bp)
                    bp += (key + "=" + quote(result[0]) + '&' if result else "" + "&")

                else:
                    result = re.findall("&" + key + '=(.*?)' + "&", source_bp)
                    bp += (key + "=" + result[0] + '&' if result else "" + "&")

        elif self.signType == "shopDetail":
            for key in shopDetail_key_list:
                if key == "behavioral_characteristics" or key == "wm_dtype" or key == "wm_mac" or key == "style_template_ids":
                    result = re.findall("&" + key + '=(.*?)' + "&", source_bp)
                    bp += (key + "=" + quote(result[0]) + '&' if result else "" + "&")

                else:
                    result = re.findall("&" + key + '=(.*?)' + "&", source_bp)
                    bp += (key + "=" + result[0] + '&' if result else "" + "&")

        bp = bp.strip("&")
        self.MtgSigSignString = self.module.format(method=self.method, url=self.url, bp=bp)

    def getMtgSig(self):
        self.structure_shopList_sign_string()
        print(self.MtgSigSignString)
        return self.rpc.exports.getmtgsig(self.MtgSigSignString)
