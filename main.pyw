#coding=utf8
import tornado.web
import tornado.wsgi
import os
import io
import sys
import time

from tornado.iostream import BaseIOStream
from tornado.ioloop import IOLoop
from glob import glob
from threading import Thread
from window import ServerGUI


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

global SERVER_CONTINUE
def callback():
    print('run callback')
    SERVER_CONTINUE = True
    while SERVER_CONTINUE:
        time.sleep(100)
    print('stopping server')
    os.chdir(path)
    os.system('stop_nginx')
    IOLoop.current().stop()
    print('Server shutdown.')


def start_server():
    app.listen(8888)
    os.chdir(path)
    os.system('start_nginx')
    # IOLoop.current().add_callback(callback)
    ioloop_thread = Thread(target=IOLoop.current().start)
    ioloop_thread.start()
    print ('start server')


def stop_server():
    SERVER_CONTINUE = False
    print('SERVER_CONTINUE to False.')
    print('stopping server')
    os.chdir(path)
    os.system('stop_nginx')
    IOLoop.current().stop()
    print('Server shutdown.')


def main():
    print('Press Ctrl + C to stop the server.')
    try:
        app.listen(8888)
        os.chdir(path)
        os.system('start_nginx')
        IOLoop.current().start()
    except KeyboardInterrupt:
        os.chdir(path)
        os.system('stop_nginx')
        IOLoop.current().stop()
        print('Server shutdown.')
    print("end")


if __name__ == '__main__':
    window = ServerGUI()
    window.setStart(start_server)
    window.setStop(stop_server)
    window.mainloop()
