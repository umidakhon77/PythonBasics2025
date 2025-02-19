print("Hello World")
import sys
#line one was updated change
#might change
# 1. add TC-3,
# 2. click file in left side
# 3. write comment in left side at the bottom -> commit button(кнопка)
#4.  press commit button
#5. top one would be last changed with u comments (kind name), u should check at the top one and
#6. if click this green one twice it show in the buttom two files
#7. one file with changes would be with green color - mean

name ='\n\t    john    doe'
print(f'Welcome back, {name.strip().title()}! Glad to see u again!')
#strip()  remove leading & trailing whitespace not between text

print(name.replace('o', 'u'))
print(f'Welcome back, {name.replace('o', 'u').strip().title()}! Glad to see u again!')


msg='Hello!'
print(msg)
print(msg.replace('!', '?'))
print(f"I'm using this file: {__file__}")
print(f"I'm using this file: {sys.platform}")