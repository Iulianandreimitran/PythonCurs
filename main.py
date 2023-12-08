# Declararea listei inițiale
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Afișarea listei ordonate ascendent
list_ascendent = sorted(my_list)
print("Lista ordonată ascendent:", list_ascendent)

# Afișarea listei ordonate descendent
list_descendent = sorted(my_list, reverse=True)
print("Lista ordonată descendent:", list_descendent)

# Afișarea numerelor cu indici pari din listă
my_sliced_list = my_list[1::2]
print("Numere cu indici pari:", my_sliced_list)

# Afișarea numerelor cu indici impari din listă
my_sliced_list = my_list[::2]
print("Numere cu indici impari:", my_sliced_list)

# Afișarea elementelor multipli ai lui 3
multiplii_ai_lui_3 = [i for i in my_list if i % 3 == 0]
print("Elemente multipli ai lui 3:", multiplii_ai_lui_3)
