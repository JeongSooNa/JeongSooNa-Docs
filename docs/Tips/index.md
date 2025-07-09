# TIPS
IT 직무 혹은 개발에 유용한 꿀팁 모음

### Portfolio
포트폴리오는 취업, 이직, 자기개발 용도로 제작하며, 요구사항에 맞는 다양한 제작이 필요합니다.

- Github
    - 깃허브를 통해 본인의 소스코드 및 프로젝트를 소개할 수 있으며, 개발자, IT 업계 종사자 혹은 진출을 원할 경우 업데이트, 소스코드 관리를 생활화 하는 것을 추천합니다.
    - 기본적인 포트폴리오 템플릿부터 간단한 배포까지 손쉽게 가능합니다. 따로 데이터베이스를 사용하지 않는 웹 프로젝트, 알고리즘 구현 기능 등을 배포할 수 있습니다.
    - Organization 및 협업에 특화돼 공동 개발에도 유용합니다.
- AWS
    - 개발에 처음 입문하는 사람이라면 단기간 제공되는 무료 라이센스를 통해 배포 및 할당 받은 Linux 서버 운영을 경험할 수 있습니다.
    - 데이터베이스와 연동된 프로젝트를 배포하고, 제공하는데 적합합니다.
- 블로그
    - 티스토리, Docs, 네이버, Github를 통해서 다양한 방식의 블로그를 제작할 수 있습니다.
    - 운영 및 수익 창출이 목적이 될 수 있으나, 문제 해결 방법 등을 작성하고, 한눈에 본인의 프로젝트, 경험, 공부 내용 등을 공유하는데 적합합니다.
- 


### Git 과 Github
Git 이란 소스 코드 관리를 위한 형상관리툴로, 협업과 저장소 관리에 유용한 기술입니다.  
Git을 기반으로 Public 저장소와 개발자들간의 소통을 제공하는 Github는 개발자 뿐만 아니라 IT 전 분야에 걸쳐 필수적인 커뮤니티로 자리잡고 있습니다.

- Github 계정 및 Repository 생성
    - Git 설치
    ![jpg](../img/git_install.png)
    - Github 계정 생성
    ![jpg](../img/github_create_account.png)
    - Github Repository 생성
    ![jpg](../img/github_create_repo.png)
    - Git Clone을 통해 복사된 코드를 사용하여 VS Code 등 사용 IDE에서 Clone
    ![jpg](../img/git_clone_url.png)
- 사용 환경 내 Github 계정 등록
```
git config user.name __github_이름__
git config user.email __github_이메일__
```
- Clone : Repository(저장소)를 내 환경에 세팅
- Commit : 수정 사항 내 환경에서 저장
- Push : Commit 사항 Repository로 보내기 (저장)
- Pull : 다른 수정 된 내용을 불러오기
- Fork : Repository 복제 (주로 다른 유저의 Repository를 복제하여 본인이 사용하기 위해 사용, 라이센스 등 확인)

- VS Code를 활용한 Github 연동 및 Repository 관리
    1. VSCode에 Git 설치 및 설정:
        - VSCode에서 Git을 사용하려면 먼저 Git을 설치해야 합니다. 
        - Git을 설치한 후, VSCode에서 Git을 설정합니다. 
        - Git 설정에서 사용자 이름과 이메일을 입력합니다. 
    2. GitHub 계정 생성 및 VSCode 확장 프로그램 설치:
        - GitHub 계정을 생성합니다.
        - VSCode에서 GitHub 확장 프로그램을 설치합니다.
        - GitHub 확장 프로그램이 설치되면, VSCode에서 GitHub 계정에 로그인합니다. 
    3. VSCode에서 GitHub 저장소 클론 및 푸시:
        - VSCode에서 터미널을 열고, 다음 명령어를 입력하여 GitHub 저장소를 로컬에 클론합니다.
        - ```git clone <GitHub 저장소 URL>```
    4. VSCode를 통해 GitHub에 코드 업로드: 
        - VSCode의 소스 제어 뷰(왼쪽에서 세 번째 아이콘)를 사용하여 파일을 변경합니다. 
        - 변경사항 위의 칸에 커밋 메세지를 입력하고 커밋 버튼을 눌러 커밋합니다. 
        - Sync Changes 버튼을 눌러 GitHub에 푸시합니다. 

### Markdown
마크다운(Markdown)이란 텍스트 기반의 언어로, 쉽게 쓰고 읽을 수 있습니다.  
특수기호와 문자를 이용하여 매우 간단한 구조의 문법을 사용하여 보다 빠르게 컨텐츠를 작성하고, 직관적으로 인식할 수 있습니다.  

- [참조 및 사용법](https://gist.github.com/ihoneymon/652be052a0727ad59601)

### 개발자를 위한 프로그래밍 역량 강화
환경 설정, 기본적인 문법 숙지가 충분하다면 실무에 가까운 경험을 위한 프로젝트 진행을 권장합니다.  
프로젝트의 경우 간단한 기능을 제공하는 미니 프로젝트부터, 플랫폼 구축, 배포를 포함한 웹 연동 서비스 제공, API 개발 등 다양한 분야에서 접근이 가능하며, 이를 본인의 Github, 혹은 공동 개발자가 있을 경우 Github Organizations을 통해 개발하는 것을 권장합니다.

- 추천 링크
    - [Python mini project](https://github.com/ndleah/python-mini-project)
    - [Java mini project](https://github.com/topics/java-mini-project)

### 코딩 역량 강화 및 코딩 테스트 대비
최근 IT 직무 수요 증가와 함께 대기업을 포함한 대부분의 기업 IT 직군 모집에서 코딩 역량을 확인하는 테스트를 갖고 있습니다.  
이에 따라 알고리즘 구현 능력과 기초적인 문법 및 함수를 활용한 코딩 테스트 대비는 필수 요소로 자리잡고 있습니다.

- 코딩 테스트 추천 사이트
    - [백준](https://www.acmicpc.net/)
    - [프로그래머스](https://school.programmers.co.kr/)
- 웹 프로그래밍 서비스
    - 따로 환경 세팅이 필요 없이 온라인에서 코드를 작성하고 실행해 볼 수 있는 서비스입니다.
    - [구글 Colab](https://colab.research.google.com/)
        - Linux 환경에서의 간단한 테스트, OS와 연동된 프로그램 개발 테스트에 적합한 웹 서비스입니다.
    - [Tutorials point](https://www.tutorialspoint.com/compilers/index.htm)
        - 다양한 언어를 제공하며, 빠르게 간단한 코드를 실행시켜보고 싶을 때 적합합니다.
    - [Replit](https://replit.com/)
        - 개발부터 배포까지 웹으로 가능한 서비스입니다.
    - [CodePen](https://codepen.io/)
        - 주로 프론트앤드 결과물 확인에 적합하며, 다양한 웹 디자인을 가져오고, 수정할 수 있습니다.


### Python TIPS

1. ```import *``` 사용을 자재
    - ```from __ import *``` 로 모든 모듈을 불러오는 경우
    - 가동 시간이 길다.
    - 변수명끼리 충돌 현상이 일어날 수 있다.

2. ```except```절의 정확한 Error 명시
    - 특정 예외를 지정함으로써 프로그램 중지를 방지하고 효율적인 자원관리를 할 수 있다.

3. 수학 계산에 ```numpy``` 사용
    - 수학 연산에 있어 for 루프보다 더 빠른 연산 속도를 보여줌. (작업을 벡터화하기 때문)
    - 간단한 연산은 그냥 구현하면 되지만 계산량이 많아지거나 복잡한 경우 ```numpy```를 사용하는 것을 권장.

4. 불러온 파일을 닫는 습관
    - ```open```을 사용해 외부 파일을 불러온 경우 ```close```를 사용해 닫아주는 것이 좋다.
    - ```write``` ```read```를 사용할 경우 예외가 발생할 경우 열린 파일이 닫히지 않을 수 있기 때문

5. PRP8의 가이드라인을 벗어나지 않도록
    - 이해하기 쉬운 변수명을 사용
    - 코드 작성에 최적의 가이드라인을 따라 클린코드를 작성

6. 딕셔너리를 사용할 때 ```.keys```와 ```.values```를 적절히 사용할 것
    - ```for``` 루프에서 딕셔너리를 반복하는 것 만으로도 key값을 얻을 수 있다.

    ```py
    for key in dict.keys():
        print(key)
    ```

    - ```.ietm()```을 사용해 value값을 얻을 수 있다.

7. 컴프리헨션(comprehension)을 적절히 사용
    - ```for```루프를 사용하는 것 대신 컴프리헨션으로 단단히 처리할 수 있다.

    ```py
    a = ['a','b','c']
    b = []

    # for 사용
    for i in a:
        b.append(i.lower())

    # Using comprehension
    b = [i.lower() for i in a]
    ```

8. range(len()) 사용을 자제
    - 실제 프로그래밍 시 ```range(len())```을 사용하는 것 보다 enumerate나 zip을 사용해 리스트를 효율적으로 사용할 수 있다.
    
    ```py
    for i,j in enumerate(data_list):
        print(i,j) # list의 index와 요소를 함께 사용
    for i,j in zip(list_1,list_2):
        print(i,j) # 여러 개의 list의 인자를 동시에 가져오기
    ```

9. 출력 시 + 연산자보다 f-string을 권장

10. Mutable value를 디폴트 매개변수로 사용 시 주의

- Reference : [파이썬 초보자가 저지르는 10가지 실수](https://yozm.wishket.com/magazine/detail/1605/)