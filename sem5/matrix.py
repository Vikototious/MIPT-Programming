class Vector_3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        z_new = self.z + other.z
        
        return Vector_3D(x_new, y_new, z_new)
    
    def __mul__(self, other):
        if isinstance(self, Vector_3D) and isinstance(other, Vector_3D):       
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector_3D(self.x * other, self.y * other, self.z * other)
        
    def __rmul__(self, other):
        if isinstance(self, Vector_3D) and isinstance(other, Vector_3D):       
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector_3D(self.x * other, self.y * other, self.z * other)
    
    def __bool__(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            return False
        return True
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __str__(self):
        return f'({self.x}; {self.y}; {self.z})'
    

V0 = Vector_3D(x = 0, y = 0, z = 0)    
V1 = Vector_3D(x = 1, y = 2, z = 3)
V2 = Vector_3D(x = 2, y = 2, z = 6)

print(V1)
print(V2)
print()
print(V1 + V2)
print(V1 * V2)
print(V1 * 3)
print(3 * V1)
print(bool(V0))
print(bool(V1))
print(abs(V2))