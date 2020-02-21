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
    print('Строка 1')
    v_string_001v = input()
    print('Строка 2')
    v_string_002v = input()
    print(equel(v_string_001v,v_string_002v))

def equel(v_string_001v='',v_string_002v=''):
      if v_string_001v == '' or v_string_001v == None or v_string_002v == '' or v_string_002v == None:
       return 0
      elif v_string_001v == v_string_002v:
       return 1
      elif len(v_string_001v) > len(v_string_002v):
       return 2
      elif v_string_001v != v_string_002v == 'learn' :
       return 3
      else:
        return -1
    
if __name__ == "__main__":
    main()
