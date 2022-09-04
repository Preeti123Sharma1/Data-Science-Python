class Cat:
    breed = None
    gender = None
    fur_color = None
    age = None
    weight = None
    height = None
    is_tamed = None

    def eat(self, food ='catfood'):
        print(f'🐕 is eating {food}')

    def play(self):
        print('🐕 is playing')

    def sleep(self):
        print('🐕 is sleeping')

billu = Cat() # constructor calling
tom = Cat()
bagadbilla = Cat()

billu.breed = 'persian'
billu.weight = 2
billu.age = 2
billu.fur_color = 'white'
billu.height = 1
billu.is_tamed = True
billu.gender = 'M'

tom.breed = 'street cat'
tom.weight = 1.5
tom.age = 10
tom.fur_color = 'brown'
tom.height = 3
tom.is_tamed = True
tom.gender = 'M'

bagadbilla.breed = 'American'
bagadbilla.weight = 4
bagadbilla.age = 5
bagadbilla.height = 3
bagadbilla.fur_color = 'goldan'
bagadbilla.gender = 'M'
bagadbilla.is_tamed = True

print('Billu details')
print('breed:',billu.breed)
print('weight:',billu.weight)
print('age:',billu.age)
print('height:',billu.height)
print('color:',billu.fur_color)
print('gender:',billu.gender)
print('pet:','yes'if billu.is_tamed else 'no')
billu.sleep()
billu.play()
billu.eat()

print('Tom details')
print('breed:',tom.breed)
print('weight:',tom.weight)
print('age:',tom.age)
print('height:',tom.height)
print('color:',tom.fur_color)
print('gender:',tom.gender)
print('pet:','yes'if tom.is_tamed else 'no')
tom.sleep()
tom.play()
tom.sleep()

print('Bagadbilla details')
print('breed:',bagadbilla.breed)
print('weight:',bagadbilla.weight)
print('age:',bagadbilla.age)
print('height:',bagadbilla.height)
print('color:',bagadbilla.fur_color)
print('gender:',bagadbilla.gender)
print('pet:','yes'if bagadbilla.is_tamed else 'no')
bagadbilla.sleep()
bagadbilla.eat('bird')
bagadbilla.eat('mouse')