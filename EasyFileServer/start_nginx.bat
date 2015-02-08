@echo off
cd nginx
taskkill /IM nginx.exe /F
start nginx.exe
cd ..