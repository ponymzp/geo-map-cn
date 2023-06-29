# -*- coding: utf-8 -*-

import json
import requests
import os


# 获取区域编码类型
def get_area_code_type(code):
    # 省级编码
    if code[2:6] == "0000":
        return "province"
    # 市级编码
    elif code[4:6] == "00":
        return "city"
    # 县级编码
    else:
        return "district"


def get_geos():
    # 创建文件夹
    geos_dir = "src/geos/"
    if not os.path.isdir(geos_dir):
        os.makedirs(geos_dir)
    for dir in ["province", "city", "district"]:
        if not os.path.isdir(geos_dir + dir):
            os.makedirs(geos_dir + dir)
            print("create {} folder success".format(dir))

    # 获取所有城市列表
    info = requests.get(url="https://geo.datav.aliyun.com/areas_v3/bound/infos.json")
    info = json.loads(info.content.decode(encoding='utf-8'))
    with open(geos_dir + "location.json", "w", encoding='utf-8') as json_file:
        json.dump(info, json_file, ensure_ascii=False)
        print("write location.json success")
    # 获取城市详细数据
    for item in list(info.keys()):
        urls = [
            "https://geo.datav.aliyun.com/areas_v3/bound/{}.json".format(item),
            "https://geo.datav.aliyun.com/areas_v3/bound/{}_full.json".format(item)
        ]
        dir = geos_dir
        # 全国数据
        if item != "100000":
            dir = geos_dir + "/" + get_area_code_type(item)
        print("request {} start".format(urls[0]))
        res, res_full = requests.get(url=urls[0]), requests.get(url=urls[1])
        if res.status_code != 200 and res_full.status_code != 200:
            print("get {} error".format(urls[0]))
        else:
            if res_full.status_code == 200:
                res_full = res_full
            else:
                res_full = res
            res_full = json.loads(res_full.content.decode(encoding='utf-8'))
            with open(dir + "/" + urls[0].split('/')[-1], "w", encoding='utf-8') as json_file:
                json.dump(res_full, json_file, ensure_ascii=False)
            print("write {} success".format(urls[0]))
    print("all  success")


if __name__ == "__main__":
    get_geos()
