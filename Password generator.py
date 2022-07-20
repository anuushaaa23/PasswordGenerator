import random  
import re       

Replaced=[]

#function to generate passwords
def generatePassword(length):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    passwords=[] #List containing all the generated passwords
    
    for i in length:
        password=""
        for j in range(i):
            alpha_index=random.randrange(len(alphabet))  #choosing an alphabet index in random
            password=password+alphabet[alpha_index]      #updating the password string with chosen alphabet
    
        password=replaceWithUpperCaseLetter(password)    #calling function to replace some letters with corresponding uppercase letters
        password=replaceWithNumber(password)             #calling function to replace some letters with numbers
        password=replaceWithSpecialCharacter(password)
    
        passwords.append(password) #appending the generated password to list
        
    return passwords

#function for replacing some letters with corresponding uppercase letters at random
def replaceWithUpperCaseLetter(password): 
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password)//2)
        Replaced.append(replace_index)
        #using regular expression method sub() to substitute the letter with uppercase
        password = re.sub(password[replace_index],password[replace_index].upper(),password)
        return password

#function to replace some letters with numbers
def replaceWithNumber(password):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password)//2,len(password))
        Replaced.append(replace_index)
        #using regular expression method sub() to substitute the letter with number
        password = re.sub(password[replace_index],str(random.randrange(10)),password)
        return password      

#function to replace some letters with special characters
def replaceWithSpecialCharacter(password):
    char="`~!@#$%^&*()_-+={[}]|\"':;?/>.<,"
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password))
        if replace_index not in Replaced:
            #using regular expression method sub() to substitute the letter with special character
            password = re.sub(password[replace_index],char[random.randrange(len(char))],password)
        return password

def main():
    
    numPasswords=int(input("Enter the number of passwords you want to generate : "))
    print("\n-----------Generating "+str(numPasswords)+" passwords-----------\n")
    
    length=[]
    for i in range(numPasswords):
        leng = int(input("Enter the length of the password "+str(i+1)+" : "))
        length.append(leng)
        
    passwords = generatePassword(length)
    
    for i in range(len(passwords)):
        print("\nPassword "+str(i+1)+" :"+passwords[i])
        
main()

