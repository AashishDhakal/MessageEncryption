alphabets="abcdefghijklmnopqrstuvwxyz"
key=int(input("Enter the secret key to encrypt your messages"))
Message=input("Enter the Message:")
newMessage=""
for character in Message:
    if character in alphabets:
        position=alphabets.find(character)
        newPosition=(position+key)%26
        newCharacter=alphabets[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character
print(newMessage)
