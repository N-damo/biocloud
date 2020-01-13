conda ceate -n django#创建虚拟环境
#####################
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/#更改conda源
conda config --set show_channel_urls yes
######################
conda install mysql
##################
创建root用户
mysql -u root
　　mysql> use mysql;
　　mysql> UPDATE user SET Password = PASSWORD('newpass') WHERE user = 'root';
　　mysql> FLUSH PRIVILEGES; 
##################
python3 -m pip install django==2.2
####################
#mysqlclient替换为pymysql
#edit python3.6/site-packages/django/db/backends/mysql/operations.py decode->encode
#python3.6/site-packages/django/db/backends/mysql/base.py 注释掉version<判断
##################
Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)
内容如下：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com #修改pip源
#####################
python3 -m pip install django-simple-captcha # 安装字符验证
python3 -m pip install pymysql
python3 -m pip install jinja2
python3 -m pip install seaborn