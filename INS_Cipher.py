import random
import hashlib

charData = input("Enter the message: ")


def rsa():
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        d = x % m
        if d == a:
            raise Exception('Please select a larger prime numbers next time!')
        else:
            return d

    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num ** 0.5) + 2, 2):
            if num % n == 0:
                return False
        return True

    def generate_keypair(p, q):
        if not (is_prime(p) and is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')

        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randrange(1, phi)

        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)

        d = modinv(e, phi)

        return (e, n), (d, n)

    p = int(input("Enter p: "))
    q = int(input("Enter q: "))

    cc = generate_keypair(p, q)

    return cc


private_key = rsa()
print("The public and private key is: ", private_key)


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


original_msg = decrypt(private_key, dictionary, cipher, sk)
print("Original Message is: ", original_msg)
