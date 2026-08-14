import hashlib
import os
import json
from cryptography.fernet import Fernet

class CIAVault:
    def __init__(self, log_file="vault_logs.json"):
        self.log_file = log_file
        self.users = {"admin": "password123"}  # Basic Auth Control
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.vault_data = None
        self.vault_hash = None

    def authenticate(self, username, password):
        """Authorization Control Check"""
        return self.users.get(username) == password

    def write_secure_data(self, secret_text: str):
        """Confidentiality & Integrity Action"""
        encrypted_bytes = self.cipher.encrypt(secret_text.encode())
        self.vault_data = encrypted_bytes
        self.vault_hash = hashlib.sha256(encrypted_bytes).hexdigest()
        
        # Save to actual local file
        log_payload = {
            "ciphertext": encrypted_bytes.decode(),
            "integrity_hash": self.vault_hash
        }
        with open(self.log_file, "w") as f:
            json.dump(log_payload, f)
        return True

    def read_secure_data(self, username, password):
        """CIA Verification Pipeline"""
        if not self.authenticate(username, password):
            return "AUTH_FAILURE"
            
        # Availability Check
        if not os.path.exists(self.log_file) or self.vault_data is None:
            return "AVAILABILITY_FAILURE"

        # Integrity Check
        current_hash = hashlib.sha256(self.vault_data).hexdigest()
        if current_hash != self.vault_hash:
            return "INTEGRITY_FAILURE"

        # Confidentiality Check
        try:
            return self.cipher.decrypt(self.vault_data).decode()
        except Exception:
            return "CONFIDENTIALITY_FAILURE"

    def tamper_with_data(self):
        """Simulates an attack string modification"""
        if self.vault_data:
            self.vault_data += b"malicious_injection"
