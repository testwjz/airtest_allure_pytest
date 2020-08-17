# 说明文档
### 环境准备
    1、基础环境准备python3.7.2
    2、pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ airtest==1.1.3
    3、pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pocoui==1.0.79
    4、pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pytest==5.4.1
    5、pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ allure-pytest==2.8.13
    6、安装allure 2.13.3（提前需要安装JDK8+）
    7、配置本地ADB环境变量..\site-packages\airtest\core\android\static\adb\windows
    8、安装，用于日志颜色修改：pip install colorlog==4.1.0   
>allure下载地址：https://github.com/allure-framework/allure2/releases/tag/2.13.3

>   allure使用文档：https://docs.qameta.io/allure/

>   airtest使用文档：https://airtest.doc.io.netease.com/


### 源码修改
##### 1、report.py windows下需要修改，mac linux 不用修改
##### 路径：..\site-packages\airtest\report\report.py
    434 if not self.static_root.endswith(os.path.sep):
    435    self.static_root = self.static_root.replace("\\", "/")
    436    # 源码修改：注释以下代码
    437    # self.static_root += "/"

##### 2、修改log_template.html
##### 路径：..\site-packages\airtest\report\log_template.html
>对info info1、info-left内容添加样式：
 
    41  <div class="summary" >
    ...
    44  <div class="info info1" style="width: 80%;display: inline-block;display: flex;align-items: center;padding-left:100px;position: relative;">
    45  <div class="info-left" style="position: absolute;left: -23px;top: -28px;">
    
>注释以下内容
 
    75  <!-- </div>-->
    76  <!-- {% endif %}-->
    77  <!-- {% if log %}-->
    78  <!-- <div class="info-log">-->
    79  <!-- <span class="info-name" lang="en">Log: </span>-->
    80  <!-- <span class="info-value log">-->
    81  <!-- <a href="{{log}}" target="_blank" download="log.txt">log.txt <img src="{{static_root}}image/download_log.svg" /></a>-->
    82  <!-- </span>-->
    83  <!-- </div>-->
    84  <!-- {% endif %}-->
    85  <!-- </div>-->

##### 3、修改utils.py 
##### 源码路径：..\site-packages\airtest\aircv\utils.py
    52 nparr = np.frombuffer(pngstr, np.uint8)
    
##### 4、修改logger.py 
##### 源码路径：..\site-packages\airtest\utils\logger.py
    10 # formatter = logging.Formatter(
    11 #     fmt='[%(asctime)s][%(levelname)s]<%(name)s> %(message)s',
    12 #     datefmt='%I:%M:%S'
    13 # )
    14 #额外新增
    15 LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
    16 from colorlog import ColoredFormatter
    17 formatter = ColoredFormatter(LOGFORMAT)
    
### 目录讲解
##### 1、case
>   存放所有被执行用例py文件，以test_*.py、*_test.py开头
    
    指定某个模块 pytest test_module.py
    指定某个目录及其子目录的所有测试文件 pytest testcase
    指定某个某块的某个方法 pytest test_module::test_function
    指定执行某模块的某个类中的某个用例 用“::”分割 pytesy test_model.py::test_class::test_method
    
    比如：case/home 存放首页相关测试用例
    
##### 2、case/__init__.py
>用例执行公共文件，主要使用copy_result_html装饰器将allure与airtest集成，每条用例至少需要增加如下两个装饰器，且html参数字符串必须一样，见下面实例：

###### 登录用例：
    @allure.feature("登录功能归属模块名称")
    @allure.story("登录用例简单描述")
    @allure.title("登录用例名称")
    @allure.descript("登录描述")
    @allure.link("login.html", name="登录")
    @copy_result_html("login.html")
    def test_login():
        setp()
###### 注册用例：  
    @allure.feature("注册功能归属模块名称")
    @allure.story("注册用例简单描述")
    @allure.title("注册用例名称")
    @allure.descript("注册描述") 
    @allure.link("register.html", name="注册")
    @copy_result_html("register.html")
    def test_register():
        setp()

##### 3、case/conftest.py
    pytest自带公共模块，所有同目录测试文件运行前都会执行conftest.py文件

##### 4、case/common.py
    编写用例使用的公共模块，额外自定义公共方法
    
##### 5、case/template
    存放所有用例执行中使用到的图片，用于airtest定位
  
##### 6、case/page_object
    根据不同页面或不同功能存放操作步骤  
          
##### 7、pytest.ini
    pytest自带公共配置文件，执行脚本时首先加载该文件里面的配置项
    
>   pytest使用文档：https://docs.pytest.org/en/latest/_modules/_pytest/python.html

##### 8、config.py
    配置文件，主要用于管理当前项目报告

##### 9、main.py
    程序主入口，如果以下四种方式不能满足你的需求，请额外扩展脚本
>执行方式一，对case路径下所有测试文件进行执行：

    casepath = os.path.join(base_dir, 'case')
    main(casepath)
>执行方式二，对case路径下home路径所有测试文件进行执行：

    casepath = os.path.join(base_dir, 'case'，'home')
    main(casepath)
>执行方式三，只执行case路径下home路径下test.py中用例：

    casepath = os.path.join(base_dir, 'case'，'home'，'test_py')
    main(casepath)
    
>执行方式四，只执行case路径下home路径下test.py中指定方法：

    casepath = os.path.join(base_dir, 'case'，'home'，'test_py::test_method')
    main(casepath)
    
##### 10、allure-report
    报告路径，存放airtest+pytest+allure集成后报告，使用方式：
    1、直接pycharm打开index.html【通过open in browser方式打开】
    2、cmd命令行执行：allure open index.html
    
### 注意事项
>1、项目路径不能是中文

>2、用例相关文件只能存放于case路径下，可以额外自定义二级目录