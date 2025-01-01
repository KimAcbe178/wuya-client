from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                           QLineEdit, QPushButton, QComboBox, QMessageBox,
                           QSpinBox, QDoubleSpinBox, QCheckBox)
from PyQt6.QtCore import Qt
import json
import os

class TradeSettings(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('거래 설정')
        self.setGeometry(150, 150, 500, 400)
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        layout = QVBoxLayout()

        # 레버리지 설정
        leverage_layout = QHBoxLayout()
        leverage_label = QLabel('레버리지:')
        self.leverage_spin = QSpinBox()
        self.leverage_spin.setRange(1, 125)
        self.leverage_spin.setValue(10)
        leverage_layout.addWidget(leverage_label)
        leverage_layout.addWidget(self.leverage_spin)
        layout.addLayout(leverage_layout)

        # 주문 수량 설정 (계좌 비율)
        amount_layout = QHBoxLayout()
        amount_label = QLabel('주문 수량 (%):')
        self.amount_spin = QDoubleSpinBox()
        self.amount_spin.setRange(1, 100)
        self.amount_spin.setValue(10)
        amount_layout.addWidget(amount_label)
        amount_layout.addWidget(self.amount_spin)
        layout.addLayout(amount_layout)

        # 손절 설정
        sl_layout = QHBoxLayout()
        sl_label = QLabel('손절 비율 (%):')
        self.sl_spin = QDoubleSpinBox()
        self.sl_spin.setRange(0.1, 100)
        self.sl_spin.setValue(2)
        self.sl_check = QCheckBox('손절 사용')
        sl_layout.addWidget(sl_label)
        sl_layout.addWidget(self.sl_spin)
        sl_layout.addWidget(self.sl_check)
        layout.addLayout(sl_layout)

        # 익절 설정
        tp_layout = QHBoxLayout()
        tp_label = QLabel('익절 비율 (%):')
        self.tp_spin = QDoubleSpinBox()
        self.tp_spin.setRange(0.1, 1000)
        self.tp_spin.setValue(5)
        self.tp_check = QCheckBox('익절 사용')
        tp_layout.addWidget(tp_label)
        tp_layout.addWidget(self.tp_spin)
        tp_layout.addWidget(self.tp_check)
        layout.addLayout(tp_layout)

        # 버튼
        button_layout = QHBoxLayout()
        save_button = QPushButton('저장')
        save_button.clicked.connect(self.save_settings)
        button_layout.addWidget(save_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def save_settings(self):
        settings = {
            'leverage': self.leverage_spin.value(),
            'order_amount': self.amount_spin.value(),
            'stop_loss': {
                'enabled': self.sl_check.isChecked(),
                'percentage': self.sl_spin.value()
            },
            'take_profit': {
                'enabled': self.tp_check.isChecked(),
                'percentage': self.tp_spin.value()
            }
        }
        
        try:
            os.makedirs('config', exist_ok=True)
            with open('config/trade_settings.json', 'w') as f:
                json.dump(settings, f)
            QMessageBox.information(self, '성공', '거래 설정이 저장되었습니다.')
        except Exception as e:
            QMessageBox.critical(self, '오류', f'설정 저장 실패: {str(e)}')

    def load_settings(self):
        try:
            if os.path.exists('config/trade_settings.json'):
                with open('config/trade_settings.json', 'r') as f:
                    settings = json.load(f)
                    self.leverage_spin.setValue(settings.get('leverage', 10))
                    self.amount_spin.setValue(settings.get('order_amount', 10))
                    
                    sl_settings = settings.get('stop_loss', {})
                    self.sl_check.setChecked(sl_settings.get('enabled', False))
                    self.sl_spin.setValue(sl_settings.get('percentage', 2))
                    
                    tp_settings = settings.get('take_profit', {})
                    self.tp_check.setChecked(tp_settings.get('enabled', False))
                    self.tp_spin.setValue(tp_settings.get('percentage', 5))
        except Exception as e:
            print(f'설정 로드 실패: {str(e)}')