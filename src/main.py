from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Wuya Trading Bot')
        self.setGeometry(100, 100, 800, 600)

        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 제목 라벨
        title = QLabel('Wuya Trading Bot Configuration')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # API 설정 버튼
        api_button = QPushButton('API 설정')
        api_button.clicked.connect(self.open_api_settings)
        layout.addWidget(api_button)

        # 거래 설정 버튼
        trade_button = QPushButton('거래 설정')
        trade_button.clicked.connect(self.open_trade_settings)
        layout.addWidget(trade_button)

        # 모니터링 버튼
        monitor_button = QPushButton('모니터링')
        monitor_button.clicked.connect(self.open_monitoring)
        layout.addWidget(monitor_button)

    def open_api_settings(self):
        print('API 설정 열기')

    def open_trade_settings(self):
        print('거래 설정 열기')

    def open_monitoring(self):
        print('모니터링 열기')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
