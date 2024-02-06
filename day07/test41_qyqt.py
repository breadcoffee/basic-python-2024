# file : test41_qyqt.py
# desc : PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 추가 .scaledToWidth(800) 해상도를 w800으로 고정
        pixmap = QPixmap('./images/Yosigo.jpg').scaledToWidth(600)

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel('Sample', self) #lblSize.setText('Sample') 
        lblSize.setFont(QFont('NanumGothicCoding', 20)) # 폰트와 폰트 사이즈
        lblSize.setStyleSheet('Color: #50FF00')
        lblSize.setText(f'{pixmap.width()} x {pixmap.height()}') # 사진의 넓이와 크기
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로중앙정렬 | 세로중앙정렬

        vbox = QVBoxLayout(self) # QtDesigner VerticalLayout 위젯 생성
        vbox.addWidget(lblImage) # VL 위젯에 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # Form에 VL 추가

        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('이미지 뷰어')
        rect = QRect(300, 300, 300, 300) # x, y, w, h
        self.setGeometry(rect)  # 같은 이름의 함수를 여러개 선언해놓고 원하는대로 사용 (오버로딩)
        #self.setGeometry(300, 300, 300, 300)
        self.show() # showFullScreen() 모니터를 꽉 채워서 출력
        self.setCenter()

    def setCenter(self): # 윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())
    

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height()
    print(width, 'x', height)
    instance = WinApp()
    instance.show()
    sys.exit(app.exec_()) # sys.exit() 종료 시 리소스 반환 등 사용