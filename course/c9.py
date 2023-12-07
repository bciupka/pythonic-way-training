# zaimplementować klasę Port
# - atrybut ip - string
# - chciałbym walidować wartość nr ip
# - wewnętrzna reprezentacja (192, 168, 0, 2)

class Port:
    def _set_ip(self, ip):
        if type(ip) is str:
            ip_t = ip.split('.')
            ip_t = [int(i) for i in ip_t]
        else:
            ip_t = ip
        if len(ip_t) != 4 or \
                any(i > 255 or i < 0 for i in ip_t):
            raise ValueError(f'Błędny nr IP: {ip}')
        self._ip = ip_t

    def _get_ip(self):
        return '.'.join(str(i) for i in self._ip)

    ip = property(fget=_get_ip, fset=_set_ip)

    @property
    def ip_tuple(self):
        return self._ip
    def __init__(self, ip):
        self.ip = ip


if __name__ == '__main__':
    p = Port('192.168.0.1')
    print(p.ip)
    p.ip = '10.0.0.1'
    print(p.ip)
    p.ip = (8, 8, 8, 8)
    print(p.ip)
    print(p.ip_tuple)
    # tu nie przechodzimy walidacji bo 999 > 255
    # p.ip = '999.999.999.999'
