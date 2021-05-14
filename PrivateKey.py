from EllipticCurve import G

class PrivateKey:

    def __init__(self , secret):
        self.secret = secret
        self.point = secret * G

    def hex(self):
        return '{:x}'.format(self.secret).zfill(64)
