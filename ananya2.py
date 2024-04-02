import random
import string
def crack_password(password):
   attempts = 0
   while True:
      guess=''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
      attempts += 1
      if guess == password:
        return attempts
password = input("Enter the password to crack:")
attempts = crack_password(password)
guess = crack password(password)
print("cracking password")
if guess:
    print(f"Password cracked in {attempts} attempts. The password is {guess}.")
else:
    print(f"Password not cracked after {attempts} attempts.")

    


