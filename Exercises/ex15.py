from sys import argv

script, filename = argv
txt = open(filename)

print(f"here is your {filename}: ")
print(txt.read())
print("type the filename again:")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())



"""
run this command in command prompt.
cd to path/
activate envs
python ex14.py Krishan
"""
