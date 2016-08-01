环境安装
=======
环境依赖包(必须，否则程序无法正常运行)： Python3.3/tornado，Mysql，mysql-connector-python，sqlalchemy
    安装命令：
        Mysql 5.5.37: apt-get install mysql-server
        Mysql connector/python 2.0.1: pip3 install mysql-connector-python
        tornado-4.0.2:（要先去官网下载安装包，再解压安装）
            wget https://pypi.python.org/packages/source/t/tornado/tornado-4.0.2.tar.gz;tar -xzvf tornado-4.0.2.tar.gz;cd tornado-4.0.2;sudo python3 setup.py install
        sqlalchemy 0.9: pip3 install sqlalchemy

其他依赖包（非必须）：pytest，alembic，Nginx（不装nginx程序也能运行，不过强烈建议安装）
    安装命令：
        py.test: pip3 install pytest
        自动数据库迁移：alembic 0.6.7: pip3 install alembic

