from sys import argv
scripts, user_name = argv
prompt = '>'
print(f"{user_name}, I'm the {scripts} script.")
print("I'd like to ask few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"where do you live {user_name}?")
lives = input(prompt)
print(f"what kind of compuetr do you have ?")
computer = input(prompt)
print(f"""
alright, so you {likes} about liking me.
you live in {lives}. Not sure where that is.
and you have this {computer} computer. Nice.
""")

"""
run this command in command prompt.
cd to path/
activate envs
python ex14.py Krishan
"""

#study drills
from sys import argv
scripts, user_name, first, second = argv
prompt = '?'
print(f"{user_name}, I'm the {scripts} script.")
print("I'd like to ask few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"where do you live {user_name}?")
lives = input(prompt)
print(f"which was your first compuetr do you have ?")
#computer = input(prompt)
print(f"""
alright, so you {likes} about liking me.
you live in {lives}. Not sure where that is.
and you have your first computr was {first}. Nice.
""")

"""
run this command in command prompt.
cd to path/
activate envs
python ex14.py Krishan anythin anythin
"""
