# seleneium基础框架

## 需要使用的依赖库
使用打包文件requirements.txt安装依赖库

`pip install -r requirements.txt`


- 一些常用的国内镜像下载地址  
    阿里云 http://mirrors.aliyun.com/pypi/simple/  
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/  
    豆瓣(douban) http://pypi.douban.com/simple/  
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/  
    中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
    
    
## 框架结构如下
###公共方法
* areacode.py     文件内使用的区域编码文件
* by_element.py   枚举查找元素的方式
* openbrowser.py  封装常用的元素事件
* readini.py      读取配置文件
* testng,py       一些常用的数据生成（手机号码、身份证号码、随机名，读取Excel等）


### 驱动文件
* driver 存放常用的浏览器driver

### 截图
* error_img 存放用例失败后的的截图

### 日志
* log.py    日志的封装
* log_file  日志存放位置

### 根目录
* conftest.py 修改测试报告的描述样式
* run.py      执行所有测试用例

## 测试用例

* case 存放测试用例

## 使用实例
![image text](http://chuantu.xyz/t6/741/1611664190x989559130.png)

![image text](http://chuantu.xyz/t6/741/1611664239x-1404755342.png)

![image text](http://chuantu.xyz/t6/741/1611664277x989559130.png)

