# rsa алгоритм шифрования
import sys
import rsa


def code(message):
    '''
    :param message: сообщение для зашифровки.
    :return: зашифрованное сообщение и расшифрованное.
    '''
    (pubkey, privkey) = rsa.newkeys(512)
    print('Исходное сообщение', message)

    crypto = rsa.encrypt(message, pubkey)
    message = rsa.decrypt(crypto, privkey)
    print(crypto)
    print(message)


code(b'ASV')
