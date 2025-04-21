import logging.handlers

class GetLogger:
    #设置一个单例
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            #创建logger对象
            cls.logger = logging.getLogger()
            #设置日志级别
            cls.logger.setLevel(logging.INFO)
            #获取处理器 控制台
            # sh = logging.StreamHandler()
            #获取处理器 文件
            th = logging.handlers.TimedRotatingFileHandler(filename=r'D:/web测试/day09_pytest/log/log.txt',
                                                           when='M',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8'
                                                           )
            #获取格式器
            fm = logging.Formatter('%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
            #将格式器加入处理器
            # sh.setFormatter(fm)
            th.setFormatter(fm)
            #将处理器加入日志器
            # cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger

if __name__ == '__main__':
    logger = GetLogger.get_logger()
    logger.error('error message')
    logger.info('info message')


