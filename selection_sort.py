# Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i  # Предполагаем, что текущий элемент минимальный
        for j in range(i + 1, len(arr)):  # Ищем минимальный элемент в оставшейся части
            if arr[j] < arr[min_index]:
                min_index = j  # Обновляем индекс минимального элемента
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Меняем местами текущий и минимальный элементы

# Пример использования
a = [-3, 5, 0, -8, 1, 10]
selection_sort(a)
print("Сортировка выбором:", a)  # [-8, -3, 0, 1, 5, 10]
