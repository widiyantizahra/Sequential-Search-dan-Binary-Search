def binary_search_definition(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid][0] == target:
            return data[mid][1]
        elif data[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

word_to_find = "Banana"
definition = binary_search_definition(dictionary, word_to_find)

if definition:
    print(f"Definisi kata {word_to_find}: {definition}")
else:
    print(f"Definisi kata {word_to_find} tidak ditemukan.")