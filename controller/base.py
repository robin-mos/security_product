# coding=utf-8


import tornado.web

class BaseHandler(tornado.web.RequestHandler):
	'''[summary]
	
	[description]
	
	Extends:
		tornado.web.RequestHandler
	'''

	def session(self):
		
		
