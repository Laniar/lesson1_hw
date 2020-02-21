"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
  v_num_question = 1
  v_list_of_answers = []

  while True:
    print("Как дела?")
    v_answer = input() 
    if v_answer == "Хорошо":
      if v_num_question == 1:
        print("Ого! С первого раза!")
        print(v_num_question)
        False
      
      else:
        print('Отлично! И всего-то потребовалось '+str(v_num_question)+ ' вопросов')
        print('А теперь, дава посмотрим что ты ответил до этого:')
        for v_answer_count in v_list_of_answers:
          print(v_answer_count)
      
      break
    else:
      v_num_question +=1    
      v_list_of_answers += [v_answer]
      
    
if __name__ == "__main__":
    ask_user()
