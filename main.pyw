# -*- coding: utf-8 -*-
import tornado.web
import tornado.wsgi
import os
import sys

from glob import glob
from tornado.ioloop import IOLoop
from threading import Thread
from window import ServerGUI


path = os.getcwd().decode('big5')
file_path = os.path.join(path, u'file')


if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('big5')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        os.chdir(file_path)
        filelist = glob(u'*.*')
        self.render('front.html',filelist=filelist)


settings = {
    'static_path': os.path.join(path, 'static'),
    'template_path'  : os.path.join(path, 'static/templates'),
}


app = tornado.web.Application([
    (r'/', MainHandler),
],**settings)


def start_server():
    print('Starting server...')
    os.chdir(path)
    with open('nginx/conf/nginx.conf.python','r') as nginx_conf:
        conf = nginx_conf.read()
        with open('nginx/conf/nginx.conf','wb') as user_conf:
            user_conf.write(conf % file_path.encode('utf-8'))
    os.system('start_nginx')
    ioloop_thread = Thread(target=IOLoop.current().start)
    ioloop_thread.start()
    print ('Server running successful!')
    print('Please put your file in "%s"' %file_path)


def stop_server():
    print('Stopping server...')
    os.chdir(path)
    os.system('stop_nginx')
    print('Stopping nginx...')
    IOLoop.current().stop()
    print('Server shutdown.')


def set_file_path(path_f):
    global file_path
    file_path = path_f


if __name__ == '__main__':
    window = ServerGUI(start_server,stop_server,set_file_path,app)
    window.mainloop()
