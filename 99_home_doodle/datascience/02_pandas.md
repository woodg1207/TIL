[TOC]

# 01. pandas

## From list of lists, array of arrays, list of series

2차원 리스트나 2차원 numpy array로 DataFrame을 만들 수 있습니다. 심지어 pandas Series를 담고 있는 리스트로도 DataFrame을 만들 수 있습니다.

따로 column과 row(index)에 대한 설정이 없으면 그냥 0, 1, 2, ... 순서로 값이 매겨집니다.

```python
import numpy as np
import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
    pd.Series(['dongwook', 50, 86]), 
    pd.Series(['sineui', 89, 31]), 
    pd.Series(['ikjoong', 68, 91]), 
    pd.Series(['yoonsoo', 88, 75])
]

# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)

print(df1)
          0   1   2
0  dongwook  50  86
1    sineui  89  31
2   ikjoong  68  91
3   yoonsoo  88  75
```

## From dict of lists, dict of arrays, dict of series

파이썬 사전(dictionary)으로도 DataFrame을 만들 수 있습니다.

사전의 key로는 column 이름을 쓰고, 그 column에 해당하는 리스트, numpy array, 혹은 pandas Series를 사전의 value로 넣어주면 됩니다.

```python
import numpy as np
import pandas as pd

names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name': names, 
    'english_score': english_scores, 
    'math_score': math_scores
}

dict2 = {
    'name': np.array(names), 
    'english_score': np.array(english_scores), 
    'math_score': np.array(math_scores)
}

dict3 = {
    'name': pd.Series(names), 
    'english_score': pd.Series(english_scores), 
    'math_score': pd.Series(math_scores)
}


# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)

print(df1)
       name  english_score  math_score
0  dongwook             50          86
1    sineui             89          31
2   ikjoong             68          91
3   yoonsoo             88          75
```

## From list of dicts

리스트가 담긴 사전이 아니라, 사전이 담긴 리스트로도 DataFrame을 만들 수 있습니다.

```python
import numpy as np
import pandas as pd

my_list = [
    {'name': 'dongwook', 'english_score': 50, 'math_score': 86},
    {'name': 'sineui', 'english_score': 89, 'math_score': 31},
    {'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
    {'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
]

df = pd.DataFrame(my_list)
print(df)
   english_score  math_score      name
0             50          86  dongwook
1             89          31    sineui
2             68          91   ikjoong
3             88          75   yoonsoo
```