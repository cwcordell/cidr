ip    = "10.0.0.1"     # 00001010 00000000 00000000 00000001
cidr  = "10.0.0.0/24"  # 00001010 00000000 00000000 00000000

def get_mask():
  cidr_ip, cidr_mask = cidr.split("/")
  print(f'cidr_ip: {cidr_ip}, cidr_mask: {cidr_mask}')
  return cidr_ip, cidr_mask

def is_ip_in_cidr():
  for i in range(cidr_ip):
    print(i)
  return True
  
  
  
cidr_ip, cidr_mask = get_mask()
is_ip_in_cidr()