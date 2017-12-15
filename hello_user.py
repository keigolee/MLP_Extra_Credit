import tornado.ioloop
import tornado.web

class HelloUserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('user')
        write_str = "Hello, " + username
        self.write(write_str)

if __name__ == "__main__":
    handler_mapping = [(r'/hello', HelloUserHandler),]
    app = tornado.web.Application(handler_mapping)
    app.listen(7777)
    tornado.ioloop.IOLoop.current().start()
