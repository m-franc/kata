#def compare(array_1, array_2):

 #   common = []

#    for elem_1 in array_1:
 #       for elem_2 in array_2:
 #           if elem_1 == elem_2:
  #              common.append(elem_1)
   # return common 

def common(a, b, c):

    sum = 0
    
    for elem_a in a:
        for elem_b in b:
            for elem_c in c:
                if elem_a == elem_b:
                    sum = sum + elem_a
                elif elem_b == elem_c:
                    sum = sum + elem_b
                elif elem_a == elem_c:
                    sum = sum + elem_c
                    
    return sum
    

print(common([1,2,2,3],[5,3,2,2],[7,3,2,2]))