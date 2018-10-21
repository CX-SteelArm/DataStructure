Mysql
==================

本文为实验楼平台上Mysql基础课程的学习笔记

#目录
-----------------

## 第一课

-------------

**数据库的概念和安装、查看**

* 安装前的检查
`service sudo mysql start`检测是否安装有mysql

* Ubuntu安装Mysql
`sudo apt-get install mysql-server`
`sudo apt-get install mysql-client`
`sudo netstat -tap | grep mysql`检查是否安装并启动成功

    打开sql： mysql -u root
    查看： show databases;
    连接: use *databasename*;
    查看表： show tables;
    退出： quit/exit 

##  第二课

-------------

**创建数据库和表、数据插入表中**

* 创建数据库 `create database dbname;`
* 创建表

    create table tbname(
        colA dataType(length),
        colB dataType(length),
        colC dataType(length)
    );

* 删除表 `drop database dbname;`

数据类型：

|数据类型|描述|
|:--:|:--:|
|int|整数4|
|float/double|浮点数4/8|
|enum/set|单选/多选|
|date/time/year|日期3/时刻3/年份1|
|char/varchar|定长/变长字符串(0-255)|

* 插入数据 `insert into tbname values(XX, XX, XX)` 或者
    `insert into tbname(id, name) values(XX, XX)` 未插入的项为Null
* 查看表 `select * from tbname`

## 第三课

-------------

**数据库的约束**

sql约束：

|限制|名称|
|:--:|:--:|
|主键|primary key|
|默认值|default|
|唯一|unique|
|外键|foreign key|
|非空|not null|

[CSDN讲解](https://blog.csdn.net/w_linux/article/details/79655073)

* 字段约束和表级约束

    mysql> create table t_user(
    -> id int(10),
    # 直接在后方写出来，字段约束
    -> name varchar(32) not null,
    -> email varchar(128),
    # 表级约束
    -> unique(name,email),
    # 用constraint可以给表级约束起名字
    -> constraint t_user_email_unique unique(email)
    -> );

* 主键
primary key：一张表应该有主键字段，如果没有，表示该表无效
主键值唯一且不可重复(not null & unique)，会默认添加索引--index
可以用表级约束定义复合主键，可以指定auto_increment表示键值自增加

* 外键
只能用表级约束定义外键
外键值可以为null
外键字段必须有unique属性
步骤：创建先创建父表 --> 插入数据先插入父表，再插入子表

foreign key(key_in_this_tb) references other_tb(other_key)

例子：建立一个简单的分数数据库
```sql
create database gradesystem;
use gradesystem;
create table student(
    sid int(2) primary key auto_increment,
    sname char(20),
    gender enum("male", "female")
); 

create table course(
    cid int(2) auto_increment,
    cname char(20),
    primary key(cid)
);

create table mark(
    mid int(2) primary key auto_increment,
    sid int(2),
    cid int(2),
    foreign key(sid) references student(sid),
    foreign key(cid) references course(cid),
    score int(3)
);

insert into student(sname, gender) values("Tom", "male");
insert into student(sname, gender) values("Jack", "male");
insert into student(sname, gender) values("Rose", "female");

insert into course(cname) values("math");
insert into course(cname) values("physics");
insert into course(cname) values("chemistry");

insert into mark(sid, cid, score) values(1,1,80);
insert into mark(sid, cid, score) values(2,1,85);
insert into mark(sid, cid, score) values(3,1,90);
insert into mark(sid, cid, score) values(1,2,60);
insert into mark(sid, cid, score) values(2,2,90);
insert into mark(sid, cid, score) values(3,2,75);
insert into mark(sid, cid, score) values(1,3,95);
insert into mark(sid, cid, score) values(2,3,75);
insert into mark(sid, cid, score) values(3,3,85);
```
* 可以将sql语句写入`.sql`文件中，然后在mysql命令行使用`source XX.../XX.sql`的方式新建和导入数据库

## 第四课

-------------

**数据库的基本查询语句**

* select基本语法
`select 要查询的列 from 表名 where 限制条件`
`select database();` 查询现在使用的是哪个数据库，如果没有则返回null

where限制条件：
1. 大于小于等于
2. or | and | between and
3. in | not in
4. like(通配符类型: _ 代表一个未指定字符 % 代表不定个位指定字符)

结果排序：
order by命令
asc：升序    desc：降序

内置函数和计算：
内置count计数，sum求和，avg平均，max和min函数
`select max(salary) as max, min(number) from employee`

子查询：嵌套的sql语句

连接查询：
`join on`语句用来连接两个表


## 第五课

-------------

**数据库的基本修改语句**

* 重命名 
`rename table 原名 to 新名字;`
`alter table 原名 rename 新名字;`
`alter table 原名 rename to 新名字;`

* 删除表
`drop table tbname`

* 改变
增加一列：`alter table tbname add 名称 数据类型 约束条件`
增加`after someCol`可以将其增加到`someCol`列之后，使用`first`可以将增加的列作为第一列

删除一列：`alter table tbname drop column colname`
删除一行：`delete from 表名 where 条件`

重命名一列：`alter table tbname change 原列名 名称 数据类型 约束条件`

改变数据类型：`alter table 表名 modify 列名 新数据类型`



* 修改
`update 表名 set XX=..,YY=.. where 条件`
把更改部分放在XX,YY中

## 第六课

-------------

**其他基本操作**

* 建立索引(在数据量大时可以大大加快查询速度)
`alter table tbname add index indexname(colname)`
`create index indexname on tablename(colname)`

* 视图(依照已经存在的数据构建一个虚拟的表)
`create view xxx(a,b,c) as select name, age from atable`

* 导入
`load data infile '文件路径' into table 表名字`
需要注意在Ubuntu中文件需要放在`/var/lib/mysql-files/`文件夹下

* 导出
`select *(或列1,列2等) into outfile '文件路径' from 表名字`

* 备份
`mysql -u root 数据库名>备份文件名`
`mysql -u root 数据库名 表名字>备份文件名`

* 恢复
将备份中的大于号换成小于号就是恢复(还原)

# 以下是Mysql手册部分，涉及的内容较为全面

## 第七课

-------------

**Mysql服务与安装**

输入查询：
`select version(), current_date;`
`select 3+4;`
`select now();`
使用`\c`来取消一条语句的执行
注意`'>` `">` 等输入提示符的区别

## 第八课

-------------

**创建并使用数据库**

* 创建表
```sql
create table pet(
    name varchar(20),
    owner varchar(20),
    species varchar(20),
    sex char(1),
    birth date,
    death date
);

describe pet; #显示pet表各列的具体信息(数据类型、限制等)
```
* 将数据加载到表中
`mysql> LOAD DATA INFILE '文件路径' INTO TABLE pet LINES 
    -> TERMINATED BY '\r\n';`在windows中需要第二行的语句

`insert into pet values(XX, YY, ZZ)` 是直接添加的做法

* 修改数据
方法1：`delete from tbname; load data infile filename into table tbname`
方法2：`updata tbname set xx=yy,zz=ww where ...`

* 日期计算

* NULL值操作
null与数据的计算结果为null，使用`is null`和`is not null`可以判断是否为null

* regexp

* group by检索，返回对象不重复的元素(组)个数个值
```sql
mysql> SELECT species, sex, COUNT(*) FROM pet
    -> WHERE species = 'dog' OR species = 'cat'
    -> GROUP BY species, sex; #相当于选择了两列进行操作
```
* count(\*)统计数目`select sex,count(*) from pet group by sex;`

## 第九课

-------------

**数据库基本查询操作**

* 查询最大值所在的行
```sql
mysql> SELECT *
    -> FROM   shop
    -> WHERE  price=(SELECT MAX(price) FROM shop);

# 或者

mysql> SELECT article, dealer, price
    -> FROM shop
    -> ORDER BY price DESC
    -> LIMIT 1;

# limit可以限制输出几个值
```

* 定义变量
`set @t1=3,@t2=@t1+3;` 或者
`select @t1:=(@t2:=4)+3;` 注意等号的不同