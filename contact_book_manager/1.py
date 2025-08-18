class Alpha:
    def process(self):
        print("Alpha processed")

class Beta(Alpha):
    def process(self):
        print("Beta processed")

class Gamma(Alpha):
    def process(self):
        print("Gamma processed")

class Delta(Beta, Gamma):
    pass

# Creating object of Delta
d = Delta()

# Call to process()
print("MRO-based process call:")
d.process()  # Should print "Beta processed"

# Explicitly calling all versions without using super()
print("\nExplicit calls:")
Beta.process(d)    # Beta's version
Gamma.process(d)   # Gamma's version
Alpha.process(d)   # Alpha's version
'''Delta(Beta, Gamma) —> MRO: Delta → Beta → Gamma → Alpha → object

So, d.process() uses Beta's method.

We manually call all others using class names.'''
