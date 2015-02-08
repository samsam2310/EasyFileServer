import py2exe

from distutils.core import setup
from glob import glob 


setup(windows=['main.pyw',{"script":"main.pyw", "icon_resources":[(1, "icon.ico")]}])