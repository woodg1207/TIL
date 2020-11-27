# Window_function

```sql
SELECT WINDOW_FUNCTION (ARGUMENTS) OVER ( [PARTITION BY 칼럼] [ORDER BY 절] [WINDOWING 절] ) FROM 테이블 명;
```

- WINDOW_FUNCTION : 기존에 사용하던 함수도 있고, 새롭게 WINDOW 함수용으로 추가된 함수도 있다. 
- ARGUMENTS (인수) : 함수에 따라 0 ~ N개의 인수가 지정될 수 있다. 
- PARTITION BY 절 : 전체 집합을 기준에 의해 소그룹으로 나눌 수 있다. 
- ORDER BY 절 : 어떤 항목에 대해 순위를 지정할 지 ORDER BY 절을 기술한다. 
- WINDOWING 절 : WINDOWING 절은 함수의 대상이 되는 행 기준의 범위를 강력하게 지정할 수 있다. ROWS는 물리적인 결과 행의 수를, RANGE는 논리적인 값에 의한 범위를 나타내는데, 둘 중의 하나를 선택해서 사용할 수 있다. 다만, WINDOWING 절은 SQL Server에서는 지원하지 않는다.

### 1. 그룹 내 순위 함수

1. `RANK` 함수

- `ORDER BY`를 포함한 QUERY 문에서 특정 항목(칼럼)에 대한 순위를 구하는 함수

```sql
SELECT JOB, ENAME, SAL, 
	RANK( ) OVER (ORDER BY SAL DESC) ALL_RANK, 
	RANK( ) OVER (PARTITION BY JOB ORDER BY SAL DESC) JOB_RANK 
FROM EMP;
```

```sql
JOB ENAME SAL ALL_RANK JOB_RANK 
-------- ----- ---- -------- ------- 
PRESIDENT KING 5000 1 1 
ANALYST FORD 3000 2 1 
ANALYST SCOTT 3000 2 1 
MANAGER JONES 2975 4 1 
MANAGER BLAKE 2850 5 2 
MANAGER CLARK 2450 6 3 
SALESMAN ALLEN 1600 7 1 
SALESMAN TURNER 1500 8 2 
CLERK MILLER 1300 9 1 
SALESMAN WARD 1250 10 3 
SALESMAN MARTIN 1250 10 3 
CLERK ADAMS 1100 12 2 
CLERK JAMES 950 13 3 
CLERK SMITH 800 14 4 --13개의 행이 선택되었다.
```

- 업무 구분이 없는 ALL_RANK 칼럼에서 FORD와 SCOTT, WARD와 MARTIN은 동일한 SALARY이므로 같은 순위를 부여한다. 그리고 업무를 PARTITION으로 구분한 JOB_RANK의 경우 같은 업무 내 범위에서만 순위를 부여한다. 
- 하나의 SQL 문장에 ORDER BY SAL DESC 조건과 PARTITION BY JOB 조건이 충돌이 났기 때문에 JOB 별로는 정렬이 되지 않고, ORDER BY SAL DESC 조건으로 정렬이 되었다.

2. `DENSE_RANK` 함수

- 동일한 순위를 하나의 건수로 취급하는 것이 틀린 점이다.

```sql
SELECT JOB, ENAME, SAL, 
	RANK( ) OVER (ORDER BY SAL DESC) RANK, 
	DENSE_RANK( ) OVER (ORDER BY SAL DESC) DENSE_RANK FROM EMP;
```

```sql
JOB ENAME SAL RANK DENSE_RANK 
---------- ------ ---- ---- --------- 
PRESIDENT KING 5000 1 1 
ANALYST FORD 3000 2 2 
ANALYST SCOTT 3000 2 2 
MANAGER JONES 2975 4 3 ######
MANAGER BLAKE 2850 5 4 
MANAGER CLARK 2450 6 5 
SALESMAN ALLEN 1600 7 6 
SALESMAN TURNER 1500 8 7 CLERK MILLER 1300 9 8 SALESMAN WARD 1250 10 9 SALESMAN MARTIN 1250 10 9 CLERK ADAMS 1100 12 10 CLERK JAMES 950 13 11 CLERK SMITH 800 14 12 --13개의 행이 선택되었다.
```

- FORD와 SCOTT, WARD와 MARTIN은 동일한 SALARY이므로 RANK와 DENSE_RANK 칼럼에서 모두 같은 순위를 부여한다. 
- 그러나 RANK와 DENSE_RANK의 차이를 알 수 있는 데이터는 FORD와 SCOTT의 다음 순위인 JONES의 경우 RANK는 4등으로 DENSE_RANK는 3등으로 표시되어 있다. 
- 마찬가지로 WARD와 MARTIN의 다음 순위인 ADAMS의 경우 RANK는 12등으로 DENSE_RANK는 10등으로 표시되어 있다.

3. `ROW_NUMBER` 함수

- `ROW_NUMBER` 함수는 `RANK`나 `DENSE_RANK` 함수가 동일한 값에 대해서는 동일한 순위를 부여하는데 반해, 동일한 값이라도 고유한 순위를 부여한다.

```sql
SELECT JOB, ENAME, SAL, 
	RANK( ) OVER (ORDER BY SAL DESC) RANK, 
	ROW_NUMBER() OVER (ORDER BY SAL DESC) ROW_NUMBER FROM EMP;
```

```sql
JOB ENAME SAL RANK ROW_NUMBER 
--------- ------ ----- ----- ---------- 
PRESIDENT KING 5000 1 1 
ANALYST FORD 3000 2 2 
ANALYST SCOTT 3000 2 3 #####
MANAGER JONES 2975 4 4 
MANAGER BLAKE 2850 5 5 MANAGER CLARK 2450 6 6 SALESMAN ALLEN 1600 7 7 SALESMAN TURNER 1500 8 8 CLERK MILLER 1300 9 9 SALESMAN WARD 1250 10 10 SALESMAN MARTIN 1250 10 11 CLERK ADAMS 1100 12 12 CLERK JAMES 950 13 13 CLERK SMITH 800 14 14 14개의 행이 선택되었다.
```

- FORD와 SCOTT, WARD와 MARTIN은 동일한 SALARY이므로 RANK는 같은 순위를 부여했지만, ROW_NUMBER의 경우 동일한 순위를 배제하기 위해 유니크한 순위를 정한다. 
- 위 경우는 같은 SALARY에서는 어떤 순서가 정해질지 알 수 없다. 
- (Oracle의 경우 rowid가 적은 행이 먼저 나온다) 이 부분은 데이터베이스 별로 틀린 결과가 나올 수 있으므로, 만일 동일 값에 대한 순서까지 관리하고 싶으면 
- `ROW_NUMBER( ) OVER (ORDER BY SAL DESC, ENAME)` 같이 ORDER BY 절을 이용해 추가적인 정렬 기준을 정의해야 한다.

### 2. 집계함수

생략

### 3. 그룹 내 행 순서 함수

1. `FIRST_VALUE` 함수

- FIRST_VALUE 함수를 이용해 파티션별 윈도우에서 가장 먼저 나온 값을 구한다. SQL Server에서는 지원하지 않는 함수이다. MIN 함수를 활용하여 같은 결과를 얻을 수도 있다.

```sql
SELECT DEPTNO, ENAME, SAL, 
	FIRST_VALUE(ENAME) OVER (PARTITION BY DEPTNO ORDER BY SAL DESC ROWS UNBOUNDED PRECEDING) as DEPT_RICH 
FROM EMP; RANGE UNBOUNDED PRECEDING : 현재 행을 기준으로 파티션 내의 첫 번째 행까지의 범위를 지정한다.
```

```sql
DEPTNO ENAME SAL DEPT_RICH 
------ ------- ---- -------- 
10 KING 5000 KING 10 CLARK 2450 KING 10 MILLER 1300 KING 20 SCOTT * 3000 SCOTT 20 FORD * 3000 SCOTT 20 JONES 2975 SCOTT 20 ADAMS 1100 SCOTT 20 SMITH 800 SCOTT 30 BLAKE 2850 BLAKE 30 ALLEN 1600 BLAKE 30 TURNER 1500 BLAKE 30 MARTIN 1250 BLAKE 30 WARD 1250 BLAKE 30 JAMES 950 BLAKE 14개의 행이 선택되었다.
```

