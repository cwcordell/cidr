import ip_functions

class IpBase:
  def __init__(self, ip):
    if ip_functions.is_valid_ip(ip):
      self.ip = ip

  