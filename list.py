beatles = [] 
print("Step 1:", beatles)

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Step 2:", beatles)

for i in ['Stu Sutcliffe', 'Pete Best']:
    beatles.append(i)
print("Step 3:", beatles)

del beatles[4]
del beatles[3]  
print("Step 4:", beatles)

beatles.insert(0, 'Ringo Starr')
print("Step 5:", beatles)

print("The Fab", len(beatles))
