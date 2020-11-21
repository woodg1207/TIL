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

- ON 조건절을 사용한 JOIN의 경우는 ALIAS나 테이블 명과 같은 접두사를 사용하여 SELECT에 사용되는 칼럼을 논리적으로 명확하게 지정해주어야 한다. (DEPTNO → E.DEPTNO)

##### 4-1 where 절과의 혼용

```sql
SELECT E.ENAME, E.DEPTNO, D.DEPTNO, D.DNAME FROM EMP E JOIN DEPT D ON (E.DEPTNO = D.DEPTNO) WHERE E.DEPTNO = 30;
```

##### 4-2 on + 데이터 검증

- ON 조건절에 JOIN 조건 외에도 데이터 검색 조건을 추가할 수는 있으나, 검색 조건 목적인 경우는 WHERE 절을 사용할 것을 권고한다. 
- 다만, `아우터 조인`에서 `조인의 대상을 제한`하기 위한 목적으로 사용되는 추가 조건의 경우는 ON 절에 표기되어야 한다.

```sql
SELECT E.ENAME, E.MGR, D.DEPTNO, D.DNAME FROM EMP E JOIN DEPT D ON (E.DEPTNO = D.DEPTNO AND E.MGR = 7698); 

위 SQL과 아래 SQL은 같은 결과를 얻을 수 있다. 

SELECT E.ENAME, E.MGR, D.DEPTNO, D.DNAME FROM EMP E JOIN DEPT D ON (E.DEPTNO = D.DEPTNO) WHERE E.MGR = 7698;
```

##### 4-3 ex)

```sql
SELECT TEAM_NAME, TEAM.STADIUM_ID, STADIUM_NAME FROM TEAM JOIN STADIUM ON TEAM.STADIUM_ID = STADIUM.STADIUM_ID ORDER BY STADIUM_ID;

위 SQL은 STADIUM_ID라는 공통된 칼럼이 있기 때문에 아래처럼 USING 조건절로 구현할 수도 있다. 

SELECT TEAM_NAME, STADIUM_ID, STADIUM_NAME FROM TEAM JOIN STADIUM USING (STADIUM_ID) ORDER BY STADIUM_ID; 

위 SQL은 고전적인 방식인 WHERE 절의 INNER JOIN으로 구현할 수도 있다. 

SELECT TEAM_NAME, TEAM.STADIUM_ID, STADIUM_NAME FROM TEAM, STADIUM WHERE TEAM.STADIUM_ID = STADIUM.STADIUM_ID ORDER BY STADIUM_ID

```

##### 4-4 다중 테이블 join

```sql
SELECT E.EMPNO, D.DEPTNO, D.DNAME, T.DNAME New_DNAME FROM EMP E JOIN DEPT D 
	ON (E.DEPTNO = D.DEPTNO) JOIN DEPT_TEMP T 
	ON (E.DEPTNO = T.DEPTNO); 
위 SQL은 고전적인 방식인 WHERE 절의 INNER JOIN으로 구현할 수도 있다. 
SELECT E.EMPNO, D.DEPTNO, D.DNAME, T.DNAME New_DNAME FROM EMP E, DEPT D, DEPT_TEMP T 
WHERE E.DEPTNO = D.DEPTNO AND E.DEPTNO = T.DEPTNO;
```

```sql
SELECT P.PLAYER_NAME 선수명, P.POSITION 포지션, T.REGION_NAME 연고지명, T.TEAM_NAME 팀명, S.STADIUM_NAME 구장명 FROM PLAYER P JOIN TEAM T 
	ON P.TEAM_ID = T.TEAM_ID JOIN STADIUM S 
	ON T.STADIUM_ID = S.STADIUM_ID 
WHERE P.POSITION = 'GK' 
ORDER BY 선수명; 

위 SQL은 고전적인 방식인 WHERE 절의 INNER JOIN으로 구현할 수도 있다.

SELECT P.PLAYER_NAME 선수명, P.POSITION 포지션, T.REGION_NAME 연고지명, T.TEAM_NAME 팀명, S.STADIUM_NAME 구장명 FROM PLAYER P, TEAM T, STADIUM S 
WHERE P.TEAM_ID = T.TEAM_ID AND T.STADIUM_ID = S.STADIUM_ID AND P.POSITION = 'GK' 
ORDER BY 선수명;
```

```sql
SELECT ST.STADIUM_NAME, SC.STADIUM_ID, SCHE_DATE, HT.TEAM_NAME, AT.TEAM_NAME, HOME_SCORE, AWAY_SCORE 
FROM SCHEDULE SC JOIN STADIUM ST 
	ON SC.STADIUM_ID = ST.STADIUM_ID JOIN TEAM HT 
	ON SC.HOMETEAM_ID = HT.TEAM_ID JOIN TEAM AT 
	ON SC.AWAYTEAM_ID = AT.TEAM_ID 
WHERE HOME_SCORE > = AWAY_SCORE +3; 

위 SQL은 고전적인 방식인 WHERE 절의 INNER JOIN으로 구현할 수도 있다. 

SELECT ST.STADIUM_NAME, SC.STADIUM_ID, SCHE_DATE, HT.TEAM_NAME, AT.TEAM_NAME, HOME_SCORE, AWAY_SCORE FROM SCHEDULE SC, STADIUM ST, TEAM HT, TEAM AT 
WHERE HOME_SCORE> = AWAY_SCORE +3 AND SC.STADIUM_ID = ST.STADIUM_ID AND SC.HOMETEAM_ID = HT.TEAM_ID AND SC.AWAYTEAM_ID = AT.TEAM_ID; 

FROM 절에 4개의 테이블이 JOIN에 참여하였으며, HOME TEAM과 AWAY TEAM의 팀 이름을 구하기 위해 TEAM 테이블을 HT와 AT 두 개의 ALIAS로 구분하였다.
```



### 5. cross join

- CROSS JOIN은 E.F.CODD 박사가 언급한 일반 집합 연산자의 `PRODUCT`의 개념으로 테이블 간 JOIN 조건이 없는 경우 생길 수 있는 모든 데이터의 조합을 말한다. 
- 두 개의 테이블에 대한 CARTESIAN PRODUCT 또는 CROSS PRODUCT와 같은 표현으로, 결과는 양쪽 집합의 `M*N` 건의 데이터 조합이 발생한다. 

```sql
SELECT ENAME, DNAME FROM EMP CROSS JOIN DEPT ORDER BY ENAME;
```

- NATURAL JOIN의 경우 WHERE 절에서 JOIN 조건을 추가할 수 없지만, CROSS JOIN의 경우 WHERE 절에 JOIN 조건을 추가할 수 있다. 
- 그러나, 이 경우는 CROSS JOIN이 아니라 INNER JOIN과 같은 결과를 얻기 때문에 CROSS JOIN을 사용하는 의미가 없어지므로 권고하지 않는다.

```sql
SELECT ENAME, DNAME FROM EMP CROSS JOIN DEPT WHERE EMP.DEPTNO = DEPT.DEPTNO; 

위 SQL과 아래 SQL은 같은 결과를 얻을 수 있다. 

SELECT ENAME, DNAME FROM EMP INNER JOIN DEPT WHERE EMP.DEPTNO = DEPT.DEPTNO;
```



### 6. outer join

- INNER(내부) JOIN과 대비하여 OUTER(외부) JOIN이라고 불리며, JOIN 조건에서 동일한 값이 없는 행도 반환할 때 사용할 수 있다.

