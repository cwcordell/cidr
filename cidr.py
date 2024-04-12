import ipBase, ip_functions

class CIDR(ipBase.IpBase):
  def __init__(self, cidr:str):
    # if not cidr.contains("/"):
    #   throw Exception("CIDR is not valid")
    ip_mask = cidr.split("/")
    if len(ip_mask) != 2:
      print('ERROR: {cidr} is not a valid CIDR. Expected CIDR in format like 10.1.2.0/24')

    self.mask = ip_mask[1]
    super().__init__(ip_mask[0])
    
  def __str__(self):
    return f'{self.ip}/{self.mask}'
  
  @mask.setter
  def mask(self, x):
    if not (0 < x <= 32):
      raise Exception("mask must be greater than 0 but less than or equal to 32")
    self._mask = x
  
  def contains(self, ip):
    bl, err = ip_functions.convert_to_bit_list(ip)
    return True
    
if __name__ == "__main__":
  c = CIDR("10.1.2.0/24")
  print(c)
