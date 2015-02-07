#coding=utf8
import tornado.web
import tornado.wsgi
import os
import io
import sys

from tornado.iostream import BaseIOStream
from tornado.ioloop import IOLoop
from glob import glob


path = os.getcwd().decode('big5')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        os.chdir(os.path.join(path, 'file'))
        filelist = glob(u'*.*')
        self.render('front.html',filelist=filelist)


settings = {
    'static_path': os.path.join(path, 'static'),
    'template_path'  : os.path.join(path, 'static/templates'),
}


app = tornado.web.Application([
    (r'/', MainHandler),
],**settings)


def main():
    print('Press Ctrl + C to stop the server.')
    try:
        app.listen(8888)
        os.chdir(path)
        os.system('start_nginx')
        def callback():
            print(5);
        IOLoop.current().add_callback(callback)
        IOLoop.current().start()
    except KeyboardInterrupt:
        os.chdir(path)
        os.system('stop_nginx')
        IOLoop.current().stop()
        print('Server shutdown.')
    print("end")


if __name__ == '__main__':
    main()
