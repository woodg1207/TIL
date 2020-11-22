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

  ```sql
  
  ```

  