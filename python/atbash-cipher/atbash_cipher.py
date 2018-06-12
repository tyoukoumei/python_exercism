from string import ascii_lowercase
Length = 5
Plain = ascii_lowercase
Cipher = ascii_lowercase[::-1]

def base_trans(text):
    Emp = ''
    for i in text:
        if i.isalnum():
            Emp += i
    return Emp.lower().translate(Emp.maketrans(Plain,Cipher))

def encode(plain):
    cipher1 = base_trans(plain)
    cipher1_list = []
    for i in range(0, len(cipher1), Length):
        cipher1_list.append((cipher1[i:i + Length]))
    return " ".join(cipher1_list)

def decode(ciphered):
    return base_trans(ciphered)
