## sql常用方法总结

**数据库中最基本的单元: <font color=red>表(table)</font>**

> * 数据库中是以表格的形式表示数据的，任何一张表都有行和列：
>  * 行(row)： 被称为数据/记录
>   * 列(column):	被称为字段，每个字段都有字段名、数据类型、约束等条件
>
> * 每一行代表一行数据，每一列为字段约束 。

------
> **<font color=red>*</font>sql **语句不区分大小写
>
> **sql执行先后顺序：**
>
> > **(8)**SELECT	**(9)**DISTINCT	**(11)**  <Top NUM>   <select list>            
> >
> > **(1)**FROM	[left_table] 
> >
> > **(3)**<join_type> JOIN <right_table>
> >
> > **(2)**  ON <join condition> 
> >
> > **(4)** WHERE <where condition>
> >
> > **(5)**GROUP BY <group_by_list>
> >
> > **(6)**WITH <CUBE | RollUP>
> >
> > **(7)**HAVING <having_condition>
> >
> > **(10)**ORDER　BY <order_by_list>

## 数据表：

EMP表：
| EMPNO | ENAME | JOB  | MGR  | HIREDATE | SAL  | COMM | DEPTNO |
| ----- | ----- | ---- | ---- | -------- | ---- | ---- | ------ |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-04-19 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-05-23 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |

DEPT表：
| DEPTNO | DNAME | LOC  |
| :----: | :---: | :--: |
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | dallas |
|     30 | SALES      | CHICAGO  |
|     40 | OPERATIONS | boston |

SALGRADE表(多对多关系表)：
| GRADE | LOSAL | HISAL |
| :------: |: -----: | :----: |
|     1 |   700 |  1200 |
|     2 |  1201 |  1400 |
|     3 |  1401 |  2000 |
|     4 |  2001 |  3000 |
|     5 |  3001 |  9999 |

## 1. 查询(select)

```sql
-- 1. 查询一个字段
 SELECT 字段名 from 表名;

-- 2. 查询多个字段, 字段之间用逗号隔开
SELECT 字段一,字段二 from 表名;

-- 3. 查询所有字段，实际开发中不要使用，效率低可读性差
SELECT *(所有字段) from 表名;
```

### 1.1 查询的列起别名

```sql
-- 1. 使用as
SELECT 字段名 as 字段别名 FROM 表名;

-- 2. 不能有空格
SELECT 字段名 字段别名 FROM 表名;

-- 3. 使用单引号' '包裹有空格的字段别名
SELECT 字段名 '字段别名' FROM 表名;
```

### 1.2  列数值运算

```sql
-- 查询计算年薪
SELECT sal*12 as sal FROM 表名;
```

### 1.3 条件查询(where)

**条件查询需要用到where语句， where 必须放到from 语句表的后面，支持以下运算符：**

| 运算符 | 含义 |
| :----: | :--: |
|   =    | 等于 |
|<> 或 !=|不等于|
|<|小于|
|<=|小于等于|
|>|大于|
|>=|大于等于|
|between...and...|两个值之间，等同于 <font color=red>>= and <=</font>|
|is null|为null (is not null 不为空)|
|and|并且|
|or|或者|
|in|包含，相当于多个or(not in 不在这个范围内)|
|not|not 可以取非，主要用在**is或in**中|
|like|like 称为模糊查询，支持%或下划线(_)匹配<br />%：匹配任意个字符<br />下划线：一个下划线只匹配一个字符|

```sql
SELECT 字段1,字段2 FROM 表名 WHERE 查询条件;


-- 1. 查询薪资大于800 的员工
SELECT ENAME FROM EMP WHERE SAL > 3000;


-- 2.【BETWEEN...AND区间查询】, 查询薪资在900到3000的员工 
SELECT ENAME, SAL FROM EMP WHERE sal between 900 and 3000; 
SELECT ENAME, SAL FROM EMP WHERE sal >= 900 and SAL<=3000;
-- *使用between...and时遵循左小右大,闭区间包括两端的值


-- 3.【OR或查询】, 查询部门编号为20或30的工作
SELECT ENAME, SAL, JOB FROM EMP WHERE DEPTNO=20 or DEPTNO=30;


-- 4.【and和or混合使用】, 查询薪资大于2500, 部门编号为10或20
SELECT * from EMP WHERE SAL > 2500 AND (DEPTNO = 10 or DEPTNO=20);
-- *and和or同时出现，and的优先级比or高


-- 5.【NULL用法】, 查询字段COMM字段为空的数据
SELECT ENAME, JOB, SAL from EMP WHERE COMM is NULL;
-- *注意：在数据库中null不能使用等号进行衡量,需要使用is NULL
-- 因为数据库中的null代表什么也没有,它不是一个值。


-- 6.【IN查询】, 查询工作岗位是mangager和salesman的员工
SELECT  EMPNO, ename, job FROM EMP WHERE job IN('manager', 'SALESMAN');
-- *注意： in不是一个区间。in后面跟的是具体的值。


-- 7.【LIKE模糊查询】, 根据匹配规则进行查询
-- 查找员工名称以 S 开始的员工信息
SELECT  * FROM EMP WHERE ENAME LIKE "S%"; 
-- 查找员工名称以 S 结尾的员工信息
SELECT  * FROM EMP WHERE ENAME LIKE "%S";
-- 查找员工名称中包含 O 的员工信息
SELECT  * FROM EMP WHERE ENAME LIKE "%O%"; 
-- 查询员工名称第二个字符是 O 的员工信息
SELECT  * FROM EMP WHERE ENAME LIKE "_O%";
-- 查询工作名称中包含 _ 的员工信息
SELECT  * FROM EMP WHERE JOB LIKE "%\_%";
-- *注意：因为_是一个匹配字符, 使用 \ 进行转义
```

### 1.4 排序(order by)

<font color=red>*</font>：排序需要用到order by语句,  order by 必须放到from 语句表的后面,  默认是<font color=red>升序</font>

```sql
-- 1.查询员工工资
SELECT  * FROM EMP ORDER BY sal;
 *注意：默认是升序


-- 2.查询员工工资, 指定降序
SELECT  * FROM EMP ORDER BY sal DESC;   //升序是 ASC


-- 3.多个字段排序, 薪资相同的情况下再加一个入职时间进行排序 
SELECT  * FROM EMP ORDER BY sal, HIREDATE;
 

-- 4.根据查询字段的位置进行排序，按照查询字段的JOB进行排序
SELECT  ENAME, EMPNO, JOB, HIREDATE FROM EMP ORDER BY 3;
-- 不建议开发中使用, 查询字段列随时会发生变化
```

### 1.5 分页(limit)

limit作用：将查询结果集的一部分取出来, 通常在分页查询当中使用。

- 完整用法 ：limit [startIndex, [length]]  startIndex是起始下标，length是长度。
- 起始下标从0开始。
- 缺省用法：limit 5;  取前5条.

```sql
-- limit 分页
-- 取前8条数据
SELECT ENAME, JOB, SAL FROM `EMP` ORDER BY SAL DESC LIMIT 0,8; 
-- 执行顺序, msyql是在order by之后执行
```

每页显示pageSize条:

* 记录: 第pageNo页：limit (pageNo - 1) * pageSize , pageSize

### 1.6 函数

#### 1.6.1 单行处理函数

* 单行处理函数的特点：一个输入对应一个输出

  * 和单行处理函数相对的是：多行处理函数。（多行处理函数特点：多个输入，对应1个输出！）

__常见的单行处理函数__：

| 函数  | 含义             |
| :---: | :--------------: |
| lower | 字符串转换成<font color=red>小</font>写 |
|upper|字符串转换成<font color=red>大</font>写|
|substr|取子串（substr(被截取的字符串， 起始下标，截取的长度)）<br />注意：substr的起始下标从<font color=red>1</font>开始，没有0|
|concat|字符串拼接 <br/> concat(字段1/字符串1, 字段2/字符串2, ...)|
|length|获取长度|
|trim|去空格|
|str_to_date|将字符串转换成日期|
|date_format|格式化日期|
|format|设置千分位|
|round|四舍五入， round(数值，保留小数位的整数值)|
|rand|生成随机数|
|ifnull|可以将null转换成一个具体值|

```sql
-- 1. lower 转换小写
SELECT LOWER(ENAME) FROM `EMP`;

-- 2. upper 转换大写
SELECT UPPER(LOC) FROM `DEPT`;

-- 3. substr 取子字符串
-- 找出ENAME字段前两个字母是AD的员工
SELECT ENAME, JOB FROM `EMP` WHERE SUBSTR(ENAME, 1, 2) = 'AD';
-- 模糊查询也可以做到
SELECT ENAME, JOB FROM `EMP` WHERE ENAME LIKE "AD%"

-- 4. concat 字符换拼接
SELECT CONCAT(ENAME, "_", JOB) FROM `EMP`;
-- ENAME字段值的首字母小写
SELECT CONCAT(SUBSTR(LOWER(ENAME), 1, 1), SUBSTR(ENAME, 2, LENGTH(ENAME) - 1))  FROM `EMP`;

-- 5. length 获取长度
SELECT LENGTH(JOB) name_length from `EMP`;

-- 6. trim 去除空格
SELECT * from `EMP` WHERE JOB = TRIM("  CLERK");

-- 7. str_to_date 字符串转换日期

-- 8. date_format 格式化日期 

-- 9. format 设置千分位
SELECT FORMAT(MGR, 3) FROM `EMP`;

-- 10. round 四舍五入
SELECT ENAME, ROUND(SAL, 1) sal FROM `EMP`;

-- 11. rand 生成随机数
-- 100以内的随机数向下取整， FLOOR表示向下取整，向上取整是CEILING
SELECT FLOOR(rand(10)*100) FROM `EMP`;

-- 12. ifnull 可以将null转换成一个具体值
-- ifnull是空处理函数，专门处理空的。
-- 在所有数据库当中，只要有NULL参与的数学运算，最终结果就是NULL。
-- ifnull函数用法: ifnull(数据, 需要替换的值)
-- 如果数据为NULL的时候, 把这个数据结构当做替换的值
SELECT ENAME, FORMAT(IFNULL(SAL, '')+IFNULL(COMM, ''), 3) 薪资 FROM `EMP`;

-- 13. case...when...then...when...then...else...end(了解)
-- 相当于if判断操作
-- 语法: SELECT 字段1, (CASE 字段2 WHEN '字段2的条件' THEN 字段操作 WHEN '字段2的条件' THEN 字段操作 ELSE 字段2 END) 别名 FROM `表名`;
SELECT ENAME, JOB, SAL as old_sal,(CASE JOB WHEN 'ANALYST' THEN sal*1.5 WHEN 'CLERK' THEN sal*1.2 ELSE sal END) as new_sal FROM `EMP`;
```

关于7、8 两个日期函数参考：[MySQL的date_format()和str_to_date()](https://mp.weixin.qq.com/s?__biz=MzI2NzM1OTM4OA==&mid=2247498800&idx=1&sn=cf023a4c36a593ae0d0255c1b39bd6db&chksm=ea82b9c3ddf530d5e179b677113be7e2b8c29b6031985da17df19118d50db46d95e658771c75&scene=27) 

#### 1.6.2 多行处理函数

* 分组函数也被称为多行处理函数
* 多行处理函数的特点：输入多行，最终输出一行。

__常见的多行处理函数__

| 函数  | 含义 |
| :---: | :--: |
| count | 计数 |
|sum|求和|
|avg|计算平均值|
|max|最大值|
|min|最小值|

<font color=red>*</font>：分组函数在使用的时候<font color=red>必须先进行分组</font>，然后才能使用。如果你没有对数据进行分组，整张表默认视为一组。

```sql
-- *注意：以下操作都是以一张表为一组
-- 1. count 计数
-- 查看所有员工数
SELECT COUNT(ENAME) name FROM `EMP`;
-- 查看表中所有数据的总行数, 只要有一行数据count则++, 因为每一行记录不可能都是null, 一行数据中有一列不为null, 则这行数据就是有效的。 
SELECT COUNT(*) FROM `EMP`;

-- 2. sum 求和
-- 所有员工工资
SELECT SUM(SAL) name FROM `EMP`;

-- 3. avg 平均值
-- 所有员工总薪资的平均薪资取整
SELECT FLOOR(AVG(SAL)) name FROM `EMP`;

-- 4，max 最大值
-- 所有员工的最大工资
SELECT MAX(SAL) name FROM `EMP`;

-- 5，min 最小值
-- 所有员工的最小工资
SELECT MIN(SAL) name FROM `EMP`;
```

__分组函数在使用的时候需要注意哪些？__

* 1. 分组函数自动忽略NULL, 你不需要提前对null进行处理。
* 2. 分组函数中的count()和count(具体字段有什么区别)？
     * count(具体字段)：表示统计该字段下所有不为NULL的元素的总数。
     * count(*): 统计表当中的总行数。只有一行数据count则++，因为每一行数据不可能都为NULL, 一行数据中有一列不为NULL, 则这行数据就是有效的。

* 3. 分组函数不能直接用在where字句中。

### 1.7 分组查询<font color=red>**</font>

*  分组查询是对数据按照某个或多个字段进行分组 
*  GROUP BY关键字可以将查询结果按照某个字段或多个字段进行分组,字段中值相等的为一组
  * 分组的核心是：在查询SQL中指定分组的列名，然后根据该列的值进行分组，值相等的为一组

  #### 1.7.1 group by

```sql
-- group by 分组
-- 以工作岗位进行分组, 计算岗位的工资总和及平均薪资
select JOB, SUM(sal), AVG(SAL) from `EMP` GROUP BY JOB; 

-- GROUP BY关键字通常与集合函数一起使用,如果GROUP BY不与聚合函数一起使用，那么查询结果就是字段取值的分组情况,字段中取值相同的记录为一组, 且只显示该组的第一条记录
```

<font color=red>*</font>： 在一条select语句中，如果有group by语句的话，select后面只能跟参加分组的字段，以及分组函数，其它的一律不能跟。

#### 1.7.2 联合分组

```sql
-- 查找每个部门，不同工作岗位的最高薪资
select DEPTNO, JOB, MAX(sal) from `EMP` GROUP BY DEPTNO, JOB; 
-- 将DEPTNO,JOB看做一个字段
```

#### 1.7.3  having

* 使用having可以对分完组之后的数据进一步过滤。

* HAVING条件表达式：用来限制分组后的显示，符合条件表达式的结果将被显示 

- having<font color=red>不能单独使用</font>，having不能代替where，having必须和group by联合使用。

```sql
-- 查询部门的最高薪资大于2000的工作岗位
select DEPTNO, JOB, MAX(sal) from `EMP` GROUP BY DEPTNO, JOB HAVING MAX(SAL) > 2000;
-- 优化策略: where 和 having， 优先选择where,where完成不了的再选择having
select DEPTNO, JOB, MAX(SAL) from `EMP` WHERE SAL > 2000 GROUP BY DEPTNO, JOB; 
```
###  1.8 distinct

- distinct 把查询结果去除重复记录
- distinct 只能出现在所有字段的最前方, 语法：` SELECT DISTINCT 列名称 FROM 表名称 `

```sql
-- distinct 去除重复记录
-- 查询岗位
SELECT distinct job from `EMP`;

-- distinct 出现在 job,deptno 两个字段之前，表示两个字段联合起来去重。
select distinct job,deptno from emp;
```

### 1.9 连接查询

- 从一张表中单独查询，称为单表查询
- emp表和dept表联合起来查询数据，从emp表中取员工名字，从dept表中取部门名字。

- 这种跨表查询，多张表联合起来查询数据，被称为连接查询。

- 当两张表进行连接查询，没有任何条件限制的时候，最终查询结果条数，是两张表条数的乘积，这种现象被称为：笛卡尔积现象。`select ename,dname from emp, dept;`

<font color=red>*</font>：通过笛卡尔积现象得出，表的连接次数越多效率越低，尽量避免表的连接次数。

根据表连接的方式分类:

  * 内连接：
    	* 等值连接
    * 非等值连接
    * 自连接

* 外连接：
  * 左外连接(左连接)
  * 右外连接(右连接)
* 全连接(了解)

#### 1.9.1 内连接

- 内连接：（A和B连接，AB两张表没有主次关系。平等的。）
- 内连接的特点：把能够匹配ON后面的条件的数据查询出来。

##### 1）内连接之等值连接

* 语法：select 字段1,字段2 , ... from 表一 别名  join(inner join)  表二 别名 on 条件一 where 条件2    表起别名可以提高查询效率  


```sql
-- 查找员工对应的部门名称
SELECT 
    ENAME, DNAME
FROM 
    `EMP` E
JOIN
	`DEPT` D
on 
	E.DEPTNO = D.DEPTNO;  // 条件是等值关系，所以是等值连接。
```
##### 2）内连接之非等值连接
   ```sql
-- 查找每个员工的薪资等级，要求显示员工名，薪资，薪资等级？
SELECT 
	E.ENAME, E.SAL, S.GRADE 
FROM 
	`EMP` E 
INNER JOIN 
	`SALGRADE` S 
ON 
	E.SAL 
BETWEEN 
	S.LOSAL 
AND 
	S.HISAL;   // 条件不是一个等量关系，所以是非等值连接。
   ```
##### 3）内连接之自连接
* 将一张表看成两张表称为自连接

```sql
-- 查询员工的上级领导，并显示员工名和对应的领导名
SELECT 
	a.ENAME '员工名', b.ENAME '领导名'
FROM
	`EMP` as a 
INNER JOIN
	`EMP` as b
ON
	a.MGR = b.EMPNO;  // 员工的领导编号 = 领导的员工编号,查出匹配上这个条件的所有数据
```

#### 1.9.2 外连接<font color=red>**</font> 

* 在外连接当中，两张表连接产生了主次关系


##### 1）左外连接(左连接)

* 什么是左连接：MySQL LEFT JOIN 会读取左边数据表的全部数据，即使右边表无对应数据。

```sql
-- 以EMP表为左表关联查询DEPT表, 查询部门的员工
SELECT 
	b.ENAME '员工名', a.DNAME '部门'
FROM
	`EMP` as b
LEFT JOIN
	`DEPT` as a
ON
	b.DEPTNO = a.DEPTNO;
```

##### 2）右外连接(右连接)

* 什么是右连接： MySQL RIGHT JOIN 会读取右边数据表的全部数据，即使左边边表无对应数据。 

```sql
-- 以DEPT表为右表关联查询EMP表, 查询部门的员工
SELECT 
	a.ENAME '员工名', b.DNAME '部门'
FROM
	`EMP` as a 
RIGHT JOIN
	`DEPT` as b
ON
	a.DEPTNO = b.DEPTNO;
```

**任何一个左连接都有右连接的写法，任何一个右连接都有左连接的写法。**

#### 1.9.3 全连接

* 全连接就是将 table1 和 table2 的内容完全显示，不管有没有匹配上。  语法：` SELECT column_name(s) FROM table1 FULL OUTER JOIN table2 ON table1.column_name = table2.column_name;  `

#### 1.9.4 多张表查询

语法：

```sql
select 
	...
from
	a
join
	b
on
	a和b的连接条件
join
	c
on
	a和c的连接条件
right join
	d
on
	a和d的连接条件
-- 一个sql中内连接和外连接可以混合,都可以出现
```

```sql
-- 1.查找每个员工的名字, 部门名, 薪资, 薪资等级
SELECT 
	e.ENAME, e.SAL, d.DNAME, s.GRADE '薪资等级'  
FROM
	`EMP` e
JOIN 
	`SALGRADE` s
on 
	e.SAL BETWEEN s.LOSAL and s.HISAL
LEFT JOIN 
	`DEPT` d 
on 
	e.DEPTNO = d.DEPTNO;
	

-- 2.找出每个员工的员工名字, 领导名, 部门名, 薪资, 薪资等级
SELECT 
	e.ENAME '员工', leader.ENAME '领导', e.SAL '薪资', d.DNAME '部门', s.GRADE '薪资等级'  
FROM
	`EMP` e
JOIN 
	`SALGRADE` s
on 
	e.SAL BETWEEN s.LOSAL and s.HISAL
LEFT JOIN 
	`DEPT` d 
on 
	e.DEPTNO = d.DEPTNO
LEFT JOIN
	`EMP` leader
on 
	leader.EMPNO = e.MGR;
```

### 1.10 子查询

* 什么是子查询：select 语句中嵌套的select语句，被嵌套的select语句称为子查询。
* 子查询可以出现在 select后面，from 后面，where 后面。
*  使用子查询必须遵循以下几个规则：
  * 子查询必须括在圆括号中。
  * 子查询不能使用 ORDER BY，不过主查询可以。在子查询中，GROUP BY 可 以起到同 ORDER BY 相同的作用。 
  * 返回多行数据的子查询只能同多值操作符一起使用，比如 IN 操作符。  
  * SELECT 列表中不能包含任何对 BLOB、ARRAY、CLOB 或者 NCLOB 类 型值的引用。 
  * BETWEEN 操作符不能同子查询一起使用，但是 BETWEEN 操作符可以用 在子查询中。  

```sql
select 
	(select XXX)
from
	(select XXX)
where
	(select XXX)
...
```

#### 1.10.1 where 子句中的的子查询

```sql
-- 找出比最低工资高的员工姓名和工资
SELECT ENAME, SAL FROM `EMP` WHERE SAL > (SELECT MIN(SAL) FROM `EMP`);
```

#### 1.10.2 from 后面出现的子查询

* from 后面的子查询可以将子查询的查询结果当作一张临时表。

```sql
-- 查询每个工作岗位的平均薪资以及对应的薪资等级
SELECT 
	t.*, s.GRADE 
FROM 
	(SELECT JOB, AVG(SAL) '平均薪资' FROM  `EMP` GROUP BY JOB) t 
LEFT JOIN 
	`SALGRADE` s
ON 
	t.平均薪资 
BETWEEN s.LOSAL AND s.HISAL;
```

#### 1.10.3 select 后面出现的子查询

```sql
-- 找出每个员工的部门名称，要求显示员工名，部门名
SELECT 
	ENAME, (SELECT d.DNAME FROM DEPT d WHERE e.DEPTNO = d.DEPTNO) as DNAME  
FROM	
	`EMP` e;
```

<font color=red>*</font>：select 后面的子查询一次只能返回一条结果，多于1条就会报错。

### 1.11 UNION

+ UNION 运算符用于组合两个或更多 SELECT 语句的结果集。 

*  UNION 使用注意：
  * UNION 中的每个 SELECT 语句必须具有相同的列数 
  * 这些列也必须具有相似的数据类型 
  * 每个 SELECT 语句中的列也必须以相同的顺序排列

语法：` SELECT column_name(s) FROM table1 UNION SELECT column_name(s) FROM table2; `

 默认情况下，UNION 运算符选择的是一个不同的值。

 ```sql
SELECT ENAME, JOB FROM `EMP`
UNION
SELECT LOSAL, HISAL FROM `SALGRADE`;
-- mysql不报错, oracle语法严格会报错,要求结果集合并时列和列的数据类型也要一致
-- union 的效率更高一些
-- 对于连接来说每连接一次新表，匹配的次数满足笛卡尔积，成倍的翻。。。
-- UNION可以减少匹配的次数，在减少匹配次数的情况下，完成两个结果集的拼接
 ```

## 2. 删除

### 2.1 delete删除(虚拟删除)

* **语法**：` DELETE FROM table_name WHERE condition;  ` 

<font color=red>*</font>： 更新时 WHERE 子句指定需要删除哪些记录。如果省略了 WHERE 子句，表中所有记录 都将被删除！ 

- 表中的数据被删除了，但是这个数据在硬盘上的真实存储空间不会被释放！！！
- 缺点：删除效率比较低。
- 优点：支持回滚，后悔了可以再恢复数据！！

### 2.1 truncate删除(物理删除)

* **语法**：`TRUNCATE TABLE 表名;`

- 这种删除效率比较高，表被一次截断，物理删除。
- 缺点：不支持回滚。
- 优点：快速。

## 3. 改(update)

* **语法**：` UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;`

 <font color=red>*</font>： 更新时 WHERE 子句指定哪些记录需要更新, 如果省略 WHERE 子句，所有记录都 将更新！ 

## 4. 增加(insert)

* **语法** ： `INSERT INTO 表名(字段1, 字段2, 字段3, ...) VALUES(值1, 值2, 值3, ...);`

```sql
-- 新增一条姓名为zy的学生信息
INSERT INTO t_student(number, name, age) VALUES(12344, 'zy', 19);

-- 一次增加多条
INSERT INTO t_student(number, name, age) VALUES
(12344, 'zy', 19),
(12345, 'jph', 24),
(12346, 'qd', 26);
-- insert 语句执行成功,表中就会多一条记录，没有给其它字段指定值，默认是NULL。
```

 <font color=red>*</font>： 如果要为表中的所有列添加值，则不需要在 SQL 查询中指定列名称。 但是要确定值的顺序与表中的列顺序相同。 

## 5. 数据表操作(DDL)

### 5.1 数据表的创建

* **语法**：

```sql
create table 表名(
	字段名1 数据类型,
    字段名2 数据类型,
    字段名3 数据类型
);
-- 表名: 建议以t_或者tbl_开始,可读性强,见名知意。
-- 字段名: 见名知意。
-- 表名和字段名都属于标识符。
-- *注意：数据库中有一条命名规范,所有的标识符全部是小写，单词和单词之间使用下划线衔接。
```

#### 5.1.1 msyql常用数据类型：

* 数据库表中的每一列都需要有一个名称和数据类型。
* 创建 SQL 表时决定表中的每个列将要存储的数据的类型。数据类型是一个标签，是便于 SQL了解每个列期望存储什么类型的数据的指南。  

|     字段类型     |                             含义                             |
| :--------------: | :----------------------------------------------------------: |
| varchar(最长255) | **可变字符串长度**，会根据实际的数据长度动态分配空间<br />优点：节省空间；缺点：需要动态分配空间，速度慢 |
|  char(最长255)   | **定长字符串**，不管实际的数据长度是多少，分配固定长度的空间去存储数据<br/>优点：不需要动态分配空间，速度快<br/>缺点：使用不当可能会导致空间的浪费 |
|       clob       | 字符串大对象，最多可以存储4G的字符串<br />比如：存储文章，存储说明<br />超过255个字符的都可以采用clob字符大对象来存储。<br />MySQL中，CLOB类型数据可以使用text类型来定义 |
|   int(最长11)    |                        数字中的整数型                        |
|      bigint      |                        数字中的长整型                        |
|      float       |                         单精度浮点型                         |
|      double      |                         双精度浮点型                         |
|       date       |                   短日期类型，只包括年月日                   |
|     datetime     |                 长日期类型，包括年月日时分秒                 |
|       bool       |                    存储 true 或 false 值                     |
|      binary      |                           二进制串                           |
|    varbinary     |                      可变的二进制串长度                      |
|       blob       | 二进制大对象，存储图片、声音、视频等流媒体数据。<br />往BLOB类型的字段上插入数据的时候，需要使用IO流才可以 |
|       xml        |                         存储xml数据                          |

建表时 varchar 和 char 怎么选择？
​		比如说性别字段，因为性别是固定长度的字符串，所有选择char, char(1)
​		姓名字段，每个人的名字长度不一样所以选择varchar		

#### 5.1.2 约束

* 在创建表的时候，我们可以给表中的字段加上一些约束，来保证这个表中数据的完整性、有效性！！！

**约束类型**:

|      约束类型       |                含义                 |
| :-----------------: | :---------------------------------: |
|      NOT NULL       | 非空约束, 约束强制列不接受 NULL 值  |
|       UNIQUE        |              唯一约束               |
| PRIMARY KEY(简称PK) |              主键约束               |
| FOREIGN KEY(简称FK) |              外键约束               |
|       DEFAULT       | 提供该列数据未指定时所采用的默认值  |
|        CHECK        | 检查约束（mysql不支持，oracle支持） |
|        索引         |  用于在数据库中快速创建或检索数据   |

*  唯一约束是被约束的列在插入新数据时，如果和已经存在的列有相同的值，则会报错。 
*  UNIQUE 和 PRIMARY KEY 约束均为列或列集合提供了唯一性的保证。
*  唯一约束是被约束的列在插入新数据时，如果和已经存在的列有相同的值，则会报错
*   在mysql当中，如果一个字段同时被notnull和unique约束的话，改字段自动变成主键字段。

##### NOT NULL(非空约束)

* 非空约束not null 约束字段不能为NULL

```sql
DROP TABLE IF EXISTS t_info;
CREATE TABLE t_info(
	id int,
	name VARCHAR(255) NOT NULL,  # not null只有列级约束，没有表级的约束
	age INT(11)
);

INSERT INTO t_info(id, age) VALUES(1, 100);
-- 1364 - Field 'name' doesn't have a default value
```

##### UNIQUE(唯一约束)

* 每个表可以有多个 UNIQUE 约束，但是每个表<font color=red>只能有一个</font> PRIMARY KEY  约束。

* 唯一性约束unique约束的字段不能重复，但是**可以为NULL**
*  UNIQUE 约束唯一标识数据库表中的每条记录。  

```sql
DROP TABLE IF EXISTS t_info;
CREATE TABLE t_info(
	id int,
	name VARCHAR(255) UNIQUE, 
	age INT(11)
);

INSERT INTO t_info(id, name) VALUES(1, 'zy');
INSERT INTO t_info(id, name) VALUES(2, 'zy');
-- 1062 - Duplicate entry 'zy' for key 't_info.name'
```

* 联合唯一：name和email两个字段联合起来具有唯一性

```sql
DROP TABLE IF EXISTS t_info;
CREATE TABLE t_info(
	id int,
	name VARCHAR(255), 
	age INT(11),
	UNIQUE(name, age)    # 约束没有添加在列的后面，这种约束被称为表级约束。
);

INSERT INTO t_info(id, name, age) VALUES(1, 'zy', 13);
INSERT INTO t_info(id, name, age) VALUES(2, 'zy', 14);
INSERT INTO t_info(id, name, age) VALUES(2, 'zy', 14);
-- 1062 - Duplicate entry 'zy-14' for key 't_info.name'
```

##### primary key(主键约束)

**主键分类**

- 自然主键：主键值是一个自然数，和业务没关系。

- 业务主键：主键值和业务紧密关联，例如拿银行卡账号做主键值。这就是业务主键！

**在创建数据表时设置主键约束，既可以为表中的一个字段设置主键，也可以为表中多个字段设置联合主键。但是不论使用哪种方法，在一个表中主键只能有一个 **.

*  主键必须包含唯一的值。 
*  主键列不能包含 NULL 值。 
*  PRIMARY KEY 约束唯一标识数据库表中的每条记录 
*  每个表都应该有一个主键，并且每个表只能有一个主键。  
* 主键的特征：not null + unique（主键值不能是NULL，同时也不能重复！）
* PRIMARY KEY 约束拥有自动定义的 UNIQUE 约束。   

```sql
DROP TABLE IF EXISTS t_info;
CREATE TABLE t_info(
  -- 一个字段的主键叫做：单一主键
	id int PRIMARY KEY,    # 列级约束
	name VARCHAR(255),  
	age INT
);

INSERT INTO t_info(id, name, age) VALUES(1, 'qdd', 18);
INSERT INTO t_info(id, name, age) VALUES(2, 'zy', 24);
INSERT INTO t_info(id, name, age) VALUES(2, 'zy1', 25);
-- 1062 - Duplicate entry '2' for key 't_info.PRIMARY'
```

##### 联合主键
* 联合主键就是这个主键是由一张表中多个字段组成的。
* 主键由多个字段联合组成，语法格式如下：  PRIMARY KEY [字段1，字段2，…,字段n]
*  设置成主键约束的字段中不允许有空值 

```sql
DROP TABLE IF EXISTS t_info;
CREATE TABLE t_info(
	id INT,
	name VARCHAR(255) COMMENT '学生姓名',  
	age INT,
	-- 多个字段的主键叫做：联合主键
	PRIMARY KEY(id, name)     # 表级约束
)COMMENT '学生信息';

INSERT INTO t_info(id, name, age) VALUES(1, 'qdd', 18);
INSERT INTO t_info(id, name, age) VALUES(3, 'zy1', 24);
INSERT INTO t_info(id, name, age) VALUES(3, 'zy1', 25);
-- 1062 - Duplicate entry '3' for key 't_info.PRIMARY'
```

<font color=red>*</font>：如果一个联合主键的其中一个字段被修改了，那么该记录的唯一性可能会被破坏，从而导致数据异常或冲突。因此，在使用联合主键时，必须确保联合主键的所有字段都是不可更改的。 在实际开发中不建议使用复合主键，建议使用单一主键。

##### FOREIGN KEY(外键约束)

* 一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY。 

* FOREIGN KEY 约束用于预防破坏表之间连接的行为。  FOREIGN KEY 约束也能防止非法数据插入外键列，因为它必须是它指向的那个表 中的值之一。 

- 如果一个实体的某个字段指向另一个实体的主键，就称为外键
- 被指向的实体，称之为主实体（主表），也叫父实体（父表）
- 负责指向的实体，称之为从实体（从表），也叫子实体（子表）

```sql
DROP TABLE IF EXISTS t_info;
CREATE TABLE t_info(
	id INT PRIMARY KEY auto_increment,     # auto_increment
	自增
	name VARCHAR(255) COMMENT '学生姓名',
	age INT
)COMMENT '学生信息';

DROP TABLE IF EXISTS t_privilege;
CREATE TABLE t_privilege(
	id INT PRIMARY KEY auto_increment,
	privilege int DEFAULT 1
)COMMENT '权限表';

DROP TABLE IF EXISTS t_relation_privilege;
CREATE TABLE t_relation_privilege(
	id INT PRIMARY KEY auto_increment,
	info_id INT,
	privilege_id INT,
	FOREIGN KEY(info_id) REFERENCES t_info(id),
	FOREIGN KEY(privilege_id) REFERENCES t_privilege(id)
)COMMENT '关联表';
```

- 外键可以为空，可以理解成 一名学生肯定会关联到一个存在的班级，但来了一个转校生，还没有分班，他现在属于学生子表，但还没有关联到班级主表中的任何一条记录。

​		**删除表**的顺序: <font color=red>先删子，再删父</font>

​		**创建表**的顺序: <font color=red>先创建父，再创建子</font>

​		**删除数据**的顺序: <font color=red>先删子，再删父</font>

​		**插入数据**的顺序: <font color=red>先插入父，再插入子</font>

- 子表中的外键引用的父表中的某个字段，被引用的这个字段不一定是主键，但至少具有unique约束。

### 5.2 数据表的删除

* **语法**：`DROP TABLE if exists 表名;`

```sql
-- 删除 t_movie 表
DROP TABLE if exists t_movie;
```

### 5.3 数据表的修改

*  ALTER TABLE 语句用于在已有的表中添加、修改或删除列。 

#### 5.3.1 修改表名

**语法**:  `ALTER TABLE <旧表名> RENAME [TO] <新表名>;`

#### 5.3.2 修改表字符集

**语法**:  ` ALTER TABLE 表名 [DEFAULT] CHARACTER SET <字符集名> [DEFAULT] COLLATE <校对规则名>; `

eg:  使用 ALTER TABLE 将数据表 tb_students_info 的字符集修改为 gb2312，校对规则修改为 gb2312_chinese_ci

```sql
mysql> ALTER TABLE tb_students_info CHARACTER SET gb2312  DEFAULT COLLATE gb2312_chinese_ci;
```

#### 5.3.3 添加列

**语法**: ` ALTER TABLE table_name ADD column_name datatype;  `

#### 5.3.4 删除列

**语法**：` ALTER TABLE <表名> DROP <字段名>; `

#### 5.3.5 修改列数据类型

**语法**：`  ALTER TABLE <表名> MODIFY <字段名> <数据类型>; `

#### 5.3.6 修改列字段名称

**语法**：`   ALTER TABLE <表名> CHANGE <旧字段名> <新字段名> <新数据类型>;` 注意： 新数据类型：指修改后的数据类型，如果不需要修改字段的数据类型，可以将新数据类型设置成与原来一样，但数据类型不能为空 。

#### 5.3.7  字段约束相关操作

```sql
-- 添加唯一约束
ALTER TABLE table_name
ADD CONSTRAINT MyUniqueConstraint
UNIQUE(column1, column2...);

-- 添加 CHECK 约束语法
ALTER TABLE table_name
ADD CONSTRAINT MyUniqueConstraint
CHECK (CONDITION);

-- 添加主键约束语法
ALTER TABLE table_name
ADD CONSTRAINT MyPrimaryKey
PRIMARY KEY (column1, column2...);

-- 删除约束语法
ALTER TABLE table_name
DROP CONSTRAINT MyUniqueConstraint;
```

## 6. 数据库操作

* **show databases;** 	查看mysql中有哪些数据库
* **use test;**	表示正在使用一个名字叫做test的数据库
* **create database db01;**	创建数据库
* **show tables;** 	查看某个数据库下有哪些表
* **select version();**	查看mysql数据库的版本号
* **select database();**	查看当前使用的是哪个数据库
* **\c**	用来终止一条命令的输入

## 7. 存储引擎

* 什么是存储引擎，有什么用

  * 存储引擎是MySQL中特有的一个术语，其它数据库中没有。(Oracle中不叫这个名字)
  * 实际上存储引擎是一个表存储/组织数据的方式
  * 不同的存储引擎，表存储数据的方式不同。

```sql
  mysql> SHOW CREATE TABLE t_info;
  +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Table  | Create Table                                                                                                                                                                                                                                                     |
  +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | t_info | CREATE TABLE `t_info` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL COMMENT '????',
    `age` int DEFAULT NULL,
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='????' |
  +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

  在建表的时候可以在最后小括号的" ) "的右边使用：

  - ENGINE来指定存储引擎，mysql默认的存储引擎是：**InnoDB**
  - CHARSET来指定这张表的字符编码方式，mysql默认的字符编码方式是：**utf8**

### mysql 支持的存储引擎

命令：`show engines \G`  查看mysql支持哪些存储引擎

MYSQL常用的存储引擎：MEMORY、InnoDB、MyISAM

#### 1） MEMORY

- 使用 MEMORY 存储引擎的表，其数据存储在内存中，且行的长度固定，这两个特点使得 MEMORY 存储引擎非常**快**。

- MEMORY 存储引擎管理的表具有下列特征：
  -  在数据库目录内，每个表均以.frm 格式的文件表示。
  -  表数据及索引被存储在内存中。（目的就是快，查询快！）
  -  表级锁机制。
  -  不能包含 TEXT 或 BLOB 字段。

- MEMORY 存储引擎以前被称为HEAP 引擎。
- MEMORY引擎优点：查询效率是最高的。不需要和硬盘交互。
- MEMORY引擎缺点：不安全，关机之后数据消失。因为数据和索引都是在内存当中。

#### 2）InnoDB

- 这是mysql默认的存储引擎，同时也是一个重量级的存储引擎。
- InnoDB支持事务，支持数据库崩溃后自动恢复机制。
- InnoDB存储引擎最主要的特点是：非常安全。

- 它管理的表具有下列主要特征：
  - 每个 InnoDB 表在数据库目录中以.frm 格式文件表示
  - InnoDB 表空间 tablespace 被用于存储表的内容（表空间是一个逻辑名称。表空间存储数据+索引。）
  - 提供一组用来记录事务性活动的日志文件
  - 用 COMMIT(提交)、SAVEPOINT 及ROLLBACK(回滚)支持事务处理
  - 提供全 ACID 兼容
  - 在 MySQL 服务器崩溃后提供自动恢复
  - 多版本（MVCC）和行级锁定
  - 支持外键及引用的完整性，包括级联删除和更新
- InnoDB最大的特点就是支持事务：以保证数据的安全。效率不是很高，并且也不能压缩，不能转换为只读，
- 不能很好的节省存储空间。

#### 3）MyISAM

* 使用三个文件表示每个表：
  - 格式文件 — 存储表结构的定义（mytable.frm）
  - 数据文件 — 存储表行的内容（mytable.MYD）
  - 索引文件 — 存储表上索引（mytable.MYI）:索引是一本书的目录，缩小扫描范围，提高查询效率的一种机制。
* 可被转换为压缩、只读表来节省空间
* MyISAM存储引擎特点：
  - 可被转换为压缩、只读表来节省空间这是这种存储引擎的优势
  - MyISAM不支持事务机制，安全性低。

## 8. 事务**

* 一个事务其实就是一个完整的业务逻辑。是一个最小的工作单元。不可再分。

- 什么是一个完整的业务逻辑？

  * 假设转账，从A账户向B账户中转账10000.
    		将A账户的钱减去10000（update语句）
      		将B账户的钱加上10000（update语句）
      		这就是一个完整的业务逻辑。

  - 以上的操作是一个最小的工作单元，要么同时成功，要么同时失败，不可再分。这两个update语句要求必须同时成功或者同时失败，这样才能保证钱是正确的。

- insert   delete   update  只有以上的三个语句和事务有关系，其它都没有关系。

- 事务：就是**批量的DML语句同时成功，或者同时失败！**

### 8.1 InnoDB实现事务

- InnoDB存储引擎：提供一组用来记录事务性活动的日志文件

- 在事务的执行过程中，每一条DML的操作都会记录到“事务性活动的日志文件”中。
- 在事务的执行过程中，**我们可以提交事务，也可以回滚事务。**

- 提交事务:  **commit**; 语句
  - 清空事务性活动的日志文件，将数据全部彻底持久化到数据库表中。
  - 提交事务标志着，事务的结束。并且是一种全部成功的结束。

- 回滚事务:  **rollback**; 语句（回滚永远都是只能回滚到上一次的**提交点**！）
  - 将之前所有的DML操作全部撤销，并且清空事务性活动的日志文件
  - 回滚事务标志着，事务的结束。并且是一种全部失败的结束。

- 将mysql的自动提交机制**关闭**掉  `start transaction;`

```sql
-- 事务回滚
mysql> select * from info;
+----+------+------+
| id | name | age  |
+----+------+------+
|  1 | name |   18 |
|  2 | zy   |   18 |
|  3 | qdd  |   20 |
+----+------+------+
3 rows in set (0.02 sec)

mysql> start transaction;    # 开启事务
Query OK, 0 rows affected (0.02 sec)

mysql> insert into info values(4, 'lh', 25);
Query OK, 1 row affected (0.07 sec)

mysql> select * from info;
+----+------+------+
| id | name | age  |
+----+------+------+
|  1 | name |   18 |
|  2 | zy   |   18 |
|  3 | qdd  |   20 |
|  4 | lh   |   25 |
+----+------+------+
4 rows in set (0.01 sec)

mysql> rollback;     # 回滚
Query OK, 0 rows affected (0.01 sec)

mysql> select * from info;
+----+------+------+
| id | name | age  |
+----+------+------+
|  1 | name |   18 |
|  2 | zy   |   18 |
|  3 | qdd  |   20 |
+----+------+------+
3 rows in set (0.00 sec)
```

### 8.2 事务的四个特性

**A: 原子性**

* 说明事务是最小的工作单元，不可再分

**C: 一致性**

* 所有事务要求在同一个事务当中，所有操作必须同时成功，或者同时失败，以保证数据的一致性

**I: 隔离性***

* A事务和B事务之间具有一定的隔离，教室A和教室B之间有一道墙，这道墙就是隔离性

  比如说A事务在操作一张表的时候，另一个事务B也操作这张表

**D: 持久性**

* 事务最终的一个保障。事务提交，就相当于将没有保存到硬盘上的数据保存到硬盘上

### 8.3 事务的隔离性

* **事务与事务之间存在四个隔离级别**

  * mysql 5 查看隔离级别：`SELECT @@tx_isolation;`

  * mysql 8 查看隔离级别：`select @@transaction_isolation;`

##### 1. 读未提交：read uncommited（最低的隔离级别）<font color=red>没有提交就读到了</font>

- 事务A可以读取到事务B未提交的数据。
- 这种隔离级别存在的问题就是：**脏读现象**！(Dirty Read)我们称读到了脏数据。
- 这种隔离级别一般都是理论上的，大多数的数据库隔离级别都是二档起步！

```sql
-- 读未提交
mysql> set global transaction isolation level read uncommitted;
Query OK, 0 rows affected (0.02 sec)


---------------------------------------------------------------------------------------------
    sql终端1                           |                 sql终端2
                                      |            
mysql> use sql_road                   | mysql> use sql_road;
Database changed                      | Database changed
                                      | 
mysql> start transaction;             | mysql> start transaction;
Query OK, 0 rows affected (0.07 sec)  | Query OK, 0 rows affected (0.07 sec)
                                      |
mysql> select * from info;            | mysql> insert into info values(5, 'zy', 26);
+----+------+------+                  | Query OK, 1 row affected (0.06 sec)
| id | name | age  |                  |
+----+------+------+                  | 
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
+----+------+------+                  |
3 rows in set (0.06 sec)              |
                                      |
mysql> select * from info;            | -- 未提交
+----+------+------+                  | 
| id | name | age  |                  |
+----+------+------+                  |
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
|  5 | zy   |   26 |                  |
+----+------+------+                  |
4 rows in set (0.02 sec)              |
```

##### 2. 读已提交：read commited  <font color=red>提交之后才能读到</font>

- 事务A只能读取到事务B提交之后的数据。
- 这种隔离级别解决了解决了脏读的现象。
- 这种隔离级别不可重复读取数据。
  - 在事务开启之后，第一次读到的数据是3条，当前事务还没有结束，可能第二次再读取的时候，读到的数据是4条，3不等于4称为不可重复读取。
- 这种隔离级别是比较真实的数据，每一次读到的数据是绝对的真实。
- oracle数据库默认的隔离级别是：read committed

```sql
-- 提交已读
mysql> set global transaction isolation level read committed;
Query OK, 0 rows affected (0.09 sec)

--------------------------------------------------------------------------------
	sql终端1                          |                 sql终端2
                                      |            
mysql> use sql_road                   | mysql> use sql_road;
Database changed                      | Database changed
                                      | 
mysql> start transaction;             | mysql> start transaction;
Query OK, 0 rows affected (0.07 sec)  | Query OK, 0 rows affected (0.07 sec)
                                      |
mysql> select * from info;            | mysql> isert into info valuse(5,'zs',19);
+----+------+------+                  | Query OK, 1 row affected (0.06 sec)
| id | name | age  |                  |
+----+------+------+                  | 
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
+----+------+------+                  |
3 rows in set (0.06 sec)              |
                                      |
mysql> select * from info;            | mysql> commit; 
+----+------+------+				  | Query OK, 0 rows affected (0.01 sec)
| id | name | age  |				  |
+----+------+------+				  |
|  1 | name |   18 |				  |
|  2 | zy   |   18 |				  |
|  3 | qdd  |   20 |				  |
+----+------+------+    			  |
3 rows in set (0.00 sec)      		  |
                                      |
mysql> select * from info;            | -- 已提交
+----+------+------+                  | 
| id | name | age  |                  |
+----+------+------+                  |
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
|  5 | zs   |   19 |                  |
+----+------+------+                  |
4 rows in set (0.02 sec)              |
```

##### 3. 可重复读：repeatable read <font color=red>提交之后也读取不到，读取到的永远是刚开启事务时的数据</font>

- 事务A开启之后，不管是多久，每一次在事务A中读取到的数据都是一致的。即使事务B将数据已经修改，并且提交了，事务A读取到的数据还是没有发生改变，这就是可重复读。
- 可重复读可能会出现幻影读。每一次读取到的数据都是幻象。不够真实！
- 早晨9点开始开启了事务，只要事务不结束，到晚上9点，读到的数据还是那样！读到的是假象。不够绝对的真实。
- mysql中默认的事务隔离级别就是这个！！！

```sql
-- 可重复读
mysql> set global transaction isolation level repeatable read;
Query OK, 0 rows affected (0.00 sec)

------------------------------------------------------------------------------------
	sql终端1                          |                 sql终端2
                                      |            
mysql> use sql_road                   | mysql> use sql_road;
Database changed                      | Database changed
                                      | 
mysql> start transaction;             | mysql> start transaction;
Query OK, 0 rows affected (0.07 sec)  | Query OK, 0 rows affected (0.07 sec)
                                      |
mysql> select * from info;            | mysql> insert into info values(7,'zyy', 26);
+----+------+------+                  | Query OK, 1 row affected (0.00 sec)
| id | name | age  |                  |
+----+------+------+                  | 
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
+----+------+------+                  |
3 rows in set (0.06 sec)              |
                                      |
mysql> select * from info;            | mysql> update info set name='zdddddddd' where id=7; 
+----+------+------+				  | Query OK, 1 row affected (0.00 sec)
| id | name | age  |				  | Rows matched: 1  Changed: 1  Warnings: 0
+----+------+------+				  |
|  1 | name |   18 |				  |
|  2 | zy   |   18 |				  |
|  3 | qdd  |   20 |				  |
+----+------+------+    			  |
3 rows in set (0.00 sec)      		  |
                                      |
mysql> select * from info;            | mysql> commit;
+----+------+------+                  | Query OK, 0 rows affected (0.00 sec)
| id | name | age  |                  |
+----+------+------+                  |
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
+----+------+------+                  |
4 rows in set (0.02 sec)              |
									  |
mysql> select * from info;            |
+----+------+------+                  |
| id | name | age  |                  |
+----+------+------+                  |
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
+----+------+------+                  |
3 rows in set (0.00 sec)              |
```

##### 4. 序列化/串行化：serializable （最高的隔离级别） 

- 效率最低，解决了所有的问题。
- 这种隔离级别表示事务排队，不能并发！
- synchronized，线程同步（事务同步）每一次读取到的数据都是最真实的，且效率是最低的。

```sql
-- 串行化
mysql> set global transaction isolation level serializable;
Query OK, 0 rows affected (0.00 sec)

------------------------------------------------------------------------
	sql终端1                           |                 sql终端2
                                      |            
mysql> use sql_road                   | mysql> use sql_road;
Database changed                      | Database changed
                                      | 
mysql> start transaction;             | mysql> start transaction;
Query OK, 0 rows affected (0.07 sec)  | Query OK, 0 rows affected (0.07 sec)
                                      |
mysql> select * from info;            | mysql> insert into info values(4, 'zy', 25);
+----+------+------+                  | Query OK, 1 row affected (0.00 sec)
| id | name | age  |                  |
+----+------+------+                  | 
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |                  |
+----+------+------+                  |
3 rows in set (0.06 sec)              |
                                      |
mysql> select * from info;            | mysql> commit;  
# 时间长了会报错 					     |
ERROR 1205 (HY000):                   |
Lock wait timeout exceeded;           | 
try restarting transaction			  |						  |  
									  | 
                                      |
mysql> select * from info;            | 
+----+------+------+                  | 
| id | name | age  |                  |
+----+------+------+                  |
|  1 | name |   18 |                  |
|  2 | zy   |   18 |                  |
|  3 | qdd  |   20 |				  |
|  4 | zy   |   25 |                  |
+----+------+------+                  |
4 rows in set (0.02 sec)              |
```

## 9. 索引

### 9.1 什么是索引

* 索引是在数据库表的字段上添加的，是为了提高查询效率存在的一种机智
* 一张表的一个字段可以添加一个索引，多个字段联合起来也可以添加索引
*  索引是一种特殊的查询表，可以被数据库搜索引擎用来加速数据的检索 
*  索引就是指向表中数据的指针
* 类似于一本书籍的目录。
* MySQL在查询方面主要就是两种方式：全表扫描  ；根据索引检索。
* **数据结构相同。TreeSet（TreeMap）底层是一个自平衡的二叉树！在mysql当中索引是一个B-Tree数据结构。**
* **遵循左小又大原则存放，采用中序遍历方式遍历取数据。**

### 9.2 索引的作用

*  索引能够提高 SELECT 查询和 WHERE 子句的速度，但是却降低了包含 UPDATE  语句或 INSERT 语句的数据输入过程的速度。
* 索引的创建与删除不会对表中的数据 产生影响。 
* 创建索引需要使用 CREATE INDEX 语句，该语句允许对索引命名，**指定要创建索 引的表以及对哪些列进行索引，还可以指定索引按照升序或者降序排列**。 
*  同 UNIQUE 约束一样，索引可以是唯一的。这种情况下，索引会阻止列中（或者 列的组合，其中某些列有索引）出现重复的条目。 

### 9.3 什么时候需要给字段添加索引

* 表中该字段中数据量庞大
* 经常被检索，经常出现在where子句中的字段
* 经常被DML(insert、delete、update)操作的字段不建议添加索引
* 建议不要随意添加索引，因为索引也是需要维护的，太多的话反而会降低系统的性能
* 建议通过主键查询，建议通过unique约束的字段进行查询，效率是比较高的。

###  9.4 索引的创建和删除

* 在任何数据库当中主键上都会自动添加索引对象，id字段上自动有索引，因为id是PK。另外在mysql当中，一个字段上如果有unique约束的话，也会自动创建索引对象
* 在任何数据库当中，任何一张表的任何一条记录在硬盘存储上都有一个硬盘的物理存储编号。
* 在mysql当中，索引是一个单独的对象，不同的存储引擎以不同的形式存在，在MyISAM存储引擎中，索引存储在一个.MYI文件中。在InnoDB存储引擎中索引存储在一个逻辑名称叫做tablespace的当中。在MEMORY存储引擎当中索引被存储在内存当中。不管索引存储在哪里，索引在mysql当中都是一个树的形式

```sql
-- 创建索引
-- 1. 单列索引
-- 语法: CREATE INDEX index_name ON table_name (column_name);
mysql> create index info_name_index on info(name);  
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

-- 2. 聚簇索引
-- 聚簇索引在表中两个或更多的列的基础上建立。
--语法: CREATE INDEX index_name ON table_name (column1, column2);
mysql> create index info_name_index on info(name, age);  
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

-- 3. 唯一索引
-- 语法: CREATE UNIQUE INDEX index_name ON table_name (column_name);

-- 4.隐式索引
-- 隐式索引由数据库服务器在创建某些对象的时候自动生成。例如，对于主键约束和唯一约束，数据库服务器就会自动创建索引。

-- *注意：
-- 创建单列索引还是聚簇索引，要看每次查询中，哪些列在作为过滤条件的 WHERE 子句中最常出现。
-- 如果只需要一列，那么就应当创建单列索引。如果作为过滤条件的 WHERE 子句用 到了两个或者更多的列，那么聚簇索引就是最好的选择。

-- 删除索引
-- 语法: DROP INDEX index_name ON table_name;
mysql> drop index info_name_index on info;    
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

-- 在mysql中查看一个SQL语句是否使用了索引进行检索？
mysql> explain select * from info where name='zy';
+----+-------------+-------+------------+------+-----------------+-----------------+---------+-------+------+----------+-------+
| id | select_type | table | partitions | type | possible_keys   | key             | key_len | ref   | rows | filtered | Extra |
+----+-------------+-------+------------+------+-----------------+-----------------+---------+-------+------+----------+-------+
|  1 | SIMPLE      | info  | NULL       | ref  | info_name_index | info_name_index | 123     | const |    2 |   100.00 | NULL  |
+----+-------------+-------+------------+------+-----------------+-----------------+---------+-------+------+----------+-------+
1 row in set, 1 warning (0.00 sec)
```

### 9.5 索引的失效

```sql
-- 1.失效一: 模糊查询
mysql> explain select * from info where name like '%d';
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | info  | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    4 |    25.00 | Using where |
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
-- 这种情况即使添加了索引也不会走索引, 原因是因为模糊匹配当中以"%"开头,这种情况会检索全表
-- 尽量避免模糊查询的时候以`%`开始，这是一种优化策略。

-- 2.失效二: 使用or的时候会失效
mysql> explain select * from info where name='zy' or age=18;
+----+-------------+-------+------------+------+-----------------+------+---------+------+------+----------+-------------+
| id | select_type | table | partitions | type | possible_keys   | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-------+------------+------+-----------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | info  | NULL       | ALL  | info_name_index | NULL | NULL    | NULL |    4 |    50.00 | Using where |
+----+-------------+-------+------------+------+-----------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
-- 使用or的时候会失效，如果使用or要求or两边的的条件字段都要有索引，才会走索引。
-- 如果其中一个字段没有索引，那么另一个字段上的索引也会实现。
-- 所以不建议使用or

-- 3.失效三: 复合索引会失效
-- 使用复合索引的时候，没有使用左侧的列查找,索引失效

-- 4. 失效四: 索引列参加了运算
-- 当设置的索引列参加了运算,索引失效
```

## 10.视图

* 视图view: 不同的角度去看待同一份数据。
*  视图包含行和列，就像真正的表一样。
* 视图中的字段是一个或多个数据库中真实表 中的字段。 

```sql
mysql> create table info_bak as select * from info;
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from info_bak;
+----+------+------+
| id | name | age  |
+----+------+------+
|  1 | name |   18 |
|  3 | qdd  |   20 |
|  2 | zy   |   18 |
|  4 | zy   |   25 |
+----+------+------+
4 rows in set (0.00 sec)

-- 创建视图对象
mysql> create view info_bak_view as select * from info_bak;
Query OK, 0 rows affected (0.01 sec)

-- 删除视图对象
mysql> drop view info_bak_view;
Query OK, 0 rows affected (0.01 sec)

-- 注意：只有DQL语句才能以view的形式创建。
--	create view view_name as 这里的语句必须是DQL语句;
```

### 10.1 视图的作用

* 可以面向视图对象进行增删改查，对视图对象的增删改查，会导致原表被操作！（视图的特点：通过对视图的操作，会影响到原表数据。）

```sql
-- 创建视图
mysql> create view info_bak_view as select * from info_bak;
Query OK, 0 rows affected (0.01 sec)

-- 面向视图插入
insert into info_bak_view values(5, 'biubiu', 25);

-- 查询原表
mysql> select * from info_bak;
+----+--------+------+
| id | name   | age  |
+----+--------+------+
|  1 | name   |   18 |
|  3 | qdd    |   20 |
|  2 | zy     |   18 |
|  4 | zy     |   25 |
|  5 | biubiu |   25 |
+----+--------+------+
5 rows in set (0.00 sec)

-- 面向视图删除
mysql> delete from info_bak_view;
Query OK, 5 rows affected (0.00 sec)

-- 查询原表数据
mysql> delete from info_bak;
Query OK, 0 rows affected (0.00 sec)
```

**视图在开发中的作用：**

- 假设有一条非常复杂的SQL语句，而这条SQL语句需要在不同的位置上反复使用。
  每一次使用这个sql语句的时候都需要重新编写，很长，很麻烦，怎么办？
  		可以把这条复杂的SQL语句以视图对象的形式新建。
  		在需要编写这条SQL语句的位置直接使用视图对象，可以大大简化开发。
  		并且利于后期的维护，因为修改的时候也只需要修改一个位置就行，只需要
  		修改视图对象所映射的SQL语句。

- 我们以后面向视图开发的时候，使用视图的时候可以像使用table一样。

- 可以对视图进行增删改查等操作。****视图不是在内存当中，视图对象也是**存储在硬盘上的，不会消失。**

## 11. 数据库三范式 

### 第一范式

* 要求任何一张表必须有主键，每一个字段原子性不可再分。

### 第二范式

* 建立在第一范式的基础之上，要求所有非主键字段完全依赖主键，不要产生部分依赖。

### 第三范式

* 建立在第二范式的基础之上，要求所有非主键字段直接依赖主键，不要产生传递依赖。

设计数据库表的时候，按照以上的范式进行，可以避免表中数据的冗余，空间的浪费。

**关于三范式的实际使用：**

数据库设计三范式是理论上的，实践和理论有的时候有偏差。最终的目的都是为了满足客户的需求，有的时候会拿冗余换执行速度。

因为在sql当中，表和表之间连接次数越多，效率越低。（笛卡尔积）

有的时候可能会存在冗余，但是为了减少表的连接次数，这样做也是合理的，并且对于开发人员来说，sql语句的编写难度也会降低。

<font color=red>*</font>：**一对多，两张表，多表加外键**

<font color=red>*</font>：**多对多，三张表，关系表两个外键**


## 12. SQL语句快速参考

* 1. **快速复制表**
  * `create  table  新表名 as select * from 复制的表名;`
  * 原理是将查询结果当做一张新表创建，表创建出来同时数据也存在了
  
* 2. **将查询结果插入一张表**
  * `insert into 表1 select * from 表2;` (很少用)

  
  



