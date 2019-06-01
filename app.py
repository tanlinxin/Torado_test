import tornado.web
from tornado.options import define,options

from handlers.main import IndexHandler,ExploreHandler,PostHandler

'''
端口运行变换，使用options
'''
define('port',default='8000',help='Listening port', type=int)
define('debug',default='True',help='Debug mode', type=bool)

class Application(tornado.web.Application):
    def __init__(self,debug=False):
        handlers = [
            (r'/', IndexHandler),
            (r'/explore',ExploreHandler),
            (r'/post/(?P<post_id>[0-9]+)',PostHandler),
        ]
        settings = dict(
            debug=debug,
            template_path='templates',
            static_path='statics',
        )
        super().__init__(handlers,**settings)




if __name__ == '__main__':
     tornado.options.parse_command_line()
     application = Application(debug=options.debug)
     application.listen(options.port)
     print('Serve port on start {}'.format(str(options.port)))
     tornado.ioloop.IOLoop.current().start()