import os
import pytest
pytest.mian()  #启动框架
os.system('allure generate ./report/temp -o ../report/html --clean')   #生成测试报告