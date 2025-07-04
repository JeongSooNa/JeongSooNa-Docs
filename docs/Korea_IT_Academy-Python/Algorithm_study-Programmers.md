# Algorithm Study - Programmers

### 옷가게 할인 받기

- 문제 설명

머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.  
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

- 제한사항
    - 10 ≤ price ≤ 1,000,000
    - price는 10원 단위로(1의 자리가 0) 주어집니다.
    - 소수점 이하를 버린 정수를 return합니다.

- 입출력 예
    - 150,000원에서 5%를 할인한 142,500원을 return 합니다.
    - 580,000원에서 20%를 할인한 464,000원을 return 합니다.

- 문제 풀이

<!--
```py
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price
```
-->

### 배열 뒤집기

- 문제 설명

정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

- 제한사항
    - 1 ≤ num_list의 길이 ≤ 1,000
    - 0 ≤ num_list의 원소 ≤ 1,000

- 입출력 예
    - num_list가 [1, 2, 3, 4, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 4, 3, 2, 1]을 return합니다.
    - num_list가 [1, 1, 1, 1, 1, 2]이므로 순서를 거꾸로 뒤집은 배열 [2, 1, 1, 1, 1, 1]을 return합니다.
    - num_list가 [1, 0, 1, 1, 1, 3, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 3, 1, 1, 1, 0, 1]을 return합니다.

- 문제 풀이

<!--
```py
def solution(num_list):
    if len(num_list)%2 == 0:
        for i in range(0,int(len(num_list)/2)):
            tmp = num_list[i]
            num_list[i] = num_list[-(i+1)]
            num_list[-(i+1)] = tmp
    else:
        for i in range(0,int((len(num_list)-1)/2)):
            tmp = num_list[i]
            num_list[i] = num_list[-(i+1)]
            num_list[-(i+1)] = tmp  
    return num_list
```
-->

### 다음에 올 숫자

- 문제 설명

등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

- 제한사항
    - 2 < common의 길이 < 1,000
    - -1,000 < common의 원소 < 2,000
    - common의 원소는 모두 정수입니다.
    - 등차수열 혹은 등비수열이 아닌 경우는 없습니다.
    - 등비수열인 경우 공비는 0이 아닌 정수입니다.

- 입출력 예
    - [1, 2, 3, 4]는 공차가 1인 등차수열이므로 다음에 올 수는 5이다.
    - [2, 4, 8]은 공비가 2인 등비수열이므로 다음에 올 수는 16이다.

- 문제 풀이

<!--
```py
def solution(common):
    flag = False
    if common[2] - common[1] == common[1] - common[0]:
        flag = True
    if flag:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] / common[0])
```
-->

### 옹알이 (1)

- 문제 설명

머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.  
문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

- 제한사항
    - 1 ≤ babbling의 길이 ≤ 100
    - 1 ≤ babbling[i]의 길이 ≤ 15
    - babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
    - 즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.
    - 문자열은 알파벳 소문자로만 이루어져 있습니다.

- 입출력 예
    - ["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.
    - ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 3을 return합니다.

- 유의사항
    - 네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.

- 문제 풀이

<!--
```py
def solution(babbling):
    answer = 0
    s = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in s:
            i = i.replace(j,"_")
        for j in range(0,len(i)):
            if not i[j] == "_":
                break
            if j == (len(i)-1):
                answer += 1
    return answer
```
-->

- Issue

<!--
    1. "wyeoo"의 경우 "ye"를 replace 한 후 "woo"가 되어 이 후 ""로 바뀌어 결과에 영향을 미칠 수 있다.
    ```py
    def solution(babbling):
        answer = 0
        s = ["aya", "ye", "woo", "ma"]
        for i in babbling:
            for j in s:
                i = i.replace(j,"")
            #print(i)
            if i == "":
                answer += 1
        return answer
    ```

    2. python에서 ```str.replace()``` 함수는 해당 문자열을 직접 변경하는 것이 아닌 replace값을 반환하는 함수로, 원래 문자열의 변경을 원할 경우 ```i = i.replace()``` 형식으로 코드를 작성해야한다.
-->
