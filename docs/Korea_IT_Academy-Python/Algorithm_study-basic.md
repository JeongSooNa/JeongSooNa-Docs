# Algorithm Study - Basic

### 다음 주어진 리스트에서 홀수만 전부 더하시오.
- input
```py
array = [1,4,5,7,8,9,12,15]
```

- 문제 풀이
```py
sum = 0
for i in array:
    if i & 2 == 1:
        sum += i
print(sum)
```

### 다음 문자열 내에서 주어진 문자열 인덱스에 해당하는 문자를 차례로 조합해 단어를 완성하시오.
- input
```py
string = "zpiaz"
index_list = [1,2,0,0,3]
```

- 문제 풀이
```py
result = ""
for i in index_list:
    result += string[i]
print(result)
```

### 구구단을 출력하시오.

- 문제 풀이
```py
for i in range(2,10):
    for j in range(1,10):
        print(str(i) + " x " + str(j) + " = " + str(i*j))
```

### 입력값(input)을 리스트로 받았을 때 제곱합을 반환(return)하는 함수를 작성하시오.
- input
```py
input = [1,2,3,4,5]
```
- 문제 풀이
<!--
```py
import math
def sumsq(a):
    result = 0
    for i in a:
        # 방법 1
        result += i * i
        # 방법 2
        #result += pow(i,2)
        # 방법 3
        #result += math.pow(i,2)
    return result
```
-->
