class hamedend :

    def __init__(self, reality=None, picture=None):
        self.r = reality
        self.i = picture
      
    def sub(self, other):
        result=hamedend()
        result.r= self.r - other.r
        result.i= self.i - other.i
        return result

    def sum(self, other):
        result=hamedend()
        result.r= self.r + other.r
        result.i= self.i + other.i
        return result

    def mul(self, other):
        result= hamedend()
        result.r= self.r * other.r - self.i * other.i
        result.i= self.r * other.i - self.i * other.r
        return result

    def show(self):
        return str(self.r )+'+('+str(self.i) +')i'

reality1=int(input('Enter Mokhtalet Number1 Real: '))
picture1=int(input('Enter Mokhtalet Number2 Image: '))

reality2=int(input('Enter Mokhtalet Number2 Real: '))
picture2=int(input('Enter Mokhtalet Number2 Image: '))

zare1 = hamedend(reality1,picture1)
zare2 = hamedend(reality2,picture2)
print('Sum:',(zare1.sum(zare2)).show())
print('SUB:',(zare1.sub(zare2)).show())
print('Mul:',(zare1.mul(zare2)).show())