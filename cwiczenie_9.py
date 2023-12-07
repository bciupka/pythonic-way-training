# zaimplementować klasę Port
# - atrybut ip - string
# - chciałbym walidować wartość nr ip
# - wewnętrzna reprezentacja (192, 168, 0, 2)

class Port:
    def __init__(self, ip):
        self._ip = ip

    @property
    def ip(self):
        if type(self._ip) == tuple:
            self._ip = '.'.join(self._ip)
        list = self._ip.split('.')
        if len(list) == 4 and all([int(i) <= 255 for i in list]):
            return self._ip
        else:
            return 'Wrong IP'

    @ip.setter
    def ip(self, new_ip):
        if type(new_ip) == tuple:
            self._ip = '.'.join(str(new_ip))
        list = self._ip.split('.')
        if len(list) == 4 and all([int(i) <= 255 for i in list]):
            return self._ip
        else:
            return 'Wrong IP'


if __name__ == '__main__':
    p = Port('192.168.0.1')
    print(p.ip)
    p.ip = '10.0.0.1'
    print(p.ip)
    p.ip = (8, 8, 8, 8)
    print(p.ip)
    # print(p.ip_t)
    # tu nie przechodzimy walidacji !
    p.ip = '999.999.999.999'