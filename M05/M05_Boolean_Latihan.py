GDP = 2000000
DEBT = 3000000

print("GDP Negara: ", GDP)
print("Hutang Negara: ", DEBT)

in_debt = GDP <= DEBT
in_surplus = GDP > DEBT

if in_debt:
    DTG = DEBT/GDP * 100
    print("Debt-GDP Ratio: ", DTG, "%")

GDP = GDP + 2000000
print("GDP negara ditambah 2 juta dolar. GDP negara sekarang: ", GDP)

# Konfigurasi ulang
in_debt = GDP <= DEBT
in_surplus = GDP > DEBT

if not in_debt and in_surplus:
    Surplus = GDP - DEBT
    print("\nSurplus GDP suatu negara: ", Surplus)
