def is_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

def find_angka_prima(data):
    angka_prima = []
    for angka in data:
        if is_prima(angka):
            angka_prima.append(angka)
    return angka_prima

my_list = [7, 10, 13, 6, 17, 22, 19]
angka_prima = find_angka_prima(my_list)

print("Bilangan prima dalam daftar:")
for prima in angka_prima:
    print(prima)