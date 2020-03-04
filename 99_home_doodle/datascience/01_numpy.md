[toc]

# 1. numpy 1강

## 파이썬 리스트를 통해 생성

`numpy` 모듈의 `array` 메소드에 파라미터로 파이썬 리스트를 넘겨주면 numpy array가 리턴됩니다.

```python
array1 = numpy.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
    
print(array1)
[ 2  3  5  7 11 13 17 19 23 29 31]
```

## 균일한 값으로 생성

`numpy` 모듈의 `full` 메소드를 사용하면, 모든 값이 같은 numpy array를 생성할 수 있습니다.

```python
array1 = numpy.full(6, 7)
    
print(array1)
[7 7 7 7 7 7]
```

### 모든 값이 0인 numpy array 생성

모든 값이 `0`인 numpy array를 생성하기 위해서는 `full` 메소드를 사용하면 되겠죠. 하지만 사실은 더 간편한 방법이 있습니다.

```python
array1 = numpy.full(6, 0)
array2 = numpy.zeros(6, dtype=int)
    
print(array1)
print()
print(array2)
[0 0 0 0 0 0]

[0 0 0 0 0 0]
```

### 모든 값이 1인 numpy array 생성

모든 값이 `1`인 numpy array를 생성하는 것도 비슷합니다. `zeros` 메소드 대신 `ones`를 사용하면 됩니다.

```python
array1 = numpy.full(6, 1)
array2 = numpy.ones(6, dtype=int)
    
print(array1)
print()
print(array2)
[1 1 1 1 1 1]

[1 1 1 1 1 1]
```

## 랜덤한 값들로 생성

어쩔 때는 임의의 값들로 배열을 생성시키고 싶습니다. 그럴 때는 `numpy`의 `random` 모듈의 `random` 함수를 사용하면 됩니다.

`numpy` 모듈 안에 `random`이라는 모듈이 있고, 그 안에 또 `random`이라는 함수가 있는 겁니다!

```python
array1 = numpy.random.random(6)
array2 = numpy.random.random(6)
    
print(array1)
print()
print(array2)
[0.42214929 0.45275673 0.57978413 0.61417065 0.39448558 0.03347601]

[0.42521953 0.65091589 0.94045742 0.18138103 0.27150749 0.8450694 ]
```

## 연속된 값들이 담긴 numpy array 생성

`numpy` 모듈의 `arange` 함수를 사용하면 연속된 값들이 담겨 있는 numpy array를 생성할 수 있습니다.

`arange` 함수는 파이썬의 기본 함수인 `range`와 굉장히 비슷한 원리로 동작하는데요. 파라미터가 1개인 경우, 2개인 경우, 3개인 경우 모두 살펴봅시다.

### 파라미터 1개

`arange(m)`을 하면 `0`부터 `m-1`까지의 값들이 담긴 numpy array가 리턴됩니다.

```python
array1 = numpy.arange(6)
print(array1)
[0 1 2 3 4 5]
```

### 파라미터 2개

`arange(n, m)`을 하면 `n`부터 `m-1`까지의 값들이 담긴 numpy array가 리턴됩니다.

```python
array1 = numpy.arange(2, 7)
print(array1)
[2 3 4 5 6]
```

### 파라미터 3개

`arange(n, m, s)`를 하면 `n`부터 `m-1`까지의 값들 중 간격이 `s`인 값들이 담긴 numpy array가 리턴됩니다.

```python
array1 = numpy.arange(3, 17, 3)
print(array1)
[ 3  6  9 12 15]
```



# 2.numpy 기본 통계 

## 최댓값, 최솟값

`max` 메소드와 `min` 메소드를 사용하면 numpy array의 최댓값과 최솟값을 구할 수 있습니다.

```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.max()) # 최댓값
print(array1.min()) # 최솟값
31
5
```

## 평균값

`mean` 메소드를 사용하면 numpy array의 평균값을 구할 수 있습니다.

```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.mean()) # 평균값
15.25
```

위 예시에서, 총합(14+6+13+21+23+31+9+514+6+13+21+23+31+9+5)을 총 개수(88)로 나누면 15.2515.25입니다.

## 중앙값

`median` 메소드를 사용하면 중간값을 구할 수 있는데요. 특이하게 `median`은 numpy array의 메소드가 아니라 numpy의 메소드입니다.

```python
import numpy as np

array1 = np.array([8, 12, 9, 15, 16])
array2 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(np.median(array1)) # 중앙값
print(np.median(array2)) # 중앙값
12.0
13.5
```

`array1`을 정렬하면 중앙값이 1212입니다.

`array2`에는 짝수개의 요소가 있기 때문에 중앙값이 1313과 1414 두 개입니다. 둘의 평균값을 내면 13.513.5입니다.

## 표준 편차, 분산

표준 편차와 분산은 값들이 평균에서 얼마나 떨어져 있는지 나타내는 지표입니다. 잘 모르신다면 일단 넘어가셔도 좋습니다.

```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.std()) # 표준 편차
print(array1.var()) # 분산
8.496322733983215
72.1875
```