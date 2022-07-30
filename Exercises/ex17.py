from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Copything from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long.")

print(f"does the output file exists? {exists(to_file)}.")
print("Ready, hit RETURN o continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright. All done")

out_file.close()
in_file.close()

"""
to create file using cmd prompt use
echo "this is a test file." > ex17_test.txt
#then look at it
cat ex17_text.txt

then
pyhton ex17.py ex17_test.txt new_ex17_test.txt
"""
