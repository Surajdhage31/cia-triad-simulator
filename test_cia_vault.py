import pytest
import os
from cia_vault import CIAVault

@pytest.fixture
def vault():
    # Setup test file
    test_vault = CIAVault(log_file="test_vault.json")
    yield test_vault
    # Teardown local file after testing
    if os.path.exists("test_vault.json"):
        os.remove("test_vault.json")

def test_confidentiality_and_integrity_pass(vault):
    vault.write_secure_data("TopSecret")
    result = vault.read_secure_data("admin", "password123")
    assert result == "TopSecret"

def test_authorization_control_fail(vault):
    vault.write_secure_data("TopSecret")
    result = vault.read_secure_data("admin", "WRONG_PASSWORD")
    assert result == "AUTH_FAILURE"

def test_integrity_breach_detection(vault):
    vault.write_secure_data("TopSecret")
    vault.tamper_with_data()
    result = vault.read_secure_data("admin", "password123")
    assert result == "INTEGRITY_FAILURE"

def test_availability_loss(vault):
    vault.write_secure_data("TopSecret")
    if os.path.exists("test_vault.json"):
        os.remove("test_vault.json") # Delete file to simulate outage
    result = vault.read_secure_data("admin", "password123")
    assert result == "AVAILABILITY_FAILURE"
