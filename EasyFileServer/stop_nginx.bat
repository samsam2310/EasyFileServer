@echo off
cd nginx
nginx.exe -s stop
taskkill /IM nginx.exe /F
cd ..