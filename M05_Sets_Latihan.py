Set_1 = {"Samsung", "Apple", "Xiaomi"}
Set_2 = set(("Samsung", "Apple", "Xiaomi"))

print("Tipe data Set_1 adalah ", type(Set_1))
print("Tipe data Set_2 adalah ", type(Set_2))
print("Data Set_1: ", Set_1)
print("Data Set_2: ", Set_2)
print("------------------------------------")

for x in Set_1:
    print(x)
print("------------------------------------")

print(len(Set_1))

if "Samsung" in Set_1:
    print("Yes, 'Samsung is an item in Set_1.")

print("\nBrand HP baru pada perusahaan 1: ")
Set_1.update(["Asus", "Infinix", "Huawei"])
print(Set_1)

set2 = {"Asus", "Motorola", "Nokia"}
print("\nBrand HP pada perusahaan 2: ", set2)
set3 = Set_1.intersection(set2)

print("\nBrand HP yang ada di perusahaan 1 dan 2 (intersection): ")
print(set3)
print("------------------------------------")