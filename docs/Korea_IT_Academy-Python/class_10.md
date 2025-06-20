# Class 10 - Python 라이브러리

### Python Library
라이브러리란 Python에서 기본적으로 제공되는 내장(표준) 라이브러리와 함께 pip을 사용해 설치를 하고 사용하는 외부 라이브러리 등 사용자의 환경에 맞게 다양한 기능을 제공합니다.  
기초적인 시스템 운영부터 데이터 분석, 크롤링, 전문 기술에 필요한 다양한 기능을 사용하기 위해 라이브러리 사용은 Python 개발에 있어 필수적인 요소로 자리잡고 있습니다.

- 사용 방법
    - from, import를 통해 기본적으로 제공되는 라이브러리 혹은 설치 된 라이브러리를 현재 Python script 혹은 환경으로 가져옵니다.
```py
from time import time
time()
```
### 외부 라이브러리의 사용 방법
외부 라이브러리의 경우 설치가 필요한 경우로 이때 주로 pip을 사용한다.

```bash

```

### os
Operating System의 약자로 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해줍니다.

- PATH 및 파일, 폴더 관리
```py
import os

# 운영 체제 확인
# posix : Unix 계열(Linux)
# nt : Window 계열
os.name

# 현재 경로 확인
os.getcwd()

# 해당 위치의 파일 및 폴더 리스트로 반환
os.listdir()

# 폴더(디렉토리) 생성
os.makedirs("new_directory")

# 폴더(디렉토리) 삭제
os.rmdir("new_directory")

# 파일 삭제
os.remove("file")

# 파일 또는 디렉토리 이름 변경
os.rename("old_name","new_name")

# 경로 존재 확인
# True / False 로 반환
os.path.exists("path")

# 경로 내 파일, 폴더 존재 유무 확인
# True / False 로 반환
os.path.isdir("path")
```

- OS 내 시스템 명령어 실행(CMD)
```py
os.system("echo Hello World")
```

### sys
파이썬 실행을 제어하는 기본 모듈

```py
import sys

# OS 플랫폼 확인
# win32 : Windows OS
# darwin : mac OS
# linux : Linux OS
sys.platform

# Get input parameter
# ex) python test.py "JeongSooNa" 10
sys.argv[0] # test.py
sys.argv[1] # "JeongSooNa"
sys.argv[2] # 10

# Python 종료
sys.exit()

```

### shutil
shutil은 파일을 복사(copy)하거나 이동(move)할 때 사용

```py
import shutil

shutil.copy("원본파일", "복사할위치(이름변경가능)")
shutil.move("원래위치", "이동할위치")
```

### glob
glob은 해당 경로에 있는 파일을 리스트로 만들어줍니다.

```py
import glob

# 현재 위치의 파일 리스트 반환
glob.glob("./")
```


