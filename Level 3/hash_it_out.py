def answer(digest):

    message = [0 for x in range(len(digest))]

    for i in range(len(digest)):
        message[i] = ((digest[i] ^ message[i - 1]) * 129) % 256

    return message


def encrypt(message):

    # message[-1] = 0
    # only loop in range(len(message) - 1)
    message.append(0)

    digest = [0 for x in range(len(message) - 1)]

    for i in range(len(message) - 1):
        digest[i] = ((129 * message[i]) ^ message[i - 1]) % 256

    return digest


message = [13, 17]
digest = [141, 156]

print(encrypt(message))
print(answer(digest))
