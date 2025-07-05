# Algorithm Study - Programmers 0단계 - 1

### 모음 제거

- 주어진 문자열에서 모음 제거

  - 모음 : "a","e","i","o","u"

- 문제 풀이

```py
def solution(my_string):
    for i in ["a","e","i","o","u"]:
        my_string = my_string.replace(i,"")
    return my_string
```

### 세균 증식

- 문제 설명
  어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

- 문제 풀이

```py
def solution(n, t):
    return n*(2**t)
```
