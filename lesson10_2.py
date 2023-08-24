import random
names_list=[]
with open("names.txt",encoding="utf-8") as file:
    for line in file:
        names_list.append(line[:3])
print("======命名系統========\n\n")
while(True):
    first_name=input("輸入姓氏")
    count=int(input("幾筆數"))
    random_names=random.choices(names_list,k=count)
    for name in random_names:
        print(first_name+name[-2:])
    
    again=input("繼續嗎")
    if again.lower()=="n":
        break
print("系統結束")