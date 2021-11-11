
EN = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz01234567890123456789"
encrypt = input("Enter a message: ")
key = int(input("Enter a key(1-25): "))
encrypt = encrypt.lower()
encrypted = ""
for letter in encrypt:
    letpos = EN.find(letter)
    newpos = letpos + key
    if letter in EN:
        encrypted = encrypted + EN[newpos]
print("Your encrypted message is: ",encrypted)
