# basic-python-2024
부경대 2024 IoT 개발자과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축
    - 코딩폰트 - 나눔고딕폰트
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01) # 10
    print(type(var01)) # <class of 'int'>

    print(5 + 4 / 2) # 7.0
    print(5 = 4) # False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참/거짓으로 조건 분기 (다른언어 switch)
        - for : 반복문 기본 (다른언어 foreach)
        - while : 반복문 변형 (다른언어 do~while)
    - 복합자료형 + 연산자(연산함수)
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷
    - 구구단 + 디버깅

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기
    - 함수
    - 객체지향

## 4일차
- folium 기본사용
    ![folium사용법](https://raw.githubusercontent.com/breadcoffee/basic-python-2024/main/images/Image_folium_map.png)

## 5일차
- 파이썬 응용
    - json 입출력
    - QR code 생성 및 출력

## 6일차
- Python 라이브러리 경로 : C:\DEV\Langs\Python311\Lib\site-packages

- 파이썬 응용
     - Window App(PyQt) 만들기

    ```python
    > pip install PyQt5
    > pip install PyQt5Designer
    ```

    - PyQt5 기본실행
    - QtDesigner 사용법
    - ☆☆☆ Thread 학습 : UI 쓰레드와 Background 쓰레드 분리
        - [ ] GIL 병렬 프로세싱 더 학습할 것

    ![Thread 예제](https://raw.githubusercontent.com/breadcoffee/basic-python-2024/main/images/python_Thread.gif)

    ```python
    # 쓰레드 클래스에서 시그널 선언
    class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
        initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
        setSignal = pyqtSignal(int)
        # ...

        def run(self) -> None: # 스레드 실행
            # 스레드로 동작할 내용
            maxVal = 100000
            self.initSignal.emit(maxVal) # UI쓰레드로 보내기...
            # ...

    class qtwin_exam(QWidget):  # UI 스레드
        # ...
        def btnStartClicked(self):
            th = BackWorker(self)
            th.start() # BackWorker 내의 self.run() 실행
            th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
            # ...    
        
        # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 슬롯함수
        @pyqtSlot(int) # BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
        def initPgbTask(self, maxVal):
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0, maxVal)
    ```

## 7일차
- 파이썬 응용
    - 객체지향 정리
        - 상속, 오버라이딩(재정의), 오버로딩(같은 이름의 함수를 여러개 활용, 매개변수는 다르게)
    - 가상환경 Virtualenv
        - 다른 버전 파이썬도 설치해야 사용 가능
        - 현재 3.11에서 3.9 가상환경이 필요 시 3.9 버전 파이썬 설치 필요

    ```python
    > pip install virtualenv
    ```

    - PyQt5와 응용예제 연습
        - 이미지 뷰어
        - 이미지 에디터
    
    ![PyQt 예제](https://raw.githubusercontent.com/breadcoffee/basic-python-2024/main/images/pypaint.png)

## 8일차
- 파이썬 기본 코딩 테스트
    - 쥬피터 노트북 활용

## 추가
- 파이썬 실행파일 만들기
    - PyQt UI파일이나 이미지파일의 경로가 절대경로로 지정되어야함
    - pip install pyinstaller 패키지 설치
    - pyinstaller -w -F ./파일이름 (-w: 콘솔창 없애기, -F: 실행파일을 하나로 만들기)