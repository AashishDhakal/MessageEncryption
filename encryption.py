alphabets="abcdefghijklmnopqrstuvwxyz"
up_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt():
    key=int(input("Enter the secret key to encrypt your messages"))
    Message=input("Enter the Message:")
    newMessage=""
    for character in Message:
        if character in alphabets:
            position=alphabets.find(character)
            newPosition=(position+key)%26
            newCharacter=alphabets[newPosition]
            newMessage += newCharacter
        elif character in up_alphabets:
            position=up_alphabets.find(character)
            newPosition=(position+key)%26
            newCharacter=up_alphabets[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print(newMessage)
def decrypt():
    key=int(input("Enter the secret key to decrypt your messages"))
    Message=input("Enter the Message:")
    newMessage=""
    for character in Message:
        if character in alphabets:
            position=alphabets.find(character)
            newPosition=(position-key)%26
            newCharacter=alphabets[newPosition]
            newMessage += newCharacter
        elif character in up_alphabets:
            position=up_alphabets.find(character)
            newPosition=(position-key)%26
            newCharacter=up_alphabets[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print(newMessage)

print("-----------------------Press E for Encrypt and D for Decrypt---------------")
user_Choice=input("Do you want to Encrypt or Decrypt?")

if user_Choice=="E":
    encrypt()
elif  user_Choice=="D":
    decrypt()
else:
    print("Please enter either E or D")

