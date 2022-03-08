ls = [0, 8, 4, 12, 2, 4, 9, 1, 3, 5, 13, 1, 3, 5, 13, 3]
print('My List:', ls)

ls1=[]
ls2=[ls1]

for i in range(len(ls)):
    if len(ls1)==0:
        ls2[i].append(ls[i])

    elif ls2[-1][-1]<=ls[i]:
        ls2[-1].append(ls[i])

    else:
        ls2.append([ls[i]])

print('Dividend into sublist :', ls2)
temp_list=max(ls2, key=len)
for i in ls2:
    if len(i) == len(temp_list):
        print(i)

