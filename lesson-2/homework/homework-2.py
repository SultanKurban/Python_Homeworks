# 1. Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
import datetime
name = input('What is your name?')
age =  int(input('Your birth year?'))
age = int(age)  # changing type of variable
currentime = datetime.datetime.now()
currentime.year-age

# 2. Extract car names from the following text: txt = 'LMaasleitbtui'
car = 'LMaasleitbtui'
car[0::2]

# 3. Extract car names from the following text: txt = 'MsaatmiazD'
car2 = 'MsaatmiazD'
car2[0::2]

# 4. Extract the residence area from the following text: txt = "I'am John. I am from London"
text1 = "I'am John. I am from London"
text2 = text1.split()
print(text2[-1])

# 5. Reverse String. Write a Python program that takes a user input string and prints it in reverse order.
reversion = input()
reversion[::-1]

# 6. Count Vowels. Write a Python program that counts the number of vowels in a given string.
word = input("Biror so'z kiriting")
ww = word.count('a')
print("Kiritilgan so'zda {0} ta 'a' harfi bor". format(ww) )

# 7. Find Maximum Value. Write a Python program that takes a list of numbers as input and prints the maximum value.
num1 = int(input('Number - a'))
num2 = int(input('Number - b'))
num3 = int(input('Number - c'))
num4 = int(input('Number - d'))
max_num = max(num1, num2, num3, num4) 
print('berilgan a, b, c, d sonlar orasida eng kattasi = {0}'.format(max_num))

# 8. Check Palindrome. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word3 = input('Write a word')
word4 = word3[::-1]
              #input('Write a word')
if word3 == word4:
    print('this word is palindrome')
else:
    print ('this word is not palindrome')

# 9. Extract Email Domain. Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input()
email2 = email.split('.')
print(email2[-1])

# 10. Generate Random Password. Write a Python program to generate a random password containing letters, digits, and special characters.
import random 
letter = random.randint(0, 9)
print(letter)





