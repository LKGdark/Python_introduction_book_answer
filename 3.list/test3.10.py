yinjie=['Kevin','Elysia','Aponia','Eden','Vill_V','KaIpas','Su','Sakura','Kosma','Mobius','Griseo','Hua','Pardofelis']
print(f"{yinjie}\n")

print(sorted(yinjie))
print(f"{sorted(yinjie,reverse=True)}\n")

print(yinjie)
yinjie.sort()
print(f"{yinjie}\n")

print(yinjie)
Del_yinjie=yinjie.pop(2)
print(f"{Del_yinjie}死了")
print(f"{yinjie}\n")

del yinjie[-1]
yinjie.remove("Aponia")
print(f"{yinjie}\n")

print("人之律者的诞生，致以无瑕之人爱莉希雅！\n")
yinjie.append("people_Elysia")
print(yinjie)

yinjie.insert(3,"Vill_V")
print(yinjie)

yinjie.append("Aponia")
print(yinjie)
print(f"\nThe num fo yinjie is {len(yinjie)}\n")
print("我们又回到了最初的往事乐土！")


