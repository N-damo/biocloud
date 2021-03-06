# 云平台使用手册


## linux系统下测试成功，windows下可能出现数据卷挂载失败  
## Dependence
* 1.Docker: version 18.09.2, build 6247962  
    >note: docker hub mirror http://hub-mirror.c.163.com
* 2.git
## Start  
step1:  
创建数据卷容器app_data,挂载nginx、supervisord、uwsgi配置文件，挂载mysql目录以及Keygene中工程目录和工程中media目录  
`docker run -v $PWD/uwsgi.ini:/home/docker/code/uwsgi.ini -v $PWD/supervisor-app.conf:/etc/supervisor/conf.d/supervisor-app.conf -v $PWD/nginx-app.conf:/etc/nginx/sites-available/nginx-app.conf -v $PWD/Keygene/:/home/docker/code/Keygene -v $HOME/mysql:/var/lib/mysql --name app_data ubuntu:18.04`


step2:  
**启动mysql和redis数据库**，其中mysql挂载$HOME/mysql  
`docker run -itd -p 6379:6379 --name redis redis:5.0.7`

`docker run -v $HOME/mysql:/var/lib/mysql -itd --name mysql -p 3306:3306 -e  MYSQL_ROOT_PASSWORD=123456 mysql:8.0.18`    
>mysql每次创建新容器后需要修改配置,修改后可远程登录；若不远程登录，则不需要以下修改命令：  
>进入mysql容器;  
>docker exec -it mysql bash  
>登录mysql; 
>mysql -u root -p  
>创建wgs，已创建就忽略这一步;  
>create database wgs;  
>修改远程登录设置;  
>ALTER USER 'root'@'%' IDENTIFIED WITH   mysql_native_password BY '123456';
>刷新;  
>flush privileges;  
>退出;  
>exit  


step3:
创建app容器，挂载app_data，链接mysql和redis数据库，同时启动supervisord进程监听  
如果还未构建django镜像,先运行下面命令build django镜像:  
`git clone https://github.com/N-damo/Keygene.git ;`    
`cd Keygene ;`    
`docker build -t django:v1 .`  
`cd Keygene ;`  
`python3 manage.py collectstatic`  
`cd .. `  
产生静态文件时需要重新运行**collectstatic**命令

build完后再创建app容器  
`docker run --volumes-from app_data -itd -p 80:80 -p 8000:8000 --link mysql:mysql --link redis:redis --name app django:v1`  
**注：如果已创建mysql和redis容器，但提示mysql和redis还未启动，那么启动对应数据库，即docker start mysql redis**


step4:  
局域网访问：
>连接WiFi：    
>WiFi密码：   
>访问:  