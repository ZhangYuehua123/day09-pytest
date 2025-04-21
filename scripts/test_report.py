import time
from tool.HTMLTestRunner import HTMLTestRunner
import unittest

suite = unittest.TestLoader().discover(r"D:/web测试/day09/scripts/", pattern="*login.py")

#定义报告存放路径及文件名称
report_dir =r"D:\web测试\day09\report\{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))

#获取报告存放文件流，并实例化HTMLTestRunner类，执行run方法
with open(report_dir,"wb") as f:
    HTMLTestRunner(f,verbosity=2,title="web自动化测试报告").run(suite)
