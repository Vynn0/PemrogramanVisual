a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

print(f"Nilai a: {a} \nNilai b: {b}\n")

if a > b:
    print(f"{bool(a > b)}, Nilai a lebih besar dari nilai b")
elif b > a:
    print(f"{bool(b > a)}, Nilai b lebih besar dari nilai a")
else:
    print(f"{bool(a == b)}, Nilai a sama dengan b")

ppn_a = 0
ppn_b = 0

if a > 10000:
    ppn_a = a * 12 / 100
    print(f"\nNilai ppn a: {ppn_a}")

if b > 50000:
    ppn_b = b * 12 / 100
    print(f"\nNilai ppn b: {ppn_b}")

if ppn_a or ppn_b > 0:
    total_ppn = ppn_a + ppn_b
    print(f"\nTotal ppn: {total_ppn}\n")
    print(bool(ppn_a and ppn_b > 0))
else:
    print(bool(ppn_a and ppn_b > 0))

a = None
b = None

print(bool(a))
print(bool(b))