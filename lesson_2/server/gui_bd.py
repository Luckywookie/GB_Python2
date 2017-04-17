from datetime import datetime, date
from tkinter import *
from tkinter.messagebox import *
from models.payments import PaymentModel
from select_data import search_date, search_partner_trans
from run_db import session


class TableGrid(Frame):
    ''' Заготовка для создания табличного вида
    '''
    def __init__(self, parent=None, titles=None, rows=0, *args, **kwargs):
        w = kwargs.get('w', 300)
        h = kwargs.get('h', 300)
        super().__init__(parent, relief=GROOVE, width=w, height=h, bd=1)
        self.w = w
        self.h = h

        # Создаем возможность вертикальной прокрутки таблицы:
        self._create_scroll()

        # Размещаем заголовки
        for index, title in enumerate(titles):
            Label(self.frame, text=title).grid(row=0, column=index)

        # Создаём пустые строки (для наглядности, что это таблица)
        self.rebuild(len(titles), rows)

        # Размещаем текущий объект self в родительском виджете parent
        self.pack()

    def _create_scroll(self):
        ''' Обёртка для создания прокрутки внутри Frame.
        Дело в том, что элемент Scrollbar можно привязать
        только к "прокручиваемым" виджетам (Canvas, Listbox, Text),
        в то время как наша "таблица" создана на основе Frame.

        Чтобы решить эту задачу, нужно внутри нашего фрейма создать дополнительные
        виджеты: Canvas и Frame.
        '''
        self.canvas = Canvas(self)
        self.frame = Frame(self.canvas)

        # Сам по себе Scrollbar - хитрый...
        # Нужно сделать связь не только в Scrollbar, но и в привязанном Canvas'е:
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # "Упаковываем" Canvas и Scrollbar - один слева, другой справа:
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left")

        # Отрисовываем новый фрейм на Canvas'е
        self.canvas.create_window((0,0), window=self.frame, anchor='nw')

        # При событии <Configure> будет происходить перерисовывание Canvas'а.
        # Событие <Configure> - базовое событие для виджетов;
        # происходит, когда виджет меняет свой размер или местоположение.
        self.frame.bind("<Configure>", lambda e: self._scroll())

    def _scroll(self):
        """
            Перерисовка канвы и области прокрутки
        """
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.canvas.config(width=self.w, height=self.h)

    def rebuild(self, rows=0, columns=0):
        '''
            Пересоздание таблицы полей ввода.
        '''
        self.vars = []
        self.cells = []

        for i in range(1, rows+1):
            self.vars.append([])
            for j in range(columns):
                # Создаём связанную переменную, которая будет "передавать" данные в виджет
                var = StringVar()
                # Внутри нашего виджета будет таблица связанных переменных  (почти MVC шаблон)
                self.vars[i-1].append(var)

                # Создаём ячейку таблицы - это простое текстовое поле Entry с привязанной переменной
                cell = Entry(self.frame, textvariable=var)
                cell.grid(row=i, column=j)

                # Все ячейки тоже "запомним" внутри нашего виджета (чтобы можно было их удалять)
                self.cells.append(cell)

    def update_data(self, data_func):
        """ Заполнение таблицы данными.
        Заполнение производится через связанные переменные.
        """
        sql_data = data_func

        self.rebuild(len(sql_data), len(sql_data[0]))

        for index, data in enumerate(sql_data):
            for i, d in enumerate(data):
                self.vars[index][i].set(d)


# Создаем основное окно программы
main_window = Tk()

main_window.minsize(400, 400)
main_window.resizable(width=True, height=True)
main_window.title('Звёздный администратор')
# main_window.iconbitmap('favicon.ico')

main_menu = Menu(main_window)
file_menu = Menu(main_menu)

grid = TableGrid(main_window, ('id', 'Sum'), 2, w=400)

file_menu.add_command(label='Terminals',
                      command=lambda g=grid:
                      g.update_data(search_partner_trans(session, PaymentModel, date(2011, 3, 5), date(2019, 3, 5))))
# file_menu.add_command(label='Transactions', command=func)
# file_menu.add_command(label='Partners', command=func)

main_menu.add_cascade(label='Data Bases', menu=file_menu)

main_window.config(menu=main_menu)

# btn1 = Button(main_window, text='Button1', command=func)
# btn2 = Button(main_window, text='Button2', command=func)
# btn1.grid(column=5, row=3)
# btn2.grid(column=3, row=6)


mainloop()
