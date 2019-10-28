def add(*args):
    for each in args:
        try:
            int(each)
        except:
            raise TypeError('You can only add numbers in this digital calculator.')
    return sum(args)

def multiply(*args):
    product=1
    for each in args:
        try:
            int(each)  
        except:
            #print(f'Must be only numbers. {each} found in list.')
            raise TypeError('You can only multiply numbers in this calculator.')
        
        product *= each
    return product
