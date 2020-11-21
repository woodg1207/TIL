# SQLD_sql_join

### 1. INNER JOIN

```sql
SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP, DEPT WHERE EMP.DEPTNO = DEPT.DEPTNO; 
SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP INNER JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO; INNER는 JOIN의 디폴트 옵션으로 아래 SQL문과 같이 생략 가능하다. 
SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO;
```

결과

```sql
DEPTNO EMPNO ENAME DNAME 
------ ----- ------ --------- 
20 7369 SMITH RESEARCH 
30 7499 ALLEN SALES 
...
```



### 2. NATURAL JOIN

- 두 테이블간의 동일한 이름을 갖는 모든 칼럼에대해 `=` join을 수행
- `using, on, where`에서 join을 수행 못함 `sql server`에서는 지원 안함

```mysql
SELECT DEPTNO, EMPNO, ENAME, DNAME FROM EMP NATURAL JOIN DEPT;
```

결과

```sql
DEPTNO EMPNO ENAME DNAME 
------ ------ ------ ------ 
20 7369 SMITH RESEARCH 
30 7499 ALLEN SALES 
...
```

- join에 사용된 `칼럼`들은 같은 데이터 유형이어야하며, `alias`나 테이블명과 같은 접두사를 못 씀

  - ```mysql
    SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP NATURAL JOIN DEPT; 
    ERROR: NATURAL JOIN에 사용된 열은 식별자를 가질 수 없음
    ```

- join이 되는 칼럼의 도메인이 일치해야함 `주의`

-  '*' 와일드카드처럼 별도의 칼럼 순서를 지정하지 않으면 NATURAL JOIN의 기준이 되는 칼럼 들이 다른 칼럼보다 먼저 출력된다. (ex: DEPTNO가 첫 번째 칼럼이 된다.) 

- 이때 NATURAL JOIN은 JOIN에 사용된 같은 이름의 칼럼을 하나로 처리한다.

  - natural

    ```sql
    DEPTNO EMPNO ENAME JOB MGR HIREDATE SAL COMM DNAME LOC 
    ----- ----- ----- -------- --- -------- ---- ---- --------- ------ 
    20 7369 SMITH CLERK 7902 1980-12-17 800 RESEARCH DALLAS 
    30 7499 ALLEN SALESMAN 7698 1981-02-20 1600 300 SALES CHICAGO
    ```

    

-  INNER JOIN의 경우 첫 번째 테이블, 두 번째 테이블의 칼럼 순서대로 데이터가 출력된다.

  - inner

    ```sql
    EMPNO ENAME JOB MGR HIREDATE SAL COMM DEPTNO DEPTNO DNAME LOC 
    ---- ----- ------ --- ------- --- ---- ----- ----- -------- ----- 
    7369 SMITH CLERK 7902 1980-12-17 800 20 20 RESEARCH DALLAS 
    7499 ALLEN SALESMAN 7698 1981-02-20 1600 300 30 30 SALES CHICAGO
    ```



### 3. using 조건절

- `natural join`에서는 이름이 같은 모든 칼럼을 기준으로 join
- 하지만 `using`을 사용하면 선택적으로 칼럼을 정함

```sql
SELECT * FROM DEPT JOIN DEPT_TEMP USING (DEPTNO);
```

- USING 조건절을 이용한 EQUI JOIN에서도 NATURAL JOIN과 마찬가지로 JOIN 칼럼에 대해서는 ALIAS나 테이블 이름과 같은 접두사를 붙일 수 없다. (DEPT.DEPTNO → DEPTNO)



### 4. on 조건절

- JOIN 서술부(ON 조건절)와 비 JOIN 서술부(WHERE 조건절)를 분리하여 이해가 쉬우며, 칼럼명이 다르더라도 JOIN 조건을 사용할 수 있는 장점이 있다.

```sql
SELECT E.EMPNO, E.ENAME, E.DEPTNO, D.DNAME FROM EMP E JOIN DEPT D ON (E.DEPTNO = D.DEPTNO);
```

