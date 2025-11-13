from PySide6.QtWidgets import QMainWindow


class BedsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    # Обработка удаления товара
    def delete_prod(self):
        sender = self.sender()
        prod = sender.product

        self.show_add_group = True
        self.switch_show_group()

        self.selected_product = prod

        self.accept_dial = AcceptDialog('Подтвердите удаление товара в наличии', self.on_delete)
        self.accept_dial.exec()

    # Удаление товара из базы данных
    def on_delete(self):
        self.accept_dial.close()

        prod = self.selected_product

        with connect() as session:
            pr = session.query(SupplyProduct).filter_by(
                id=prod.id
            ).first()

            session.delete(pr)
            session.commit()

        self.update_data()

        self.selected_product = None

        QMessageBox.information(
            self,
            'Данные удалены',
            'Запись о товаре в наличии была удалена'
        )

        self.show_add_group = True
        self.switch_show_group()
        self.pushButton.setText('+ Создать')

    # Обработка события изменения размеров окна
    def resizeEvent(self, a0, QResizeEvent=None):
        self.resize_table()

    # Изменения размеров ячеек таблицы под размер таблицы
    def resize_table(self):
        columns = self.tableWidget.columnCount()

        cell_width = (self.tableWidget.width() // columns) - 4

        if cell_width < 150:
            cell_width = 150

        for column in range(columns):
            self.tableWidget.setColumnWidth(column, cell_width)

        rows = self.tableWidget.rowCount()
        for row in range(rows):
            self.tableWidget.setRowHeight(row, 80)

    # Переключение видимости формы
    def switch_show_group(self):
        self.show_add_group = not self.show_add_group

        self.groupBox.setVisible(self.show_add_group)

    # Возврат к прошлому окну
    def back(self):
        self.parent.show()
        self.close()
