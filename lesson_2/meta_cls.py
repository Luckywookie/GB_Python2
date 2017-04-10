# 3*. Работа с ООП:
# * Создать мета-класс, определяющий в переменную класса Journal имя списка, с которым работает создаваемый класс.
# Имя списка должно генерироваться автоматически и соответствовать имени класса, написанного с большой буквы.
# * На основе созданного мета-класса создать класс с именем 'BlackPirate'. При этом экземпляр такого класса имеет
# обязательный строковый атрибут 'id' длиной ровно 13 символов.


# Объявляем метакласс, который будет контролировать создание нового класса
class NewMeta(type):
    def __init__(cls, name, base, attr_dict):
        setattr(cls, name.capitalize(), [])
        super().__init__(cls, name, base)


class ToYou(metaclass=NewMeta):
    def __init__(self, _id):
        if type(_id) and len(_id) == 13:
            self.id = _id

# print(Fooo.__name__)

me = ToYou('1234567890123')

print(me.Toyou)
print(me.id)
print(dir(me))
