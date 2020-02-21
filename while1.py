"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
  vNumQuestion = 1
  vListOfAnswers = []

  # print("Как дела?")
  while True:
    print("Как дела?")
    vAnswer = input() 
    if vAnswer == "Хорошо":
      if vNumQuestion == 1:
        print("Ого! С первого раза!")
        print(vNumQuestion)
        False
      
      else:
        print('Отлично! И всего-то потребовалось '+str(vNumQuestion)+ ' вопросов')
        print('А теперь, дава посмотрим что ты ответил до этого:')
        for vAnswerCount in vListOfAnswers:
          print(vAnswerCount)
      
      
      break
    else:
      vNumQuestion +=1    
      vListOfAnswers += [vAnswer]
      # ask_user()
      
    
if __name__ == "__main__":
    ask_user()
