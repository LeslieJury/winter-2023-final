import pytest
import _pytest.main
from Python_Start import Ask_User

def test_user_input(user):
    assert Ask_User == int



def deposit(amount):
    # In order for this program to work correctly and
    # for the bank records to be correct, we must not
    # allow someone to deposit a zero or negative amount.
    assert amount > 0

def main():
    User_Input = Ask_User()
    test_user_input(User_Input)

    pytest.main(User_Input)
