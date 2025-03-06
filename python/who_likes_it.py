#https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    len_n = len(names)
    match len_n:
        case 0:
            return "no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} likes this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} likes this"
    return f"{names[0]}, {names[1]} and {len_n-2} others people likes this"

print(likes(["Cécile", "Jason", "Jennifer", "Maxime", "Kévin"]))