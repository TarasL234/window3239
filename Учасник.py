class Wiget():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num

    def print_info(self):
        print('Напис:', self.title)
        print('Розташування:', self.x, self.y)
class Button(Wiget):
    def __init__(self, title_text, x_num, y_num, is_clicked_bool):
        super().__init__( title_text, x_num, y_num)
        self.is_clicked = is_clicked_bool
    def click(self):
        self.is_clicked = True
        print('Ви зареєстровані')

knopka = Button('Брати участь', 100, 100, False)
knopka.print_info()
answer = input('Бажаєте зареєструватися? (так\ні)')
if answer == 'так':
    knopka.click()
else:
    print('А шкода!')