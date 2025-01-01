from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                           QLineEdit, QPushButton, QComboBox, QMessageBox)
from PyQt6.QtCore import Qt
import json
import os

class APISettings(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('API 설정')
        self.setGeometry(150, 150, 400, 300)
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # 거래소 선택
        exchange_layout = QHBoxLayout()
        exchange_label = QLabel('거래소:')
        self.exchange_combo = QComboBox()
        self.exchange_combo.addItems(['Binance', 'Binance Testnet'])
        exchange_layout.addWidget(exchange_label)
        exchange_layout.addWidget(self.exchange_combo)
        layout.addLayout(exchange_layout)

        # API Key
        key_layout = QHBoxLayout()
        key_label = QLabel('API Key:')
        self.key_input = QLineEdit()
        self.key_input.setEchoMode(QLineEdit.EchoMode.Password)
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)

        # Secret Key
        secret_layout = QHBoxLayout()
        secret_label = QLabel('Secret Key:')
        self.secret_input = QLineEdit()
        self.secret_input.setEchoMode(QLineEdit.EchoMode.Password)
        secret_layout.addWidget(secret_label)
        secret_layout.addWidget(self.secret_input)
        layout.addLayout(secret_layout)

        # 버튼
        button_layout = QHBoxLayout()
        save_button = QPushButton('저장')
        save_button.clicked.connect(self.save_settings)
        test_button = QPushButton('연결 테스트')
        test_button.clicked.connect(self.test_connection)
        button_layout.addWidget(save_button)
        button_layout.addWidget(test_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def save_settings(self):
        settings = {
            'exchange': self.exchange_combo.currentText(),
            'api_key': self.key_input.text(),
            'secret_key': self.secret_input.text()
        }
        
        try:
            with open('config/api_settings.json', 'w') as f:
                json.dump(settings, f)
            QMessageBox.information(self, '성공', 'API 설정이 저장되었습니다.')
        except Exception as e:
            QMessageBox.critical(self, '오류', f'설정 저장 실패: {str(e)}')

    def load_settings(self):
        try:
            if os.path.exists('config/api_settings.json'):
                with open('config/api_settings.json', 'r') as f:
                    settings = json.load(f)
                    self.exchange_combo.setCurrentText(settings.get('exchange', 'Binance'))
                    self.key_input.setText(settings.get('api_key', ''))
                    self.secret_input.setText(settings.get('secret_key', ''))
        except Exception as e:
            print(f'설정 로드 실패: {str(e)}')

    def test_connection(self):
        # TODO: API 연결 테스트 구현
        QMessageBox.information(self, '테스트', 'API 연결 테스트 (구현 예정)')