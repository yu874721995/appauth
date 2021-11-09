
#### 介绍
基于selenium,appium,python的API自动化测试框架

#### 软件架构
- 语言：python
- 自动化框架：selenium,appium,pytest
- 设计模式:POM/关键字驱动/数据分离/配置分离
- 自动化用例组织框架：

#### 设计原则
1.  公共方法为页面提供操作服务
2.  封装细节，对外只提供方法名（或者接口）
3.  断言放在用例
4.  通过return跳转到新页面
5.  页面中重要元素进行PO管理
6.  对相同行为产生不同结果进行封装

#### 安装教程

0.  安装python3.7及以上,Appium1.21
1.  http://121.201.57.217/dxl/dengta_appauto 拉取代码
2.  pip install -r requirements.txt 安装依赖库
3.  修改config.py配置文件
4.  执行run_tests.py

#### 目录结构
```
|-- 自动化测试 # 主目录
    ├─common        # 工具包
    │  └─page.py	             #基本操作类
    ├─element       # 页面元素
    │  ├─ele_public.py           #公共
    │  ├─ele_login.py            #登录
    │  ├─ele_index.py            #首页
    │  ├─ele_information.py      #消息
    │  └─ele_mine.py             #我的
    ├─image
    │  └─...x.png	# 测试失败截图文件
    ├─logs
    │  └─...x.log	# 日志文件
    ├─report
    │  ├─xml                #报告数据
    │  └─html		        #测试报告
    ├─testsuites        # 测试用例套件
    │  ├─index	        #首页 测试用例
    │  ├─information	#信息 测试用例
    │  ├─login	        #登录 测试用例
    │  ├─mine	        #我的 测试用例
    │  └─conftest.py    #模块级conftest
    ├─config.py          # 项目全局变量管理
    ├─config.yaml        # 手机参数变量管理
    ├─conftest.py        # 会话级conftest
    ├─pytest.ini	     # pytest配置文件
    ├─README.md          # 自述文件
    ├─requirements.txt   # 项目依赖库文件
    └─run_tests.py	     # 测试主启动文件
```


#### 使用说明

1.  



#### 实现功能
1.  用例失败重跑



#### 待开发
1.  多线程执行
2.  多机型
3.  持续集成

