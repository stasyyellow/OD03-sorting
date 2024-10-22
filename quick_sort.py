#Быстрая сортировка

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Базовый случай: если массив содержит 1 или 0 элементов, он уже отсортирован
    else:
        pivot = arr[len(arr) // 2]  # Выбираем средний элемент как опорный
        left = [x for x in arr if x < pivot]  # Элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # Элементы, равные опорному
        right = [x for x in arr if x > pivot]  # Элементы больше опорного
        return quick_sort(left) + middle + quick_sort(right)  # Рекурсивно сортируем левую и правую часть

# Пример использования
a = [-3, 5, 0, -8, 1, 10]
sorted_array = quick_sort(a)
print("Быстрая сортировка:", sorted_array)  # [-8, -3, 0, 1, 5, 10]
