#a, b, c = map(float,input().split( ))

# number = float(input())
# if number < 0 or number > 100:
#     print("Fora de intervalo")
# elif number <= 25:
#     print("Intervalo [0,25]")
# elif number <= 50:
#     print("Intervalo (25,50]")
# elif number <= 75:
#     print("Intervalo (50,75]")
# else:
#     print("Intervalo (75,100]")

# x,y = map(int,input().split( ))
# if x == 1:
#     a = 4.00*y
#     print("Total: R$ ","{:.2f}".format(a))
# elif x == 2:
#     b = 4.50*y
#     print("Total: R$ ","{:.2f}".format(b))
# elif x == 3:
#     c = 5.00*y
#     print("Total: R$ ","{:.2f}".format(c))
# elif x == 4:
#     d = 2.00*y
#     print("Total: R$ ","{:.2f}".format(d)) 
# elif x == 5:
#     e = 1.50*y
#     print("Total: R$ ","{:.2f}".format(e))   
    
# Read the four grades from the user
# n1, n2, n3, n4 = map(float, input().split())
# average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
# print(f"Media: {average:.1f}")
# if average >= 7.0:
#     print("Aluno aprovado.")
# elif average < 5.0:
#     print("Aluno reprovado.")
# else:
#     print("Aluno em exame.")
#     exam_score = float(input("Nota do exame: "))
#     final_average = (average + exam_score) / 2 
#     if 4.9<= final_average <= 7.0:
#         print("Aluno aprovado.")
#     else:
#         print("Aluno reprovado.")
#         print(f"Media final: {final_average:.1f}")
      
# x, y = map(float, input().split())
# if x and y > 0:
#     print("Q1")
# elif x <0 and y> 0:
#     print("Q2")
# elif x>0 and y<0:
#     print("Q4")     
# elif x and y<0:
#     print("Q3")
# else:
#     print("Origem") 

# a, b, c = map(int, input().split( ))
# x = []
# x.append(a)
# x.append(b)
# x.append(c)
# for j in sorted(x):
#     print(j)
# print()    
# for i in x:
#     print(i) 
    
# A, B, C = map(float, input().split())
# sides = [A, B, C]
# sides.sort(reverse=True)

# A = sides[0]
# B = sides[1]
# C = sides[2]

# if A >= B + C:
#     print("NAO FORMA TRIANGULO")
# else:
#     if A**2 == B**2 + C**2:
#         print("TRIANGULO RETANGULO")
#     if A**2 > B**2 + C**2:
#         print("TRIANGULO OBTUSANGULO")
#     if A**2 < B**2 + C**2:
#         print("TRIANGULO ACUTANGULO")
#     if A == B == C:
#         print("TRIANGULO EQUILATERO")
#     if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
#         print("TRIANGULO ISOSCELES")

# a, b = map(int, input().split( ))
# ax = []
# ay = sorted(ax)
# ax.append(a)
# ax.append(b)
# ax_s = sorted(ax)
# print(ax_s)
# x = 0
# for i in range(ax_s[0]+1, ax_s[1]+1):
#     i = 1
#     x = x+i
# print(x)    

# start_time, end_time = map(int,input().split())
# if start_time < end_time:
#     duration = end_time - start_time
# else:
#     duration = 24 - start_time + end_time
# print(f"O JOGO DUROU {duration} HORA(S)")

# start_hour,start_minute,end_hour,end_minute  = map(int,input().split( ))

# start_total_minutes = start_hour * 60 + start_minute
# end_total_minutes = end_hour * 60 + end_minute
# if start_total_minutes < end_total_minutes:
#     duration_minutes = end_total_minutes - start_total_minutes
# else:
#     duration_minutes = 24 * 60 - start_total_minutes + end_total_minutes
# duration_hours = duration_minutes // 60
# duration_minutes %= 60
# print(f"O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)")

# a = float(input())
# if 0<=a<=400.00:
#     print("Novo salario:","{:.2f}".format((a*0.15)+a))
#     print("Reajuste ganho:","{:.2f}".format(((a*0.15)+a)-a))
#     print("Em percentual: 15 %")
# elif  400.01<a<=800.00:
#     print("Novo salario:","{:.2f}".format((a*0.12)+a))
#     print("Reajuste ganho:","{:.2f}".format(((a*0.12)+a)-a))
#     print("Em percentual: 12%")
# elif 800.01<=a<=1200.00:
#     print("Novo salario:","{:.2f}".format((a*0.10)+a))
#     print("Reajuste ganho:","{:.2f}".format(((a*0.10)+a)-a))
#     print("Em percentual: 10%")
# elif 1200.01<=a<=2000.00:
#     print("Novo salario:","{:.2f}".format((a*0.07)+a))
#     print("Reajuste ganho:","{:.2f}".format(((a*0.07)+a)-a))
#     print("Em percentual: 7%")
# elif a>2000.00:
#     print("Novo salario:","{:.2f}".format((a*0.04)+a))
#     print("Reajuste ganho:","{:.2f}".format(((a*0.04)+a)-a))
#     print("Em percentual: 4%")            

#a,b,c = map(str, input().split( ))
# a = str(input())
# b = str(input())
# c = str(input())

# if a == "vertebrado" and b == "mamifero" and c == "onivoro":
#     print("homem")
# elif a == "vertebrado" and b == "mamifero" and c == "herbivoro":
#     print("vaca")
# elif a == "vertebrado" and b == "ave" and c == "carnivoro":
#     print("aguia")     
# elif a == "vertebrado" and b == "ave" and c == "onivora":
#     print("pomba")  
# elif a == "invertebrado" and b == "inseto" and c == "hematofago":
#     print("pulga")      
# elif a == "invertebrado" and b == "inseto" and c == "herbivoro":
#     print("lagarta")
# elif a == "invertebrado" and b == "anelideo" and c == "hematofago":
#     print("sanguessuga")
# elif a == "invertebrado" and b == "anelideo" and c == "onivoro":
#     print("minhoca")            

# a = int(input())
# if a == 61:
#     print("Brasilia")
# elif a == 71:
#     print("Salvador")
# elif a == 11:
#     print("Sao Paulo")
# elif a == 21:
#     print("Rio De Janeiro")
# elif a == 32:
#     print("Juiz de Fora")
# elif a == 19:
#     print("Campinas")
# elif a == 27:
#     print("Vitoria")
# elif a == 31:
#     print("Belo Horizonte")
# else:
#     print("DDD nao cadastrado")                

# a = float(input())
# if 0.00<=a<=2000.00:
#     print("Isento")
# elif 2000.01<=a<=3000.00:
#     a1 = (a-2000.00)
#     a2 = (a-(2000.00+a1))*0.08
#     print("R$","{:.2f}".format(a2)) 
# elif 3000.01<=a<=4500.00:
#     a1 = (a-3000.00)*0.18
#     a2 = (a-(2000.00+(a-3000.00)))*0.08
#     print("R$","{:.2f}".format(a2+a1)) 
# elif a<4500.00:#5000
#     a1 = (a1-4500.00)*0.28
#     a2 = (a-3000.00+(a-4500.00))*0.18
#     a3 = (a-2000.00+(a-3000.00+(a-4500.00)))*0.08
#     print("R$","{:.2f}".format(a3+a2+a1))       

# Read input value
# salary = float(input())
# if salary <= 2000.00:
#     tax = 0.00
# elif salary <= 3000.00:
#     tax = (salary - 2000.00) * 0.08
# elif salary <= 4500.00:
#     tax = 1000.00 * 0.08 + (salary - 3000.00) * 0.18
# else:
#     tax = 1000.00 * 0.08 + 1500.00 * 0.18 + (salary - 4500.00) * 0.28
# if tax == 0.00:
#     print("Isento")
# else:
#     print(f"R$ {tax:.2f}")

# a = ["Fuck U", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# b = int(input())
# print(a[b])

# for i in range(1, 101):
#     if i%2 == 0:
#         print(i)

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())
# a5 = int(input())
# a6 = int(input())
# x = []
# if a1>0:
#     x.append(1) 
 
# a1 = input()
# a2 = (input())
# a3 = (input())
# a4 = (input())
# a5 = (input())
# a6 = (input())
# x = []
# # for i in range(1, 7):
# #     i = int(input())
# #     x.append(i)
# if a1>0:
#     x.append(1)
# if a2>0:
#     y.append(1)
# if a3>0:    
#     x.append(1)
# if a4>0:
#     x.append(1)
# if a5>0:
#     x.append(1)
# if a6>0:
#     x.append(1)    
# print(sum(x),"valores positivos")

# count_positive = []
# avg = []
# for _ in range(6):
#     number = float(input())
#     if number > 0:
#         count_positive.append(1)
#         avg.append(number)
# print(sum(count_positive),"valores positivos")
# print(round(sum(avg)/len(avg),1))

# count = 0
# for _ in range(5):
#     a = int(input())
#     if a%2 == 0:
#         count+=1
# print(count,"valores pares")        

# Initialize counters

# even_count = 0
# odd_count = 0
# positive_count = 0
# negative_count = 0
# for _ in range(5):
#     value = int(input())
#     if value % 2 == 0:
#         even_count += 1
#     else:
#         odd_count +=  1
#     # Check if the value is positive or negative
#     if value > 0:
#         positive_count += 1
#     elif value < 0:
#         negative_count += 1
# print(f"{even_count} valor(es) par(es)")
# print(f"{odd_count} valor(es) impar(es)")
# print(f"{positive_count} valor(es) positivo(s)")
# print(f"{negative_count} valor(es) negativo(s)")

# a = int(input())
# for i in range(1, a+1):
#     if i%2 ==0:
#         print(f"{i}^2 = {i**2}")

# n = int(input())
# in_count = 0
# out_count = 0
# for _ in range(n):
#     x = int(input())

#     if 10 <= x <= 20:
#         in_count += 1
#     else:
#         out_count += 1

# print(f"{in_count} in")
# print(f"{out_count} out")

# a = int(input())
# for i in range(1, 10000):
#     if i%a == 2:
#         print(i)

# a = int(input())
# for _ in range(a):
#     b, c, d = map(float,input().split( ))
#     e, f, g = map(float,input().split( ))
#     h, i, j = map(float,input().split( ))
#     print(round((b * 2 + c * 3 + d * 5) / 10,1))
#     print(round((e * 2 + f * 3 + g * 5) / 10,1))
#     print(round((h * 2 + i * 3 + j * 5) / 10,1))

# tb = 0
# tbc = []
# tbr = []
# tbs  = []

# a = int(input())
# for _ in range(a):
#     b, c  =input().split( )
#     bm = int(b)
#     tb+=bm

#     if 1<=bm<=15 and c=="C":
#         tbc.append(bm)
#     elif 1<=bm<=15 and c=="R":
#         tbr.append(bm)
#     elif 1<=bm<=15 and c=="S":
#         tbs.append(bm)        
# print(f"Total: {tb} cobaias")
# print(f"Total de coelhos: {sum(tbc)}")
# print(f"Total de ratos: {sum(tbr)}")
# print(f"Total de sapos: {sum(tbs)}")
# print(f"Percentual de coelhos: {'{:.2f}'.format((sum(tbc)/tb)*100,2)} %")
# print(f"Percentual de ratos: {'{:.2f}'.format((sum(tbr)/tb)*100,2)} %")
# print(f"Percentual de sapos: {'{:.2f}'.format((sum(tbs)/tb)*100,2)} %")

# i = 1
# j = 60
# while j >= 0:
#     print(f"I={i} J={j}")
#     i += 3
#     j -= 5


# for i in range(1, 10, 2):
#     for j in range(7, 4, -1):
#         print(f"I={i} J={j}")

# i = 1
# j = 7
# while i <= 9:
#     print(f"I={i} J={j}")
#     j -= 1
#     if j < 5:
#         i += 2
#         j = 7

# a = int(input())
# for _ in range(a):
#     b, c = map(int, input().split())
#     if b>c:
#         b, c = c, b
#     s = 0
#     for i in range(b+1, c):
#         if i%2 != 0:
#            s+=i
#     print(s)       

# while True:
#     a, b = map(int, input().split( ))
#     if a <= 0 or b <=0:
#         break
#     if a>b:
#         a, b= b, a
#     s = 0
#     for i in range(a, b+1):
#         print(i, end=" ")
#         s+=i
#     print(f"Sum={s}")    

# s = 0
# while s == 0:
#     a, b = map(int, input().split( ))
#     if a>b:
#         print("Decrescente")
#     elif a<b:
#         print("Crescente")
#     else:
#         s+=1

# s = 0
# while s == 0:
#     a = 2002
#     b = int(input())
#     if a != b:
#         print("Senha Invalida")
#     else:
#         print("Acesso Permitido")
#         s+=1    

# a = int(input())
# for _ in range(a):
#     b, c = map(int, input().split())
#     if 0>b and c == 0:
#         print("divisao impossivel")
#     elif c == 0:
#         print(0.0)
#     else:
#         x = (b/c) 
#         print(x)

# a = []
# count = 0
# while count != 2:
#     b = float(input())
#     if 0<b<=10:
#         a.append(b)  
#         count+=1    
#     else:
#         print("nota invalida")
# if len(a) == 2:
#     print(f"media = {'{:.2f}'.format(sum(a)/2)}")              

# option = 0
# while option != 2:
#     a = []
#     count = 0
#     while count != 2:
#         b = float(input())
#         if 0<b<=10:
#             a.append(b)  
#             count+=1    
#         else:
#             print("nota invalida")
#     if len(a) == 2:
#         print(f"media = {'{:.2f}'.format(sum(a)/2)}") 
#         while True:
#             print("novo calculo (1-sim 2-nao)")
#             option = int(input())
#             if option == 1 or option == 2:
#                 break
#         if option == 2:
#                 break   
  
# x = []
# for _ in range(2):
#     a = int(input())
#     x.append(a)
# if x[0]>x[1]:
#     x[0], x[1] = x[1], x[0]        
# y = []
# for i in range(x[0], x[1]+1):
#     if i %13 !=0:
#         y.append(i)
# print(sum(y))        

# x = 0 
# a = 0 
# g = 0
# d = 0       
# while x != 4:
#     x = int(input())
#     if x == 1:
#         a+= 1
#     elif x== 2:
#         g+= 1
#     elif x == 3:
#         d+= 1
# print("MUITO OBRIGADO") 
# print("Alcool:",a)    
# print("Gasolina:",g)  
# print("Diesel:",d)    
           
# a = int(input())
# for i in range(1, a*4, 4):
#     for j in range(2, a*4, 4):
#         for k in range(3, a*4, 4):
#             print(i,j,k, "PUM")

# x, y = map(int, input().split( ))
# y = 30
# x = 4
# for i in range(0, y):
#     #print(((i*4)-2), (i*4)-1, i*, (i*5)+1)
#     print(f"{i+1}, ")


# import random as r
# r = r.randint(9, 10)
# print(r)
# if r == 1:
#     print("_")
# elif r == 2:
#     print("_"*2)
# elif r == 3:
#     print("_"*3)
# elif r == 4:
#     print("_"*4)
# elif r == 5:
#     print("_"*5)
# elif r == 6:
#     print(" "*5,"_")    
# elif r == 7:
#     print(" "*2,"_"*2)
# elif r == 8:
#     print(" "*3,"_"*3)  
# elif r == 9:
#     print(" "*4+"_"*4)
# elif r == 10:
#     print(" "*5+"_"*5)
# # elif r == 5:
# #     print("      _____")                                              
# ss = ("""    ^ 
#    /s\\
#   | p |  
#   | a |
#  /| c |\\
# | | e | | 
# | |FlY| | 
# | /___\ | 
# |/     \|""")
# print(ss)
# A = 0
# B = 0
# C = 0
# a = "BABBBACCCB"
# for i in a:
#     if i == "B":
#         B+=1
#     elif i == "A":
#         A+=1
#     elif i == "C":
#         C+=1        
# print("b = ",B, "a = ",A, "c = ",C)



        























































