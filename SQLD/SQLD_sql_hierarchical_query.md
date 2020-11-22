## SQLD_sql_hierarchical_query

### 1. 계층형 질의

- 테이블에 계층형 데이터가 존재하는 경우 데이터를 조회하기 위해서 계층형 질의(Hierarchical Query)를 사용한다. 
- 계층형 데이터란 동일 테이블에 계층적으로 상위와 하위 데이터가 포함된 데이터를 말한다.

### 2. Oracle 계층형 질의

```mysql
select...
from table_a
where 조건 and 조건 ...
start with 조건
connect by [nocycle] 조건 and 조건 ...
[order siblings by column, column, ...]
```

- START WITH절은 계층 구조 전개의 시작 위치를 지정하는 구문이다. 
  - 즉, 루트 데이터를 지정한다.(액세스) - 
- CONNECT BY절은 다음에 전개될 자식 데이터를 지정하는 구문이다. 
  - 자식 데이터는 CONNECT BY절에 주어진 조건을 만족해야 한다.(조인) 
  - PRIOR : CONNECT BY절에 사용되며, 현재 읽은 칼럼을 지정한다. 
    - `PRIOR 자식 = 부모` 형태를 사용하면 계층구조에서 자식 데이터에서 부모 데이터(자식 → 부모) 방향으로 전개하는 순방향 전개를 한다.
    - `PRIOR 부모 = 자식` 형태를 사용하면 반대로 부모 데이터에서 자식 데이터(부모 → 자식) 방향으로 전개하는 역방향 전개를 한다. 
    - NOCYCLE : 데이터를 전개하면서 이미 나타났던 동일한 데이터가 전개 중에 다시 나타난다면 이것을 가리켜 사이클(Cycle)이 형성되었다라고 말한다. 사이클이 발생한 데이터는 런타임 오류가 발생한다. 
    - 그렇지만 NOCYCLE를 추가하면 사이클이 발생한 이후의 데이터는 전개하지 않는다. 
- ORDER SIBLINGS BY : 형제 노드(동일 LEVEL) 사이에서 정렬을 수행한다. 
- WHERE : 모든 전개를 수행한 후에 지정된 조건을 만족하는 데이터만 추출한다.(필터링)

##### orcle은 가상 칼럼을 제공한다

|                    | 설명                                                         |
| ------------------ | ------------------------------------------------------------ |
| level              | 루트 데이터면 1, 하위는 2, `리프`까지 1씩 증가               |
| connect_by_isleaf  | 전개 과정에서 해당 데이터가 `리프`면 1, 아니면 0             |
| connect_by_iscycle | 전개 과정에서 자식을 갖는데, 해당 데이터가 조상으로 존재하면 1, 아니면 0. cycle 옵션을 사용했을때만 가능, 여기서 조상이란 자신으로부터 루트까지의 경로에 존재하는 데이터 |



##### ex) 

- 결과 데이터를 들여쓰기 하기 위해서 LPAD 함수를 사용하였다.

- ```mysql
  SELECT LEVEL, LPAD(' ', 4 * (LEVEL-1)) || 사원 사원, 관리자, CONNECT_BY_ISLEAF ISLEAF 
  FROM 사원 
  START WITH 관리자 IS NULL 
  CONNECT BY PRIOR 사원 = 관리자;
  ```

- ```mysql
  LEVEL 사원 관리자 ISLEAF 
  ----- -------- ----- ------ 
  1 A 0 
  2 B A 1 
  2 C A 0 
  3 D C 1 
  3 E C 1
  ```

  - A는 루트 데이터이기 때문에 레벨이 1이다. 
  - A의 하위 데이터인 B, C는 레벨이 2이다. 
  - 그리고 C의 하위 데이터인 D, E는 레벨이 3이다. 
  - 리프 데이터는 B, D, E이다. 관리자 → 사원 방향을 전개이기 때문에 순방향 전개이다. [그림 Ⅱ-2-8]은 계층형 질의에 대한 논리적인 실행 모습이다.

- 다음 예제는 사원 'D'로부터 자신의 상위관리자를 찾는 역방향 전개의 예이다.

```mysql
SELECT LEVEL, LPAD(' ', 4 * (LEVEL-1)) || 사원 사원, 관리자, CONNECT_BY_ISLEAF ISLEAF FROM 사원 
START WITH 사원 = 'D' 
CONNECT BY PRIOR 관리자 = 사원;
```

```mysql
LEVEL 사원 관리자 ISLEAF 
----- --------- ----- ----- 
1 D C 0 
2 C A 0 
3 A 1
```

- 역방향 전개이기 때문에 하위 데이터에서 상위 데이터로 전개된다. 
- 결과를 보면 내용을 제외하고 표시 형태는 순방향 전개와 동일하다. 
- D는 루트 데이터이기 때문에 레벨이 1이다. D의 상위 데이터인 C는 레벨이 2이다. 
- 그리고 C의 상위 데이터인 A는 레벨이 3이다. 리프 데이터는 A이다. 
- 루트 및 레벨은 전개되는 방향에 따라 반대가 됨을 알 수 있다.

| 함수                | 설명                                                         |
| ------------------- | ------------------------------------------------------------ |
| sys_connect_by_path | 루트 데이터 부터 현재 전개할 데이터까지의 경로를 표기. <br />사용법 : `sys_connect_by_path(칼럼, 경로 분리자)` |
| connect_by_root     | 현재 전개할 데이터의 루트 데이터를 표시<br />사용법 : `connect_by_root 칼럼` |

```mysql
SELECT CONNECT_BY_ROOT 사원 루트사원, SYS_CONNECT_BY_PATH(사원, '/') 경로, 사원, 관리자 FROM 사원 
START WITH 관리자 IS NULL 
CONNECT BY PRIOR 사원 = 관리자
```

```mysql
루트사원 경로 사원 관리자 
------- ------- ---- ----- 
A /A A 
A /A/B B A 
A /A/C C A 
A /A/C/D D C 
A /A/C/E E C
```

- START WITH를 통해 추출된 루트 데이터가 1건 이기 때문에 루트사원은 모두 A이다. 경로는 루트로부터 현재 데이터까지의 경로를 표시한다. 예를 들어, D의 경로는 A → C → D 이다.

### 3. SQL server 계층형 질의

-  Northwind 데이터베이스에 접속하여 Employees 테이블의 데이터를 조회해 보자.

- ```sql
  USE NORTHWIND GO SELECT EMPLOYEEID, LASTNAME, FIRSTNAME, REPORTSTO FROM EMPLOYEES GO
  ************************************************************************** 
  EmployeeID LastName FirstName ReportsTo 
  --------- -------- ------- -------- 
  1 Davolio Nancy 2 
  2 Fulle Andrew NULL 
  3 Leverling Janet 2 
  4 Peacock Margaret 2 
  5 Buchanan Steven 2 
  6 Suyama Michael 5 
  7 King Robert 5 
  8 Callahan Laura 2 
  9 Dodsworth Anne 5 (9개 행 적용됨)
  ```

- 총 9개 로우가 있는데, ReportsTo 칼럼이 상위 사원에 해당하며 EmployeeID 칼럼과 재귀적 관계를 맺고 있다. 

- EmployeeID가 2인 Fuller 사원을 살펴보면, ReportsTo 칼럼 값이 NULL이므로 계층 구조의 최상위에 있음을 알 수 있다. 

- CTE(Common Table Expression)를 재귀 호출함으로써 Employees 데이터의 최상위부터 시작해 하위 방향으로 계층 구조를 전개하도록 작성한 쿼리와 결과는 다음과 같다.

- ```sql
  WITH EMPLOYEES_ANCHOR AS ( 
      SELECT EMPLOYEEID, LASTNAME, FIRSTNAME, REPORTSTO, 0 AS LEVEL FROM EMPLOYEES WHERE REPORTSTO IS NULL 
      /* 재귀 호출의 시작점 */ 
      UNION ALL 
      SELECT R.EMPLOYEEID, R.LASTNAME, R.FIRSTNAME, R.REPORTSTO, A.LEVEL + 1 FROM EMPLOYEES_ANCHOR A, EMPLOYEES R WHERE A.EMPLOYEEID = R.REPORTSTO )
      SELECT LEVEL, EMPLOYEEID, LASTNAME, FIRSTNAME, REPORTSTO FROM EMPLOYEES_ANCHOR GO
  **************************************************************************
  Level EmployeeID LastName FirstName ReportsTo 
  ---- -------- ------- ----- -------- 
  0 2 Fuller Andrew NULL 
  1 1 Davolio Nancy 2 
  1 3 Leverling Janet 2 
  1 4 Peacock Margaret 2 
  1 5 Buchanan Steven 2 
  1 8 Callahan Laura 2 
  2 6 Suyama Michael 5 
  2 7 King Robert 5 
  2 9 Dodsworth Anne 5 (9개 행 적용됨)
  ```

- WITH 절의 CTE 쿼리를 보면, UNION ALL 연산자로 쿼리 두 개를 결합했다. 

- 둘 중 위에 있는 쿼리를 ‘앵커 멤버’(Anchor Member)라고 하고, 아래에 있는 쿼리를 ‘재귀 멤버’(Recursive Member)라고 한다. 

- 1. CTE 식을 앵커 멤버와 재귀 멤버로 분할한다. 
  2. 앵커 멤버를 실행하여 첫 번째 호출 또는 기본 결과 집합(T0)을 만든다.
  3. Ti는 입력으로 사용하고 Ti+1은 출력으로 사용하여 재귀 멤버를 실행한다.
  4. 빈 집합이 반환될 때까지 3단계를 반복한다.
  5. 결과 집합을 반환한다. 이것은 T0에서 Tn까지의 UNION ALL이다.

- 

### 4. 셀프 조인

- 동일 테이블 사이의 조인

- 별칭을 사용해야 구분 해야함.

- ```sql
  SELECT WORKER.ID 사원번호, WORKER.NAME 사원명, MANAGER.NAME 관리자명 
  FROM EMP WORKER, EMP MANAGER WHERE WORKER.MGR = MANAGER.ID;
  ```

##### ex)

- 동일 테이블을 다른 테이블인 것처럼 처리하기 위해 테이블 별칭을 사용한다. 여기서는 E1(사원), E2(관리자) 테이블 별칭을 사용하였다. 차상위 관리자를 구하기 위해서 E1.관리자 = E2.사원 조인 조건을 사용한다. 셀프 조인을 이용한 SQL문은 다음과 같다.

- ```sql
  SELECT E1.사원, E1.관리자, E2.관리자 차상위_관리자 FROM 사원 E1, 사원 E2 WHERE E1.관리자 = E2.사원 ORDER BY E1.사원;
  ```

- 결과

  ```sql
  사원 관리자 차상위_관리자 
  ---- ------ ---------- 
  B A 
  C A 
  D C A 
  E C A
  ```

- 결과에서 A에 대한 정보는 누락되었다. 

- 내부 조인(Inner Join)을 사용할 경우 자신의 관리자가 존재하지 않는 경우에는 관리자(E2) 테이블에서 조인할 대상이 존재하지 않기 때문에 해당 데이터는 결과에서 누락된다. 

- 이를 방지하기 위해서는 아우터 조인을 사용해야 한다. 

- ```sql
  SELECT E1.사원, E1.관리자, E2.관리자 차상위_관리자 FROM 사원 E1 LEFT OUTER JOIN 사원 E2 ON (E1.관리자 = E2.사원) ORDER BY E1.사원;
  ```

- 결과

  ```sql
  사원 관리자 차상위_관리자 
  ---- ----- ---------- 
  A 
  B A 
  C A 
  D C A 
  E C A
  ```

  