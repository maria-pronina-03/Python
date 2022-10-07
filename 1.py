#Имя, фамилия, год рождения студента
name = input("Введите имя студента: ")
surname = input("Введите фамилию студента: ")
year = int(input("Введите год рождения студента: "))
print (name, "_", surname, "_", year)
name, surname = surname, name #Меняем местами имя и фамилию студента
year= year+60 #Прибавляем к году 60
print (name, "_", surname, "_", year)
