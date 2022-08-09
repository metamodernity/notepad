notes = []
flag = 1
class Note:
    def __init__(self, id, text):
        self.id = id
        self.text = text
        notes.append(self)
note1 = Note(1, 'Первая заметка')
note2 = Note(2, 'Вторая заметка')
note3 = Note(3, 'Третья заметка')
note4 = Note(4, 'Четвёртая заметка')
while flag == 1:
    answer = input('Что вы желаете сделать?\n1.Создать заметку \n2.Прочить заметки\n3.Удалить заметку\n4.Удалить все заметки\n5.Завершить работу программы\n')
    if answer == '1':
        num = (len(notes) + 1)
        txt = str(input('Введите текст заметки:\n'))
        note = Note(num, txt)
    if answer == '2':
        if len(notes) == 0:
            print('Заметок нет\n')
        else:
            for note in notes:
                print('===============================')
                print(note.id, note.text)
                print('===============================')
    if answer == '3':
        num = int(input('Какую заметку вы хотите удалить?'))
        if num > len(notes):
            print('ОШИБКА! Такой заметки не существует')
        else:
            notes.pop(num - 1)
            x = 1
            for note in notes:
                newId = len(notes) - (len(notes) - x)
                note.id = newId
                x+=1
    if answer == '4':
        notes.clear()
    if answer == '5':
        flag = 0
