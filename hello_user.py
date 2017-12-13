import tornado.ioloop
import tornado.web

class HelloUserHandler(tornado.web.RequestHandler):
    def get(self):
	user = self.get_argument('username')
	write_str = "Hello, " + user
	self.write(write_str)

if __name__ == "__main__":
    handler_mapping = [(r'/hello', HelloUserHandler),]
    app = tornado.web.Application(handler_mapping)
    app.listen(8006)
    tornado.ioloop.IOLoop.current().start()

