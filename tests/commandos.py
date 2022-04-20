from nose.tools import *
import commandos

def setup():
    print("KONFIGURACJA!")

def teardown():
    print("ZAMYKANIE!")

def test_basic():
    print("URUCHOMIONO TEST!")
