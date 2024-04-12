"""Unit testing for ip_functions."""
import pytest
import ip_functions

def test_is_valid_ip():
    """Test cases for is_valid_ip."""
    assert ip_functions.is_valid_ip("0.0.0.0")          is True
    assert ip_functions.is_valid_ip("255.255.255.255")  is True
    assert ip_functions.is_valid_ip("10.1.2.0")         is True
    assert ip_functions.is_valid_ip("256.0.0.0")        is False
    assert ip_functions.is_valid_ip("10.256.0.0")       is False
    assert ip_functions.is_valid_ip("10.1.256.0")       is False
    assert ip_functions.is_valid_ip("10.1.0.256")       is False
    assert ip_functions.is_valid_ip("a.0.0.c")          is False

def test_convert_to_bit_list():
    """Test cases for convert_to_bit_list."""
    assert ip_functions.convert_to_bit_list("0.0.0.0")         == ['00000000', '00000000', '00000000', '00000000']
    assert ip_functions.convert_to_bit_list("255.255.255.255") == ['11111111', '11111111', '11111111', '11111111']
    assert ip_functions.convert_to_bit_list("10.1.2.0")        == ['00001010', '00000001', '00000010', '00000000']
    with pytest.raises(ValueError, match="Invalid IP address"):
        ip_functions.convert_to_bit_list("10.256.0.0")
    with pytest.raises(ValueError, match="Invalid IP address"):
        ip_functions.convert_to_bit_list("a.0.0.c")
    with pytest.raises(ValueError, match="Invalid IP address"):
        ip_functions.convert_to_bit_list("256.0.0.0")

def test_is_valid_cidr():
    """Test cases for is_valid_cidr."""
    assert ip_functions.is_valid_cidr("10.0.0.0/24") is True

