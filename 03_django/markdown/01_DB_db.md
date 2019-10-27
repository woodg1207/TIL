# 01. Data Base



#### 스키마(scheme)

- 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조
- 데이터베이스의 구조와 제약 조건에 관련한 전반적인 명세를 기술

#### SQL 개념

- DDL
- DML
- DCL

### tutorial

```sql
student@DESKTOP MINGW64 ~/Desktop/TIL/03_django/04_db/00_sql (master)
$ sqlite3 tutorial.sqlite3
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite> .databases
main: C:\Users\student\Desktop\TIL\03_django\04_db\00_sql\tutorial.sqlite3
```



```sql
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables
examples
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232
sqlite> .headers on
sqlite> .mode colum
sqlite> SELECT * FROM examples;
id          first_name  last_name   age         country     phone
----------  ----------  ----------  ----------  ----------  -------------
1           길동          홍           600         충청도         010-2424-1232
sqlite>
```

### 1. DCL (create, drop, select)

- 생성

```sql
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT );
sqlite> .tables
classmates  examples
```



```sql
sqlite> .tables     --> 테이블 목록 조회
classmates  examples
sqlite> .schema classmates  --> 특정 테이블 스마 조회
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT );
```



`.`  : sqlite3 프로그램의 기능을 실행하는 것

`;` : 세미콜론 까지가 하나의 명령(Query)으로 간주

-  SQL 문법은 소문자로 작성해도 된다. (단, 대문자를 권장한다.)
- 하나의 DB에는 여러개의 table이 존재한다. 



- 삭제 (DROP)

```sql
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
```

- data  추가

```bash
sqlite> CREATE TABLE classmates(   ---> 생성
   ...> name TEXT,
   ...> age INTEGER,
   ...> address TEXT);
sqlite> INSERT INTO classmates (name, age) ---> 추가
   ...> values('홍길동', 23);
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         23
sqlite> INSERT INTO classmates (name, age, address)-->전체 속성시에 명시()필요 X
   ...> values('홍길동', 30, '서울');
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         23
홍길동         30          서울
```

- 

```bash
sqlite> SELECT rowid, * FROM classmates; --> id(기본 키) 자동생성(64비트 정수의 최대값까지)
rowid       name        age         address
----------  ----------  ----------  ----------
1           홍길동         23
2           홍길동         30          서울
```

- NOT NULL

```sqlite
sqlite> INSERT INTO classmates (name, age) VALUES('홍길동', 23);
Error: NOT NULL constraint failed: classmates.address

sqlite> INSERT INTO classmates (name, age, address) VALUES('홍길동', 23, 'seoul');

sqlite> SELECT * FROM classmates;
id          name        age         address
----------  ----------  ----------  ----------
1           홍길동         23          seoul
sqlite> INSERT INTO classmates VALUES ('김영희',30, '대전');
Error: table classmates has 4 columns but 3 values were supplied

추가))) rowid를 사용하는게 편리하다. 

sqlite> INSERT INTO classmates VALUES ('홍길동',30,'서울'), ('김철수',23,'대전')
, ('박나래',33,'광주'), ('김영희',23,'구미');
```

- 조회 

```sqlite
sqlite> SELECT rowid, name FROM classmates;
rowid       name
----------  ----------
1           홍길동
2           김철수
...

sqlite> SELECT rowid, name FROM classmates LIMIT 1;
rowid       name
----------  ----------
1           홍길동

0ffset은 특정위치 이후에서 부터 몇개 --> 2부터 1개 라서 3번이 나온다.
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
rowid       name
----------  ----------
3           박나래

sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
rowid       name
----------  ----------
1           홍길동

--> 중복없이 가져오는 것 DISTINCT
sqlite> SELECT DISTINCT age FROM classmates;
age
----------
30
23
33

```

### DML 

- data 삭제 (delete) 레코드를 삭제함.

```sql
sqlite> DELETE FROM classmates WHERE rowid = 4;
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         30          서울
김철수         23          대전
박나래         33          광주

sqlite> INSERT INTO classmates VALUES ('최철순', 44, '서울');
sqlite> SELECT rowid, * FROM classmates;
rowid       name        age         address
----------  ----------  ----------  ----------
1           홍길동         30          서울
2           김철수         23          대전
3           박나래         33          광주
4           최철순         44          서울
--> 4번을 재 사용. 프로그램마다 다름.

--> AUTOINCREMENT 특성
-->명세상 재사용이 아니라면 이 속성을 사용하지 말아야 한다. 불필요한 메모리사용
sqlite> CREATE TABLE tests(
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL);
sqlite> INSERT INTO tests (id, name)
   ...> VALUES(1,'홍길동'), (2,'김철수');
sqlite> select rowid, * from tests;
id          id          name
----------  ----------  ----------
1           1           홍길동
2           2           김철수

sqlite> DELETE FROM tests WHERE id=2; --> 삭제 후
sqlite> INSERT INTO tests(name) VALUES('최철순');
sqlite> select rowid, * from tests;
id          id          name
----------  ----------  ----------
1           1           홍길동
3           3           최철순

```

- rowid 의 최대값은 64비트 8바이트 실수의 최대값
  - 922경
- INSERT INTO를 한다면
  1.  AUTOINCREMENT 없을때: 중간에 ㅇ벗는 ID를 재사용하므로 에러가 나지 않는다.
  2.  AUTOINCREMENT 있을때: 최대 레코드를 넘어서기 때문에 에러가 발생.



- DATA 수정( update )

```sql
sqlite> UPDATE classmates SET name = '홍길동', address = '제주도' WHERE rowid=4;
sqlite> select rowid, * from classmates;
rowid       name        age         address
----------  ----------  ----------  ----------
1           홍길동         30          서울
2           김철수         23          대전
3           박나래         33          광주
4           홍길동         44          제주도

```

![](C:\Users\student\Desktop\TIL\03_django\markdown\img\db.JPG)



## 2.심화

#### WHERE

```sqlite
sqlite> SELECT * FROM users WHERE age >= 30;  --> 이상
sqlite> select first_name from users where age >= 30;

sqlite> select last_name, age from users where age >= 30 and last_name = '김';

sqlite> SELECT COUNT(*) FROM users; --> 레코드의 개수를 봔환한다.
COUNT(*)
1000
++
AVG(), SUM(), MIN(), MAM() ---> int 속성에만 가능하다

--> 30 이상인사람들의 평균나이
sqlite> SELECT AVG(age) FROM users WHERE age >= 30;
AVG(age)
35.1763285024155

--> 가장 큰 잔액의 사람이름과 해당 잔액
sqlite> SELECT last_name, first_name, MAX(balance) FROM users ;
last_name,first_name,MAX(balance)
"김","선영",990000

users에서 30살 이상인 사람의 계좌 평균 잔액?
sqlite> SELECT AVG(balance) FROM users WHERE age >= 30;
AVG(balance)
153541.425120773

```

#### like

- 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환한다.

`_` : 반드시 이 자리에 한개의 문자가 필요
`%` : 이 자리에 문자열이 있거나, 없거나

![](C:\Users\student\Desktop\TIL\03_django\markdown\img\like.JPG)

```sql
sqlite> SELECT * FROM users WHERE age LIKE '2_' ;   -->20대인 사람들.

sqlite> SELECT * FROM users WHERE phone LIKE '02-%' ;   -->지역번호가 02-

sqlite> SELECT * FROM users WHERE first_name LIKE '%준' ; -->이름이 '준'으로 끝나는 사람

sqlite> SELECT * FROM users WHERE phone LIKE '%-5114-%' ; --> 중간번호가 '5114'인 사람

```

#### ORDER 정렬

ORDER BY column1, ... [asc/desc]

```sql
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
나이를 오름차순으로 10명
sqlite> SELECT * FROM users ORDER BY age, last_name LIMIT 10;

sqlite> SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10 ;
계좌 잔액순으로 내림차순
```



#### ALTER

```sql
sqlite> .tables
articles    classmates  examples    tests       users
sqlite> INSERT INTO articles VALUES
   ...> ( '1 번제목','1번내용');
1. 테이블 이름 변경
sqlite> ALTER TABLE articles RENAME TO news;
sqlite> .tables
classmates  examples    news        tests       users

2. 새로운 컬럼 추가
sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at DATETIME NOT NULL ;
Error: Cannot add a NOT NULL column with default value NULL
## 기존데이터에 not null 조건으로 인해 null 값으로 새로운 겈럼이 추가될수 없으므로 위와 같은 에러가 발생한다. not null조건을 없애거나 default값을 설정해야한다.

1>> NOT NULL 조건 삭제 
sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at DATETIME ;
sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at DATETIME ;
sqlite> INSERT INTO news VALUES ('title', 'content', datetime('now', 'localtime')) ;

2>> DEFAULT 값을 설정해 준다.
sqlite> ALTER TABLE news ADD  COLUMN subtitle TEXT NOT NULL DEFAULT 1;
sqlite> select * from news;
title|content|created_at|subtitle
1 번제목|1번내용||1
title|content|2019-10-16 14:10:51|1

```

