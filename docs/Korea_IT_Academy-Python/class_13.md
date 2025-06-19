# Class 13 - Python 예외처리

### try & except
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

### UPDATING...