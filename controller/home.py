# coding=utf-8

'''
@license LiXiangping
@version: 1.0
@email: 752070569@qq.com
@author: LiXiangping
@description: 管理登录登出
@date: 2018/03/26
'''  

import tornado.web
from base import BaseHandler


class IndexHandler(BaseHandler):
	pass




class LoginHandler(BaseHandler):
	'''验证登录'''

	def get(self):
		username = self.get_argument('username')
		passwd = self.get_argument('password')
		


