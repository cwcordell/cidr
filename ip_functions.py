"""Helper functions for IP and CIDR"""
def is_valid_ip(ip:str):
  """Checks that the passed IP address is valid. Returns True or False."""

  ip_segments = ip.split('.')
  
  # Check if there are 4 items (segments)
  if len(ip_segments) != 4:
    return False
  
  # Loop segments and check that they are integers between 0 and 255
  for s in ip_segments:
    if not s.isnumeric() or int(s) > 255 or int(s) < 0:
      return False

  return True

def is_valid_cidr_mask(mask:int):
  """Checks if the passed argument is a valid CIDR mask. Returns True or False."""
  if 1 > mask > 32:
    return False
  return True

def is_valid_cidr(cidr:str):
  """Checks that a CIDR (IP/mask) is valid. Returns True or False."""
  sl = cidr.split("/")
  if len(sl) != 2 or not is_valid_cidr_mask(int(sl[1])) or not is_valid_ip(sl[0]):
    return False
  return True

def convert_to_bit_list(ip:str):
  """Converts an IP to a list of bits. Returns a list with four items representing the four segments where each is in binary representation."""
  if not is_valid_ip(ip):
    raise ValueError("Invalid IP address")
  return [format(int(i), "08b") for i in ip.split('.')]
  

if __name__ == "__main__":
  print(is_valid_ip("10.0.0.3"))
  # print(is_valid_ip("300.0.0.3"))
  # print(is_valid_ip("a.0.0.c"))
  # print(convert_to_bit_list("0.0.0.0"))
  # print(format(10, "08b"))
  # is_valid_cidr(21)