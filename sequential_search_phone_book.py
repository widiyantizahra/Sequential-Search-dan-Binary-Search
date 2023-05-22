def find_nomor_telepom(nama,buku_telepon):
    for entry in buku_telepon:
        if entry[0] == nama:
            return entry[1]
    return None

buku_telepon = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]

nama_to_find = "Jane Smith"
nomor_telepon = find_nomor_telepom(nama_to_find, buku_telepon)

if nomor_telepon:
    print(f"Nomor telepon {nama_to_find}: {nomor_telepon}")
else:
    print(f"Nomor telepon {nama_to_find} tidak ditemukan.")