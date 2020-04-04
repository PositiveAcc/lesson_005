# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as central_house1_room1_folks
from district.central_street.house1.room2 import folks as central_house1_room2_folks
from district.central_street.house2.room1 import folks as central_house2_room1_folks
from district.central_street.house2.room2 import folks as central_house2_room2_folks
from district.soviet_street.house1.room1 import folks as soviet_house1_room1_folks
from district.soviet_street.house1.room2 import folks as soviet_house1_room2_folks
from district.soviet_street.house2.room1 import folks as soviet_house2_room1_folks
from district.soviet_street.house2.room2 import folks as soviet_house2_room2_folks

folks_list = [central_house1_room1_folks, central_house1_room2_folks, central_house2_room1_folks,
              central_house2_room2_folks, soviet_house1_room1_folks, soviet_house1_room2_folks,
              soviet_house2_room1_folks, soviet_house2_room2_folks]
print_list = ''
for i in folks_list:
    print_list += ", ".join(i)

print(print_list)
