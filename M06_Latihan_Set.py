Restaurant_1 = {"Nasi Goreng", "Soto", "Bakso", "Sate", "Dimsum", "Mie", "Nasi Ayam"}

print("Kamu adalah seorang owner restaurant sat. Terdapat pilihan menu makanan pada restaurant satu untuk hari senin sebagai berikut:") #1
print(Restaurant_1)


addData = input("\nSebelum penjualan berlangsung, kamu sebagai owner menambah makanan baru pada menu untuk penjualan restoran satu: ")
Restaurant_1.add(addData) #2
print(Restaurant_1)

print(f"Sebelum penjualan terjadi, sang manajer melakukan organisir terhadap menu tersebut. Dia menghitung banyaknya menu yang tersedia pada restoran satu, dimana terdapat {len(Restaurant_1)} jumlah makanan.\n") #3

def remove_food():
    while True: 
        removeData = input("Setelah restaurant dibuka selama beberapa jam, sebuah stock makanan habis. Makanan tersebut adalah: ")
        if removeData in Restaurant_1:
            Restaurant_1.remove(removeData) #4
            break
        else:
            print("Makanan tidak ada di dalam menu. Silahkan coba lagi.")

remove_food()

print("\nJadi, tersisa makanan pada menu sebagai berikut:")
print(Restaurant_1)

Restaurant_2 = {"Bubur Ayam", "Ketoprak", "Ketupat Sayur"}
print("\nKemudian, kamu ditawarkan kerjasama dengan restaurant 2 pada hari senin karena penjualan restaurant 2 tidak laku. Kamu harus menerima kerjasama pada hari itu juga, dan setelah proses yang singkat, menu kedua restaurant tersebut disatukan menjadi satu sebagai berikut:")
print(Restaurant_1.union(Restaurant_2)) #5