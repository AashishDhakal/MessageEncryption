alphabets="abcdefghijklmnopqrstuvwxyz"
up_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
