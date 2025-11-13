from PySide6.QtWidgets import QMainWindow


class BedsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Обработка редактирования товара
        def edit_prod(self):
            sender = self.sender()
            prod = sender.product

            self.selected_product = prod
            self.paste_form()
            self.show_add_group = False

            self.switch_show_group()

            if self.show_add_group:
                self.pushButton.setText('Закрыть')

            else:
                self.pushButton.setText('+ Создать')

        # Очистка формы
        def clear_form(self):
            self.comboBox.setCurrentIndex(0)
            self.comboBox_2.setCurrentIndex(0)
            self.doubleSpinBox.setValue(0)

        # Обновление данных
        def update_data(self):
            self.tableWidget.setRowCount(0)

            search_text = self.lineEdit.text().strip().lower()

            with connect() as session:
                sup_products = session.query(SupplyProduct).join(
                    SupplyProduct.product
                ).filter(
                    Product.status.has(name='В наличии')
                ).options(
                    joinedload(SupplyProduct.product)
                ).options(
                    joinedload(SupplyProduct.supplier)
                ).order_by(desc(SupplyProduct.id)).all()

                self.tableWidget.setRowCount(len(sup_products))

                index = 0
                for sup_prod in sup_products:

                    try:
                        # Поиск Леввенштейна
                        if search_text != "":
                            if len(search_text) > len(sup_prod.product.product_name):
                                scope = len(search_text) - len(sup_prod.product.product_name)
                                h = 0
                                for i in sup_prod.product.product_name.strip().lower():
                                    if i != search_text[h]:
                                        scope += 1
                                    h += 1

                                if scope > 3:
                                    continue

                            else:
                                scope = len(sup_prod.product.product_name) - len(search_text)
                                h = 0
                                for i in search_text:
                                    if i != sup_prod.product.product_name.strip().lower()[h]:
                                        scope += 1
                                    h += 1

                                if scope > 3:
                                    continue

                        lbl = QLabel(sup_prod.product.product_name)
                        self.tableWidget.setCellWidget(index, 0, lbl)

                        lbl1 = QLabel(sup_prod.product.product_article)
                        self.tableWidget.setCellWidget(index, 1, lbl1)

                        lbl2 = QLabel(str(sup_prod.product.price))
                        self.tableWidget.setCellWidget(index, 2, lbl2)

                        lb6 = QLabel(str(sup_prod.delivery_price))
                        self.tableWidget.setCellWidget(index, 3, lb6)

                        lbl3 = QLabel(f'{sup_prod.supplier.company_name}')
                        self.tableWidget.setCellWidget(index, 4, lbl3)

                        lbl4 = QLabel(sup_prod.product.status.name)
                        self.tableWidget.setCellWidget(index, 5, lbl4)

                        lbl5 = QLabel(sup_prod.product.category.name)
                        self.tableWidget.setCellWidget(index, 6, lbl5)

                        wdg = QWidget()
                        lyt = QVBoxLayout()

                        btn = QPushButton('Редактировать')
                        btn.product = sup_prod
                        btn.clicked.connect(self.edit_prod)

                        btn1 = QPushButton('Удалить')
                        btn1.product = sup_prod
                        btn1.clicked.connect(self.delete_prod)

                        lyt.addWidget(btn)
                        lyt.addWidget(btn1)

                        wdg.setLayout(lyt)
                        self.tableWidget.setCellWidget(index, 7, wdg)

                        index += 1
                    except Exception as e:
                        continue

            self.resize_table()
