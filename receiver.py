import pickle
import socket

private_key = ((117, 187), (93, 187))
dictionary = 'abcdefghijklmnopqrstuvwxyz 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$!%&*<>/?|_,.'

def decrypt(private_key, dictionary, cipher, sk):
    rsa_rem = []
    for i in cipher:
        ele = i - sk
        rsa_rem.append(ele)

    og = []
    for i in rsa_rem:
        dec = i ** private_key[1][0] % private_key[1][1]
        og.append(dec)

    ori = []
    for i in og:
        for j in dictionary:
            if i == dictionary.index(j):
                ori.append(j)

    original_text = ""
    for i in ori:
        original_text = original_text + i

    return original_text


sk = int(input("Enter the secret key: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))


while True:
    msg = s.recv(2048)
    cipher = pickle.loads(msg)
    print("The cipher text is: ", cipher)
    print("\n")
    original_msg = decrypt(private_key, dictionary, cipher, sk)
    print("Original Message is: ", original_msg)
    print("\n")
    # ch = input("Do you want to close connection?(y/n): ")
    # if ch == "y" or ch=="Y":
    #     s.close()
    #     break



