def sort_by_value_and_index(arr):
    product = []
    i = 1
    for value in arr:
        product.append(value * i)
        i += 1
    value_product = dict.fromkeys(elem for elem in arr)
    for i, elem in enumerate(arr):
        value_product[elem] = product[i]
    value_product_sorted_by_product = sorted(value_product.items(), key=lambda value_product:value_product[1])
    sorted_values = [value[0] for value in value_product_sorted_by_product]
    return sorted_values

print(sort_by_value_and_index([23, 2, 3, 4, 5]))