"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
  print('Задайте вопрос, получите ответ.')
  vDict_Dialog =  {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
    'Что ты такое?':'Я прототип Скайнет',
    'Какая версия?':'0.000000000001',
    'Зачем?':'Затем!',
    'Почему?':'Потому что!',
    'Кто?':'Где?',
    'ААА':'БББ',
    'Есть вопросы?':'Да! Ты кто?',
    }
  while True:
    try:
      vQuest = input()
      if vQuest in vDict_Dialog:
        print(vDict_Dialog[vQuest])
      elif vQuest == 'END':
        break
      elif vQuest[-1] != '?' :
        print('Вы должны задать ВОПРОС!')
        continue
      else:
        print('Этого вопроса нет в списке. Вношу к себе в память, а вас я добавляю к списку с Джоном. Да кстати, а что нужно ответить?')
        vAnswer = input()
        vDict_Dialog[vQuest] = vAnswer
        print('Задайте вопрос, получите ответ.')
        continue
    except(KeyboardInterrupt):
      print("Пока!")
      break
  
    
if __name__ == "__main__":
    ask_user()
