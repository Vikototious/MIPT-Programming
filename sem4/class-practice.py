class Cat:
  def __init__(self, age, color):
    self.age = age
    self.color = color
  
  def meow(self):
    print('meow')
  
  def get_age(self):
    print(f'cat is {self.age} years old')
  
cat_1 = Cat(2.5, 'white')

print(cat_1)
print(cat_1.age, cat_1.color)

cat_1.age = 5

print(cat_1.age, cat_1.color)

cat_1.meow()
cat_1.get_age()