import tornado.web
import tornado.wsgi
import os
import io

from tornado.iostream import BaseIOStream
from tornado.ioloop import IOLoop
from glob import glob


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        os.chdir(os.path.join(os.path.dirname(__file__), 'file'))
        filelist = glob(u'*.*')
        self.render('front.html',filelist=filelist)


class FileHandler(tornado.web.StaticFileHandler):
    pass
    # def get_content_type(self):
    #     return 'application/octet-stream'


path = os.path.dirname(__file__)

settings = {
    'static_path': os.path.join(path, 'static'),
    'template_path'  : os.path.join(path, 'static/templates'),
    'cookie_secret': '__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__',
    'login_url': '/login',
    'xsrf_cookies': True,
    'debug':True,
}


app = tornado.web.Application([
    (r'/file/(.*)', FileHandler, {'path': os.path.join(path, 'file')} ),
    (r'/', MainHandler),
],**settings)


def main():
    app.listen(80)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
