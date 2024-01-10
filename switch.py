class switch(object):
    def __init__(self, value):
        self.value = value  # Запоминаем число, которое будем проверять
        self.fall = False   # Пока не нашли совпадение, значит, не будем выполнять другие проверки

    def __iter__(self):
        yield self.match  # Говорим, что будем проверять число
        raise StopIteration  # Когда проверка закончится, заканчиваем программу

    def match(self, *args):
        # Если уже нашли совпадение или список пустой, значит, совпадение есть или проверять больше нечего
        if self.fall or not args:
            return True
        # Если число совпадает хотя бы с одним из чисел в списке, тогда совпадение есть
        elif self.value in args:
            self.fall = True  # Устанавливаем флажок, что нашли совпадение
            return True
        return False  # Если совпадений нет, говорим, что их нет
