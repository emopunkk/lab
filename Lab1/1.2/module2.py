def calculate_sum_and_product():
    sum_even = 0
    prod_odd = 1
    for i in range(21):
        if i % 2 == 0:
            sum_even += i
        else:
            prod_odd *= i      
    return sum_even, prod_odd