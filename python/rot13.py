from string import ascii_uppercase as alph_up
from string import ascii_lowercase as alph_lw

def rot13(message):
    
    new_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                rot13_i = alph_up.index(c)+13 if alph_up.index(c)+13 < 26 else alph_up.index(c)-13
                new_message += alph_up[rot13_i]
            elif c.islower():
                rot13_i = alph_lw.index(c)+13 if alph_lw.index(c)+13 < 26 else alph_lw.index(c)-13
                new_message += alph_lw[rot13_i]
        else:
            new_message += c
    return new_message

print({k : v for v, k in enumerate(alph_up, 1)})

print(rot13("TeSt"))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(mytable)
print(txt.translate(mytable)) 