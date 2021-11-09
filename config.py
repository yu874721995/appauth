import os



class RunConfig:
    """
    运行测试配置
    """
    #项目根路径
    PRO_PATH = os.path.dirname(os.path.abspath(__file__))

    # 运行测试用例的目录或文件
    cases_path = os.path.join(PRO_PATH, "testsuites", "mine/test_mine.py")

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "Android"

    # 配置运行的 URL
    url = "dengtahuaren_test"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None

    #设备信息（不需要修改）
    devices = None

