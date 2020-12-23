Key = (int(input("Set a Key: ")))
sentence = input("Your sentence: ")


def encode(t, k):
    global encodedmessage
    result = []
    for char in t:
        encodedmessage = (ord(char) - 32 + k) % 95 + 32
        result.append(chr(encodedmessage))
    return result


def decode(t, k):
    result = []
    for char in t:
        decodedmesage = ord(char) - 32 - k
        while decodedmesage < 0:
            decodedmesage = decodedmesage + 95
        decodedletter = decodedmesage % 95 + 32
        result.append(chr(decodedletter))
    return result


def split(word):
    return [char for char in word]


def stitch(para):
    uni = ""
    for i in para:
        uni += i
    return uni


code = split(sentence)

encodedmessage = encode(code, Key)
print(encodedmessage)
print('Encoded message: ', stitch(encodedmessage))
decoded_char = decode(encodedmessage, Key)
print(decoded_char)
print('Decoded message: ', stitch(decoded_char))
