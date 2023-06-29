# geo-map-cn

## 简介

爬取整理中国各省、市区县GeoJson格式数据。

> 更新时间: 2023-06-08

> 数据时间: 2022-01-26

> 数据来源: http://datav.aliyun.com/tools/atlas/

## 数据简介

> 数据位置 src/geos

### location.json

> 全国省市区县所对应行政区划代码以及中心点的坐标

### 100000.json

> 全国地图

### province
> 全国各省地图 

### city
> 全国各市地图

### district
> 全国各区县地图

## 代码

> get_geos.py


## 结果展示

> 工具: https://geojson.io/

以全国地图为例(src/geos/100000.json), 绘制结果如下:

![100000.json](src/images/100000.png)

