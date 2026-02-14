answer = input("Əməliyyat seçin: toplama, çıxma, vurma, bölmə: ")
if answer == "toplama":
    def plussing():
        a = int(input("Bir ədəd daxil edin: "))
        b = int(input("Başqa bir ədəd daxil edin: "))
        c = a + b
        print(c)
    plussing()

if answer == "çıxma":
    def minusing():
        a = int(input("Bir ədəd daxil edin: "))
        b = int(input("Başqa bir ədəd daxil edin: "))
        c = a - b
        print(c)
    minusing()
if answer == "vurma":
    def multiplying():
        a = int(input("Bir ədəd daxil edin: "))
        b = int(input("Başqa bir ədəd daxil edin: "))
        c = a * b
        print(c)
    multiplying()
if answer == "bölmə":
    def dividing():
        a = int(input("Bir ədəd daxil edin: "))
        b = int(input("Başqa bir ədəd daxil edin: "))
        c = a / b
        print(c)
    dividing()
