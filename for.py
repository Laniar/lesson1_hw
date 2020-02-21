from random import randint
"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
v_school_array = []

def main():
  print('Список')
  create_dictionary()
  print('Средняя по каждому классу')
  average_classes() 
  print('Средняя по школе')
  average_school()

def create_dictionary():
  global v_school_array
  v_abc_classes = 'abcdi'
  for v_class_num in range(1,12):
    for v_abc in v_abc_classes:
      v_scores_array = []
      for v_scores in range(4,randint(7,15)):
        v_scores_array += [randint(2,5)]
      v_school_array += [{'school_class': str(v_class_num)+v_abc, 'score': v_scores_array}]
  print(v_school_array)

def average_classes():
  global v_school_array
  v_classes_avarage_scores = []
  for v_class in v_school_array:
    v_classes_average = sum(v_class['score'])/len(v_class['score'])
    v_classes_avarage_scores += [v_classes_average]
    print('Класс: '+ v_class['school_class'] + ' Средняя оценка: ' +str(v_classes_average))
  print('Средняя от средних по школе: ' + str(sum(v_classes_avarage_scores)/len(v_classes_avarage_scores)) )

def average_school():
  global v_school_array
  v_classes_sum = 0
  v_classes_len = 0
  for v_class in v_school_array:
    v_classes_sum += sum(v_class['score'])
    v_classes_len += len(v_class['score'])

  print(v_classes_sum/v_classes_len)

if __name__ == "__main__":
    main()
