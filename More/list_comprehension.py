## Normal loop

square = []

for i in range(5):
    square.append(i*i)

print(square) 

## list comprehension

# l = [i*i for i in range(5)]
# print(l)

## list comprehension with condition

l = [i for i in range(10) if i % 2 != 0]
print(l)    ## odd number

## multiple loops

li = [[i,j] for i in range(2) for j in range(2)]
print(li)



## hackerrank problem (list comprehension)
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] 
          for i in range(x+1) 
          for j in range(y+1) 
          for k in range(z+1) 
          if i + j + k != n]

print(result)


## if the number is even then multiply by 2 , if the number is odd then keep it the same 
# l = [i*2 if i%2 == 0 else i for i in range(5)]
# print(l)     # output [0,1,4,3,8]


### check notes for syntax 