from datetime import datetime, date
from tkinter import *
from tkinter.messagebox import *
from models.payments import PaymentModel


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
        self.grid(columnspan=5)

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

frame = Frame(main_window)

s = TableGrid(main_window, ('ID', 'Date', 'Sum'), 3, w=400)


def select_partners(event):    # Функция для кнопки 'event' обязательный параметр
    s.update_data(PaymentModel.find_by_dates(date(int(entry1.get()), int(entry2.get()), int(entry3.get())), date(2019, 3, 5)))


lable1 = Label(main_window, text='Year', height=1, bg='yellow')
lable1.grid(row=0, column=0, rowspan=1)
lable2 = Label(main_window, text='Month', bg='yellow')
lable2.grid(row=0, column=1, rowspan=1)
lable3 = Label(main_window, text='Day', bg='yellow')
lable3.grid(row=0, column=2, rowspan=1)

entry1 = Entry(main_window)
entry1.grid(row=1, column=0)
entry2 = Entry(main_window)
entry2.grid(row=1, column=1)
entry3 = Entry(main_window)
entry3.grid(row=1, column=2)

btn = Button(main_window, text='View')
btn.grid(row=1, column=3)   # Отображаем кнопку
btn.bind('<Button-1>', select_partners)



mainloop()
