def operation_count(num1, num2):
    count = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count

# Kullanıcıdan iki sayı girmesini isteyelim
num1 = int(input("Lütfen birinci sayıyı girin: "))
num2 = int(input("Lütfen ikinci sayıyı girin: "))

# İşlem sayısını hesaplayalım ve ekrana yazdıralım
count = operation_count(num1, num2)
print("İşlem sayısı:", count)