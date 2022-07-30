from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("if you want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input ("?")

print("opening the file...")
target = open(filename, 'w')
print("trincating the file. GoodBye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these three lines to file.")
target.write(line1)
target.write("\n")
tagret.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it.")
target.close()
