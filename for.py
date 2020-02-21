from random import *
"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
vSchoolArray = []
#vClassesAvarageScores = []

def main():
    #
  #global vSchoolArray
  print('Список')
  createDictionary()
  print('Средняя по каждому классу')
  average_classes() 
  print('Средняя по школе')
  average_school()

def createDictionary():
  global vSchoolArray
  vABCClasses = 'abcdi'
  for vClassNum in range(1,12):
    for vABC in vABCClasses:
      vScoresArray = []
      for vScores in range(4,randint(7,15)):
        vScoresArray += [randint(2,5)]
      vSchoolArray += [{'school_class': str(vClassNum)+vABC, 'score': vScoresArray}]
      #vSchoolArray= [{'school_class': str(vClassNum+vABC)+vABC, 'score': [1,2,3,]} , {'school_class': str(vClassNum+1)+vABC)+vABC, 'score': [1,2,3,]}]
  print(vSchoolArray)

def average_classes():
  global vSchoolArray
  vClassesAvarageScores = []
  for vClass in vSchoolArray:
    vClasses_Average = sum(vClass['score'])/len(vClass['score'])
    vClassesAvarageScores += [vClasses_Average]
    print('Класс: '+ vClass['school_class'] + ' Средняя оценка: ' +str(vClasses_Average))
  print('Средняя от средних по школе: ' + str(sum(vClassesAvarageScores)/len(vClassesAvarageScores)) )

def average_school():
  global vSchoolArray
  vClasses_SUM = 0
  vClasses_Len = 0
  for vClass in vSchoolArray:
    vClasses_SUM += sum(vClass['score'])
    vClasses_Len += len(vClass['score'])

  print(vClasses_SUM/vClasses_Len)

if __name__ == "__main__":
    main()
