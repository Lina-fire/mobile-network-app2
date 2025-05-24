import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from mobile_network import MobileNetwork

class MobileNetworkApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mobile_form.ui", self)
        
        self.network = MobileNetwork()
        self.btnLoad.clicked.connect(self.load_data)
    
    def load_data(self):
        try:
            self.network.load_from_file("subscribers.txt")
            self.display_data(self.network.subscribers)
            QMessageBox.information(self, "Успех", "Данные успешно загружены и отсортированы!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные: {str(e)}")
    
    def display_data(self, subscribers):
        self.tableWidget.setRowCount(0)
        
        for row, sub in enumerate(subscribers):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(sub.last_name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(sub.initials))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(sub.phone))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(sub.tariff))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(sub.gigabytes)))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(sub.minutes)))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(str(sub.sms)))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(f"{sub.payment:.2f}"))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(sub.start_date.strftime("%d.%m.%Y")))
        
        self.tableWidget.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MobileNetworkApp()
    window.show()
    sys.exit(app.exec_())