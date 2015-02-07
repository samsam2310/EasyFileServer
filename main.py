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
    def get_content_type(self):
        return 'application/octet-stream'


path = os.path.dirname(__file__)

settings = {
    'static_path': os.path.join(path, 'static'),
    'template_path'  : os.path.join(path, 'static/templates'),
    # 'debug':True,
}


app = tornado.web.Application([
    (r'/file/(.*)', FileHandler, {'path': os.path.join(path, 'file')} ),
    (r'/', MainHandler),
],**settings)

def main():
    print('Press Ctrl + C to stop the server.')
    try:
        app.listen(80)
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()
        print('Server shutdown.')

if __name__ == '__main__':
    main()
