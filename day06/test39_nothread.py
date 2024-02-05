# file : test39_nothread.py
# desc : Qt에서 스레드없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): # QWidget을 상속받음
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self)
        # 버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일 내에 있는 위젯접근은 VSCode상에서 색상으로 표시 X

    def btnStartClicked(self):
        print('시작버튼 클릭')
        maxVal = 100
        self.pgbTask.setValue(0) # 프로그레스바 0부터 시작
        self.pgbTask.setRange(0, maxVal)
        for i in range(maxVal+1):
            print_str = f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.txbLog.append(print_str)
            self.pgbTask.setValue(i)

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__': # main entry 확인조건 추가
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()