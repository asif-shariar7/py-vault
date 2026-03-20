tweet = "slow but steady wins the race"

print (tweet[1])  #l
print (tweet[:4]) #slow (1 kom 0-3 print)
print(tweet[-4])  #r
print(tweet[-4:])  #race
print(tweet[12:18]) #ady wi

# Skip letters
print(tweet[::3]) #write first lettter skip 2 letters, then next letter comes then again skip...
print(tweet[::-1]) #reverse string

name = "Asif"
age = 24

print("Hello I am {} and I am {} years old".format(name,age))
#or
print(f"Hello I am {name} and I am {age} years old")
#join or concatination
print(name + str(age))

print(tweet.capitalize())  #Ex - Hello asif
print(tweet.title())       #Ex - Hello Asif

print(tweet.upper())       
print(tweet.lower())
print(tweet.count('o'))
print(tweet.split())     #split each word in list


quote = "Sunny shouted: \"This planet is too green!\"\nThen he ran away...\n\t*dramatic exit*"
# \" \"  double quote
print("Tweet with escape characters:")
print(quote)

messy = "I am #@Asiffff #$"
num = 9.3721
fixed = messy.replace('#','').replace('@','').replace('ffff','f').replace('$','.')
print(f"Num : {num:.2f} and",fixed)
