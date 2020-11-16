'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""
    def __init__(self, ipList):
        self._ipList = ipList

    @property
    def ipList(self):
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        self._ipList = newList

    def reverse_IP(self):
        for i in range(len(self._ipList)):
            ipList[i] = self._ipList[i].split('.')
            reverse_IP = [elem[::-1] for elem in ipList][::-1]
            reverse_IP.reverse()
            delimiter = '.'
            reverse_IP[i] = delimiter.join(reverse_IP[i])
            return reverse_IP

    def get_oct_1_3(self):
        for i in range(len(self._ipList)):
            get_oct_1_3 = [elem[3::] for elem in self._ipList]
            return get_oct_1_3

    def get_oct_3(self):
        for i in range(len(self._ipList)):
            get_oct_3 = [elem[9:] for elem in self._ipList]
            return get_oct_3


newList = ['10.11.12.13', '10.01.02.86']
ipList = ['10.11.12.13', '10.01.02.87']

d = IpHandler(ipList)
d.ipList = newList

print(d.ipList)

res = d.reverse_IP()
print(res)

res1 = d.get_oct_1_3()
print(res1)

res2 = d.get_oct_3()
print(res2)
