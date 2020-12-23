from automation import __version__
from automation.automation import get_emails, get_phone_numbers, format_phone_number

def test_version():
    assert __version__ == '0.1.0'

"""
Test Cases:
1. Can successfully return emails in the correct format.
2 Can successfully return phone numbers in the correct format.
"""

def test_auto_email():
    assert (get_emails("./potential-contacts.txt"))[0] == 'johnsonkristi@anthony.com'

def test_auto_phone():
    assert (get_phone_numbers("./potential-contacts.txt"))[0] == '517-970-9076'
