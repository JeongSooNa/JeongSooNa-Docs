# Class 13 - Python 예외처리

### try & except
try문 수행 중 오류가 발생하지 않는다면 except문은 수행되지 않는 구조.

- try-except문은 예외처리 혹은 디버깅을 위해 사용합니다.
- 코드 실행 시 에러가 발생할 것으로 예상되는 경우 try-except문을 사용해 정상 실행, 에러 발생 시 해당 부분을 넘어가며 except문에 명시한 코드를 동작할 수 있다.

- 예시
```py
try:
    num = int(input("숫자를 입력하시오."))
    print(10 / num)
except:
    print("오류가 발생했습니다.")
```

- Python에는 다양한 내장 예외처리 기능이 있어 except문 사용 시 특정 종류의 에러에 대한 대처 기능을 넣을 수 있다.

```py
try:
    a = 0
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)
```

### Error 종류
Error 발생 시 출력되는 에러 메세지를 확인 후 에러 종류에 따라 해결 방법을 쉽게 얻을 수 있다.  

- TypeError: 연산 또는 함수가 적절하지 않은 유형의 객체에 적용될 때 발생
    ```py
    "a" + 1
    ```
- ValueError: 함수 또는 연산에 인수가 올바른 유형이지만 적합하지 않은 값을 가지고 있을 때 발생
    ```py
    int("abc")
    ```
- NameError: 정의되지 않은 로컬 또는 전역 변수를 참조할 때 발생
    ```py
    print(none_definition_parameter)
    ```
- FileNotFoundError: 파일을 찾을 수 없을 때 발생
    ```py
    open("none_listed_file.txt")
    ```
- ZeroDivisionError: 0으로 나눗셈을 시도할 때 발생
    ```py
    4 / 0
    ```
- IndexError: 시퀀스(문자열, 리스트 등)의 인덱스가 범위를 벗어났을 때 발생
    ```py
    l = [1,2,3]
    print(l[3])
    ```
- KeyError: 사전(dictionary)에서 존재하지 않는 키를 검색할 때 발생
    ```py
    d = {"a":1}
    print(d["b"])
    ```
- ImportError: 모듈을 가져올 수 없을 때 발생
    ```py
    import JeongSooNa
    ```
- AttributeError: 객체에 정의되지 않은 속성에 접근하려고 할 때 발생
    ```py
    num = 10
    num.append(5)
    ```
- SyntaxError: 잘못된 구문으로 인해 발생
    ```py
    print("a)
    ```
- IndentationError: 들여쓰기가 잘못되었을 때 발생
    ```py
    if True:
    print("TRUE")
    ```