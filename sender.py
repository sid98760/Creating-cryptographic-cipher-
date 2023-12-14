import socket
import pickle
import hashlib

charData = input("Enter the message: ")

private_key = ((117, 187), (93, 187))



def value(no):
    enc1 = str(no)
    val = hashlib.sha1(enc1.encode())
    count = 0
    while True:
        enc2 = str(no) + str(count)
        val2 = hashlib.sha1(enc2.encode())
        new_val = val2.hexdigest()
        if new_val[0] == '0':
            break
        else:
            count += 1

    return count


dictionary = 'abcdefghijklmnopqrstuvwxyz 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$!%&*<>/?|_,.'


def encrypt(private_key, dictionary, charData):
    no = []
    for i in charData:
        for j in dictionary:
            if i == j:
                a = dictionary.index(i)
                enc = a ** private_key[0][0] % private_key[0][1]
                no.append(enc)
    val = value(no)
    no1 = []
    for i in no:
        no1.append(i + val)
    return no1, val

cipher, sk = encrypt(private_key, dictionary, charData)
print("The secret key is: ", sk)
print("The cipher text is: ", cipher)
print("\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg = pickle.dumps(cipher)
    clientsocket.send(msg)
    print("Sended ciphertext")

    # break




