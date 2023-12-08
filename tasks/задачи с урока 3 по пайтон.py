
#CСеминар по пайтон  урок№3 :Списки и словари

#задача 2

def find_closest_element(arr, k):
    closest_element = arr[0]
    min_difference = abs(k - closest_element)

    for element in arr:
        difference = abs(k - element)
        if difference < min_difference:
            min_difference = difference
            closest_element = element

    return closest_element

# Пример использования
list_1 = [1, 5, 9, 15, 3, 7]
k = 8

result = find_closest_element(list_1, k)
print(f"Самый близкий элемент к {k}: {result}")

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)


#задача 1
#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

#Найдите количество и выведите его.

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)


#задача 1
#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
#Найдите количество и выведите его.

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)
