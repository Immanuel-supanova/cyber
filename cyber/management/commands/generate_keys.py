from typing import Any
from django.core.management.base import BaseCommand
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class Command(BaseCommand):
    help = 'Generates RSA keys'

    def handle(self, *args: Any, **options: Any) -> str | None:
        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
        public_key = private_key.public_key()

        # Serialize keys to PEM format
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Write keys to files
        with open("private_key.pem", "wb") as f:
            f.write(private_pem)
            
        with open("public_key.pem", "wb") as f:
            f.write(public_pem)
        print("RSA keys have been generated")