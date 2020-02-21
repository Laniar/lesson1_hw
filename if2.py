"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    # vAges = input()
    print('Строка 1')
    vString_001v = input()
    print('Строка 2')
    vString_002v = input()
    print(equel(vString_001v,vString_002v))

def equel(vString_001v='',vString_002v=''):
      if vString_001v == '' or vString_001v == None or vString_002v == '' or vString_002v == None:
       return 0
      elif vString_001v == vString_002v:
       return 1
      elif len(vString_001v) > len(vString_002v):
       return 2
      elif vString_001v != vString_002v == 'learn' :
       return 3
      else:
        return -1
    
if __name__ == "__main__":
    main()
