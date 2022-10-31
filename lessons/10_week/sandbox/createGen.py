def createGenerator():
  myVal = range(6)
  for i in myVal:
    # find the square of the value as needed
    yield i*i
# end of createGenerator()


# Initiation: create a generator
myGenerator = createGenerator()
# Where is this generator in memory?
print(myGenerator)
for i in myGenerator:
  print("\t A: myGenerator: ",i)
for i in myGenerator:
  print("\t B: myGenerator: ",i)
