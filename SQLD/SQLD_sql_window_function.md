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

- 