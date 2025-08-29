# Class 2- R Path 이해

### PATH

- R에서도 운영체제 명령어와 같이 파일, 폴더 등 시스템 관리가 가능.
- 프로젝트의 library를 생성하고, 관련 파일을 관리하면 편리.

- R 설치 경로 확인
```r
R.home()
```

- working 디렉토리 확인 및 설정 
```r
getwd()
setwd('river/')
```

- 라이브러리(패키지)가 저장되어 있는 경로 확인
```r
.libPaths()
```

- 새로운 디렉터리 만들기 
```r
dir.create("test")
```

- 디렉터리 존재 여부 확인
```r
dir.exists("./")
```

- 운영체제에 따라서 자동으로 경로 표시 해줌 
```r
normalizePath("./")
```

- R 시스템 파일 접근하기
```r
system.file()
```

- 경로에서 파일이름과 디렉토리경로 분리하기
```r
basename("./")
dirname("./")
```

### 파일 다루기

- 파일 생성
```r
file.create()
```

- 파일 삭제
```r
file.remove()
```

- 파일 복사
```r
file.copy('file_name','directory_name')
```

- 파일 이동
```r
install.packages('filesstrings')
library('filesstrings')
file.move('gota-river-near-sjotopvannersbur.csv','river/')
```

- rename
```r
file.rename('file_name','file_rename')
```