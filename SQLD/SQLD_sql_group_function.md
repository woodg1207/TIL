## SQLD_sql_group_function

### 1. ROLLUP

- `ROLLUP`에 지정된 칼럼의 리스트는 `Subtotal`을 생성하기 위해 사용

- n+1 level의 `Subtotal`이 생성됨

- `ROLLUP`의 인수는 계층 구조이므로 인수 순서가 바뀌면 수행 결과도 바뀌게 되므로 인수의 순서에도 주의해야 한다.

- 일반적인 `GROUP BY`절

  ```sql
  SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY DNAME, JOB;
  ```

  결과

  ```sql
  DNAME JOB Total Empl Total Sal 
  --------- -------- ------- ------- 
  SALES MANAGER 1 2850 
  SALES CLERK 1 950 
  ACCOUNTING MANAGER 1 2450
  ... 9개의 행이 나옴
  ```

  정렬을 위해선 따로 `ORDER BY`절을 사용해야함

- `ROLLUP`

  ```sql
  SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY ROLLUP (DNAME, JOB);
  ```

  결과

  ```sql
  DNAME JOB Total Empl Total Sal 
  ---------- -------- --------- -------- 
  SALES CLERK 1 950 
  SALES MANAGER 1 2850 
  SALES SALESMAN 4 5600 
  SALES 6 9400 
  RESEARCH CLERK 2 1900 
  RESEARCH ANALYST 2 6000 
  RESEARCH MANAGER 1 2975 
  RESEARCH 5 10875 
  ACCOUNTING CLERK 1 1300 
  ACCOUNTING MANAGER 1 2450 
  ACCOUNTING PRESIDENT 1 5000 
  ACCOUNTING 3 8750 
  14 29025  #13개의 행이 선택되었다.
  ```

  - 실행 결과에서 2개의 GROUPING COLUMNS(DNAME, JOB)에 대하여 다음과 같은 추가 LEVEL의 집계가 생성된 것을 볼 수 있다.

  - L1 - GROUP BY 수행시 생성되는 표준 집계 (9건) 

    L2 - DNAME 별 모든 JOB의 SUBTOTAL (3건)

    L3 - GRAND TOTAL (마지막 행, 1건)

  - 추가로 ROLLUP의 경우 계층 간 집계에 대해서는 LEVEL 별 순서(L1→L2→L3)를 정렬하지만, 

  - 계층 내 GROUP BY 수행시 생성되는 표준 집계에는 별도의 정렬을 지원하지 않는다. 

  - L1, L2, L3 계층 내 정렬을 위해서는 별도의 ORDER BY 절을 사용해야 한다.

- `ROLLUP`+`ORDER BY`

  ```sql
  SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT 
  WHERE DEPT.DEPTNO = EMP.DEPTNO 
  GROUP BY ROLLUP (DNAME, JOB) ORDER BY DNAME, JOB ;
  ```

  결과

  ```sql
  DNAME JOB Total Empl Total Sal 
  ------------ ------- -------- -------- 
  ACCOUNTING CLERK 1 1300 
  ACCOUNTING MANAGER 1 2450 
  ACCOUNTING PRESIDENT 1 5000 
  ACCOUNTING 3 8750 
  RESEARCH ANALYST 2 6000 
  RESEARCH CLERK 2 1900 
  RESEARCH MANAGER 1 2975 
  RESEARCH 5 10875 
  SALES CLERK 1 950 
  SALES MANAGER 1 2850 
  SALES SALESMAN 4 5600 
  SALES 6 9400 
  14 29025  #13개의 행이 선택되었다.
  ```

- `GROUPING` 함수 활용

  - `ROLLUP, CUBE, GROUPING SETS` 등 새로운 그룹 함수를 지원하기 위해 `GROUPING` 함수가 추가되었다.
  - ROLLUP이나 CUBE에 의한 소계가 계산된 결과에는 GROUPING(EXPR) = 1 이 표시되고, 
  - 그 외의 결과에는 GROUPING(EXPR) = 0 이 표시된다.
- GROUPING 함수와 CASE/DECODE를 이용해, 소계를 나타내는 필드에 원하는 문자열을 지정할 수 있어, 보고서 작성시 유용하게 사용할 수 있다.
  
  ```sql
  SELECT DNAME, GROUPING(DNAME), JOB, GROUPING(JOB), COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT 
  WHERE DEPT.DEPTNO = EMP.DEPTNO 
  GROUP BY ROLLUP (DNAME, JOB);
  ```
  
  결과
  
  ```sql
  DNAME GROUPING(DNAME) JOB GROUPING(JOB) Total Empl Total Sal
  ------ -------------- --- ----------- -------- ------ 
  SALES 0 CLERK 0 1 950 
  SALES 0 MANAGER 0 1 2850 
  SALES 0 SALESMAN 0 4 5600 
  SALES 0 1 6 9400 
  RESEARCH 0 CLERK 0 2 1900 
  RESEARCH 0 ANALYST 0 2 6000 
  RESEARCH 0 MANAGER 0 1 2975 
  RESEARCH 0 1 5 10875 
  ACCOUNTING 0 CLERK 0 1 1300 
  ACCOUNTING 0 MANAGER 0 1 2450 
  ACCOUNTING 0 PRESIDENT 0 1 5000 
  ACCOUNTING 0 1 3 8750 
  1 1 14 29025 #13개의 행이 선택되었다.
  ```
  
  - 부서별, 업무별과 전체 집계를 표시한 레코드에서는 GROUPING 함수가 1을 리턴한 것을 확인할 수 있다.
  - 전체 합계를 나타내는 결과 라인에서는 부서별 GROUPING 함수와 업무별 GROUPING 함수가 둘 다 1인 것을 알 수 있다.
  
- `GROUPING`+`CASE`

  ```sql
  SELECT 
  	CASE GROUPING(DNAME) 
  		WHEN 1 THEN 'All Departments' 
  		ELSE DNAME 
  	END AS DNAME, 
  	CASE GROUPING(JOB) 
  		WHEN 1 THEN 'All Jobs' 
  		ELSE JOB 
  	END AS JOB, 
  	COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT 
  WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY ROLLUP (DNAME, JOB); 
  --Oracle의 경우는 DECODE 함수를 사용해서 좀더 짧게 표현할 수 있다. 
  SELECT DECODE(GROUPING(DNAME), 1, 'All Departments', DNAME) AS DNAME, DECODE(GROUPING(JOB), 1, 'All Jobs', JOB) AS JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY ROLLUP (DNAME, JOB);
  ```

  결과

  ```sql
  DNAME JOB Total Empl Total Sal 
  ----------- -------- -------- -------- 
  SALES CLERK 1 950 
  SALES MANAGER 1 2850 
  SALES SALESMAN 4 5600 
  SALES All Jobs 6 9400 
  RESEARCH CLERK 2 1900 
  RESEARCH ANALYST 2 6000 
  RESEARCH MANAGER 1 2975 
  RESEARCH All Jobs 5 10875 
  ACCOUNTING CLERK 1 1300 
  ACCOUNTING MANAGER 1 2450 
  ACCOUNTING PRESIDENT 1 5000 
  ACCOUNTING All Jobs 3 8750 
  All Departments All Jobs 14 29025 --13개의 행이 선택되었다.
  ```

  - 부서별과 전체 집계를 표시한 레코드에서 `ALL JOBS`와 `ALL DEPARTMENTS`라는 사용자 정의 텍스트를 확인할 수 있다. 일
  - 부 DBMS는 GROUPING_ID라는 비슷한 용도의 함수를 추가로 사용할 수도 있으므로 참조하기 바란다.

- `ROLLUP` 일부 사용

  - GROUP BY ROLLUP (DNAME, JOB) 조건에서 GROUP BY DNAME, ROLLUP(JOB) 조건으로 변경

  ```sql
  SELECT 
  	CASE GROUPING(DNAME) 
  		WHEN 1 THEN 'All Departments' 
  		ELSE DNAME 
  	END AS DNAME, 
  	CASE GROUPING(JOB) 
  		WHEN 1 THEN 'All Jobs' 
  		ELSE JOB 
  	END AS JOB, 
  COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO 
  GROUP BY DNAME, ROLLUP(JOB)
  ```

  ```sql
  DNAME JOB Total Empl Total Sal 
  ----------- -------- -------- -------- 
  SALES CLERK 1 950 
  SALES MANAGER 1 2850 
  SALES SALESMAN 4 5600 
  SALES All Jobs 6 9400 
  RESEARCH CLERK 2 1900 
  RESEARCH ANALYST 2 6000 
  RESEARCH MANAGER 1 2975 
  RESEARCH All Jobs 5 10875 
  ACCOUNTING CLERK 1 1300 
  ACCOUNTING MANAGER 1 2450 
  ACCOUNTING PRESIDENT 1 5000 
  ACCOUNTING All Jobs 3 8750 --12개의 행이 선택되었다.
  ```

  - 마지막 ALL DEPARTMENTS & ALL JOBS 줄만 계산이 되지 않았다. ROLLUP이 JOB 칼럼에만 사용되었기 때문에 DNAME에 대한 집계는 필요하지 않기 때문이다.

- `ROLLUP` 함수 결합 칼럼 사용

  ```sql
  SELECT DNAME, JOB, MGR, SUM(SAL) "Total Sal" FROM EMP, DEPT 
  WHERE DEPT.DEPTNO = EMP.DEPTNO 
  GROUP BY ROLLUP (DNAME, (JOB, MGR)); 
  -- JOB, MGR을 소계시 하나의 집합으로 간주하여 구분하지 않음
  ```

  ```sql
  DNAME JOB MGR Total Sal 
  --------- --------- ---- ------ 
  SALES CLERK 7698 950 
  SALES MANAGER 7839 2850 
  SALES SALESMAN 7698 5600 
  SALES 9400 
  RESEARCH CLERK 7788 1100 
  RESEARCH CLERK 7902 800 
  RESEARCH ANALYST 7566 6000 
  RESEARCH MANAGER 7839 2975 
  RESEARCH 10875 
  ACCOUNTING CLERK 7782 1300 
  ACCOUNTING MANAGER 7839 2450 
  ACCOUNTING PRESIDENT 5000 
  ACCOUNTING 8750 29025 --14개의 행이 선택되었다.
  ```

  - ROLLUP 함수 사용시 괄호로 묶은 JOB과 MGR의 경우 하나의 집합(JOB+MGR) 칼럼으로 간주하여 괄호 내 각 칼럼별 집계를 구하지 않는다.

### 2. CUBE 함수

- `ROLLUP`에서는 단지 가능한 Subtotal만을 생성하였지만, 

- `CUBE`는 결합 가능한 모든 값에 대하여 다차원 집계를 생성한다. 

- CUBE를 사용할 경우에는 내부적으로는 Grouping Columns의 순서를 바꾸어서 또 한 번의 Query를 추가 수행해야 한다. 뿐만 아니라 Grand Total은 양쪽의 Query 에서 모두 생성이 되므로 한 번의 Query에서는 제거되어야만 하므로 ROLLUP에 비해 시스템의 연산 대상이 많다. 

- 이처럼 Grouping Columns이 가질 수 있는 모든 경우에 대하여 Subtotal을 생성해야 하는 경우에는 CUBE를 사용하는 것이 바람직하나, ROLLUP에 비해 시스템에 많은 부담을 주므로 사용에 주의해야 한다.

- CUBE 함수의 경우 표시된 인수들에 대한 계층별 집계를 구할 수 있으며, 이때 표시된 인수들 간에는 계층 구조인 ROLLUP과는 달리 평등한 관계이므로 인수의 순서가 바뀌는 경우 행간에 정렬 순서는 바뀔 수 있어도 데이터 결과는 같다. 그리고 CUBE도 결과에 대한 정렬이 필요한 경우는 `ORDER BY` 절에 명시적으로 정렬 칼럼이 표시가 되어야 한다.

- `CUBE`함수 이용

  ```sql
  SELECT 
  	CASE GROUPING(DNAME) 
  		WHEN 1 THEN 'All Departments' 
  		ELSE DNAME 
  	END AS DNAME, 
  	CASE GROUPING(JOB) 
  		WHEN 1 THEN 'All Jobs' 
  		ELSE JOB 
  	END AS JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO 
  GROUP BY CUBE (DNAME, JOB) ;
  ```

  ```sql
  DNAME JOB Total Empl Total Sal 
  ------------- --------- --------- -------- 
  All Departments All Jobs 14 29025 
  All Departments CLERK 4 4150 
  All Departments ANALYST 2 6000 
  All Departments MANAGER 3 8275 
  All Departments SALESMAN 4 5600 
  All Departments PRESIDENT 1 5000 
  SALES All Jobs 6 9400 
  SALES CLERK 1 950 
  SALES MANAGER 1 2850 
  SALES SALESMAN 4 5600 
  RESEARCH All Jobs 5 10875 
  RESEARCH CLERK 2 1900 
  RESEARCH ANALYST 2 6000 
  RESEARCH MANAGER 1 2975 
  ACCOUNTING All Jobs 3 8750 
  ACCOUNTING CLERK 1 1300 
  ACCOUNTING MANAGER 1 2450 
  ACCOUNTING PRESIDENT 1 5000 --18개의 행이 선택되었다.
  ```

  - CUBE는 GROUPING COLUMNS이 가질 수 있는 모든 경우의 수에 대하여 Subtotal을 생성하므로 GROUPING COLUMNS의 수가 N이라고 가정하면, 2의 N승 LEVEL의 Subtotal을 생성하게 된다. 
  - 실행 결과에서 CUBE 함수 사용으로 ROLLUP 함수의 결과에다 업무별 집계까지 추가해서 출력할 수 있는데, ROLLUP 함수에 비해 업무별 집계를 표시한 5건의 레코드가 추가된 것을 확인할 수 있다. 
  - (All Departments - CLERK, ANALYST, MANAGER, SALESMAN, PRESIDENT 별 집계가 5건 추가되었다.)

- `UNION ALL` 사용 SQL

  - UNION ALL은 Set Operation 내용으로, 여러 SQL 문장을 연결하는 역할을 할 수 있다. 위 SQL은 첫 번째 SQL 모듈부터 차례대로 결과가 나오므로 위 CUBE SQL과 결과 데이터는 같으나 행들의 정렬은 다를 수 있다.

  ```SQL
  SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY DNAME, JOB 
  UNION ALL 
  SELECT DNAME, 'All Jobs', COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY DNAME 
  UNION ALL 
  SELECT 'All Departments', JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY JOB 
  UNION ALL 
  SELECT 'All Departments', 'All Jobs', COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO ;
  ```

  - CUBE 함수를 사용하면서 가장 크게 개선되는 부분은 CUBE 사용 전 SQL에서 EMP, DEPT 테이블을 네 번이나 반복 액세스하는 부분을 CUBE 사용 SQL에서는 한 번으로 줄일 수 있는 부분이다. 기존에 같은 테이블을 네 번 액세스하는 이유가 되었던 부서와 업무별 소계와 총계 부분을 CUBE 함수를 사용함으로써 한 번의 액세스만으로 구현한다. 결과적으로 수행속도 및 자원 사용율을 개선할 수 있으며, SQL 문장도 더 짧아졌으므로 가독성도 높아졌다. 실행 결과는 STEP5의 결과와 동일하다. ROLLUP 함수도 똑 같은 개선 효과를 얻을 수 있다.

### 3. GROUPING SETS 함수

- `GROUPING SETS`를 이용해 더욱 다양한 소계 집합을 만들 수 있는데, GROUP BY SQL 문장을 여러 번 반복하지 않아도 원하는 결과를 쉽게 얻을 수 있게 되었다. 

- GROUPING SETS에 표시된 인수들에 대한 개별 집계를 구할 수 있으며, 이때 표시된 인수들 간에는 계층 구조인 ROLLUP과는 달리 평등한 관계이므로 인수의 순서가 바뀌어도 결과는 같다. 

- GROUPING SETS 함수도 결과에 대한 정렬이 필요한 경우는 `ORDER BY`절에 명시적으로 정렬 칼럼이 표시가 되어야 한다.

  ```sql
  SELECT DNAME, 'All Jobs' JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY DNAME 
  UNION ALL 
  SELECT 'All Departments' DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY JOB ;
  ```

  ```sql
  DNAME JOB Total Empl Total Sal 
  ---------- ------- -------- ------ 
  ACCOUNTING All Jobs 3 8750 
  RESEARCH All Jobs 5 10875 
  SALES All Jobs 6 9400 
  All Departments CLERK 4 4150 
  All Departments SALESMAN 4 5600 
  All Departments PRESIDENT 1 5000 
  All Departments MANAGER 3 8275 
  All Departments ANALYST 2 6000 --8개의 행이 선택되었다.
  ```

  

