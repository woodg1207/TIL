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
  	ELSE DNAME END AS DNAME, 
  	CASE GROUPING(JOB) 
  		WHEN 1 THEN 'All Jobs' 
  	ELSE JOB END AS JOB, 
  	COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT 
  WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY ROLLUP (DNAME, JOB); 
  Oracle의 경우는 DECODE 함수를 사용해서 좀더 짧게 표현할 수 있다. 
  SELECT DECODE(GROUPING(DNAME), 1, 'All Departments', DNAME) AS DNAME, DECODE(GROUPING(JOB), 1, 'All Jobs', JOB) AS JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
  FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY ROLLUP (DNAME, JOB);
  ```

  

