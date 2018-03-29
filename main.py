# coding=utf-8

'''
@license LiXiangping
@version: 1.0
@email: 752070569@qq.com
@author: LiXiangping
@description: 使用tornado搭建的安防网站模板
@date: 2018/03/26
'''

from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado import ioloop
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import handler
import config
from model.config import database_config
from model.models import DbBase


def tornado_main():
	''' 启动tornado监听访问 '''
	app = Application(handler.handlers)
	server = HTTPServer(app)
	server.listen(config.config['port'])
	ioloop.IOLoop.instance().start()


def db_main():
	'''数据库连接、升级、降级测试'''

	engine = create_engine(database_config['engine_url'])
	DbBase.metadata.create_all(engine)
	print('db end!')


if __name__ == '__main__':
	db_main()
