from dal import models as models
import tornado.web
import tornado.ioloop
#from  handlers  import customer
from tornado.options import options, define

import tornado.wsgi
# import gevent.wsgi
# import pure_tornado

import os

from urls import handlers
from dal.db_configs import DBSession

define("debug", default=0, help="debug mode: 1 to open, 0 to close")
define("port", default=8887, help="port, defualt: 8888")
settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"static_url_prefix": "/static/",
	"template_path": os.path.join(os.path.dirname(__file__), "templates"),
	"cookie_secret": "shabianishishabianishi",
	"xsrf_cookies": False
}

class Application(tornado.web.Application):
	def __init__(self):
		settings["debug"] =  bool(options.debug)
		super().__init__(handlers, **settings)

def main():
	models.init_db_data()
	tornado.options.parse_command_line()
	application = Application()
	application.listen(options.port)
	if options.debug:debug_str = "in debug mode "
	else:debug_str = "in production mode"
	print("running yizhan {0} @ {1}...".format(debug_str,options.port))
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
	
							