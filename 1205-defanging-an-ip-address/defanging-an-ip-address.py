class Solution(object):
    def defangIPaddr(self, address):
        address=address.split(".")
        result="[.]".join(address)
        return result
        