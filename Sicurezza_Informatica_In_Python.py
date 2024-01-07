from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

def generate_key_pair():
    # Genera una coppia di chiavi pubblica e privata RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Serializza e salva la chiave privata su disco
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private_key.pem', 'wb') as f:
        f.write(private_pem)

    # Serializza e salva la chiave pubblica su disco
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(public_pem)

def encrypt_decrypt_message(message, public_key):
    # Carica la chiave pubblica da un file
    with open(public_key, 'rb') as f:
        public_key_bytes = f.read()
        public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())

    # Cifra il messaggio con la chiave pubblica
    ciphertext = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print(f'Messaggio cifrato: {ciphertext.hex()}')

    # Decifra il messaggio con la chiave privata
    with open('private_key.pem', 'rb') as f:
        private_key_bytes = f.read()
        private_key = serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())

    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(f'Messaggio decifrato: {decrypted_message.decode("utf-8")}')

if __name__ == "__main__":
    # Genera una coppia di chiavi (eseguire solo una volta)
    generate_key_pair()

    # Esempio di cifratura e decifratura di un messaggio
    message = "Questo è un messaggio segreto!"
    encrypt_decrypt_message(message, 'public_key.pem')
