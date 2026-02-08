import sys
import os

# Add src directory to path using absolute path from this file's location
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sample import *

def test_answer():
    assert func(3) == 5
    
    
def test_user_name(user_name:str):
    """Test username, it must be
    - Not Empty
    - Contain no spaces
    """
    usr_nm = get_username(user_name) 
    assert usr_nm != ""
    assert " " not in usr_nm
    del usr_nm
    
    
    
    def test_password(password:str):
        """Test password, it must be
        - at least 8 characters
        - at least one number
        - at least one letter
        - at least one special character
        """
        pwd_value = get_password(password)
        assert len(pwd_value) >= 8
        assert any(char.isdigit() for char in pwd_value) 
        assert any(char.isalpha() for char in pwd_value)
        assert any(not char.isalnum() for char in pwd_value)
        del pwd_value
        
def test_email(email:str):
    """Test email, it must be
    - Contain @
    - Contain .
    - Not contain spaces
    """
    usr_email = get_email(email)
    assert "@" in usr_email
    assert "." in usr_email
    assert " " not in usr_email
    del usr_email