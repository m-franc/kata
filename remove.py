#https://www.codewars.com/kata/57faf32df815ebd49e000117/train/python

def remove(st):
    st_arr = st.split()
    new_sts = []
    for st in st_arr:
        nb_mark = 0
        st_rev = str(reversed(st))
        print(st_rev)
        for c in st_rev:
            nb_mark += 1
            if c != "!":
                break
        new_sts.append(st[:-nb_mark+1])
    return new_sts

print(remove("!!!Hi !!hi!!! !hi"))