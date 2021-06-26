import requests
import json

# url = 'http://api.******.cn?stu_name=aaa '#请求接口
# url1 = 'http://api.map.baidu.com/traffic/v1/road?road_name=北二环&city=北京市&ak=2aqU8FLFTjRC65BU6OOwdc8dRHqv9ImR'#请求接口
# url1 = 'http://api.map.baidu.com/traffic/v1/road?road_name=大学城南路&city=重庆市&ak=2aqU8FLFTjRC65BU6OOwdc8dRHqv9ImR'#请求接口
# url2 = 'http://api.map.baidu.com/traffic/v1/road?road_name=大学城中路&city=重庆市&ak=2aqU8FLFTjRC65BU6OOwdc8dRHqv9ImR'#请求接口
# req1 = requests.get(url1)#发送请求
# req2 = requests.get(url2)#发送请求


# 获取路况信息
# 0：未知路况 1：畅通 2：缓行 3：拥堵 4：严重拥堵
def find_status(dic1):
    res = 1
    for x in dic1.keys():
        if x == "road_traffic":
            for y in dic1[x][0].keys():
                if y == "congestion_sections":
                    for z in dic1[x][0][y][0].keys():
                        if z == "status":
                            res = dic1[x][0][y][0][z]
    return res


def to_pre(status):
    """
    将路况转化为可信度知识前提
    :param status: int 类型
    :return: str 模糊数据
    """
    if status == 1:
        res = "畅通"
    elif status == 4:
        res = "严重拥堵"
    elif status == 3:
        res = "拥堵"
    elif status == 2:
        res = "缓行"
    else:
        res = "未知路况"
    return res


def baidumap(road1,road2,city1,city2):
    url1 = 'http://api.map.baidu.com/traffic/v1/road?road_name=' + road1 +'&city=' + city1 + '&ak=2aqU8FLFTjRC65BU6OOwdc8dRHqv9ImR'#请求接口
    url2 = 'http://api.map.baidu.com/traffic/v1/road?road_name=' + road2 +'&city=' + city2 + '&ak=2aqU8FLFTjRC65BU6OOwdc8dRHqv9ImR'#请求接口

    req1 = requests.get(url1)#发送请求
    req2 = requests.get(url2)#发送请求
    # print(req1.text)#获取请求，得到的是json格式
    # print(json.loads(req.text))#获取请求，得到的是字典格式
    dic1 = json.loads(req1.text)
    dic2 = json.loads(req2.text)
    print(dic1)
    print(dic2)
    status1 = find_status(dic1)
    status2 = find_status(dic2)
    res1 = to_pre(status1)
    res2 = to_pre(status2)
    return res1, res2

# res1, res2 = baidumap("大学城南路","大学城中路","重庆市","重庆市")
