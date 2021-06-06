class Animal:
    def play(self):
        print("i like to play")

class Dog(Animal):
    def like(self):
        print("i like playing ball")

class Cat(Animal):
    def sleep(self):
        print("i love to sleep under the tree")

dog1 = Dog()
dog1.play()
dog1.like() 

cat1 = Cat()
cat1.sleep() 
cat1.play()
