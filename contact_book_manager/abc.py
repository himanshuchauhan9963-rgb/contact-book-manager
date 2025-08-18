class cat:
    def _init_(self, name, age):
        self.name = name
        self.age = age # instance variable

    def display_attributes(self):
        print(f'Cat name: {self.name}')
        print(f'Cat age: {self.age}')

    def _str_(self):
        return f'Cat name: {self.name}, cat age:{self.age}'

# moine-coon
# ragdoll
# british shorthair
# perston

cat1 = cat("Silvia", 3)
cat2 = cat("Sam", 6)
cat3 = cat("Shiro", 0)