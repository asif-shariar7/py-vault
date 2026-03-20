import random
import time

def otp_generator():
    return random.randrange(1000,9999)

otp = otp_generator()
print("Your OTP is",otp)

start_time = time.time()  #gives the current time in second.This stores the time when OTP was created 
user_otp = int(input("Enter OTP: "))


if time.time() - start_time > 30:    #This calculates how many seconds have passed since OTP was generated.
    print("OTP Expired")

elif user_otp == otp:
    print("Verified OTP")

else:
    print("Wrong OTP")    