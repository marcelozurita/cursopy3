import copy

def safe_string_params_function(func) :
    def __func__(*args, **kwargs) :
        for arg in args :
            check_string(arg)

        result = func(*args, **kwargs)
        return result
    
    return __func__

def check_string(x) :
    if not isinstance(x, str) :
        raise TypeError('param is not str')

@safe_string_params_function
def string_invert(string) :
    return string[::-1]


# safe_string_invert = safe_string_params_function(string_invert)

inverted = string_invert('Marcelo')
print(inverted)



# decorator functions with parameters
def reduce_sample(n_mins=0, nmaxs=0) :
    print('reduce_sample')

    def decorator_func(func) :
        print('decorator')

        def __func__(*args, **kwargs) :
            print('nested')
            newargs = list(copy.copy(args))

            newargs.sort()
            print(newargs)
            newargs = newargs[n_mins:-nmaxs]

            res = func(*newargs, **kwargs)
            return res
        
        return __func__
    
    return decorator_func


@reduce_sample(2, 2)
def sum(*args):
    v = 0
    for n in args :
        v += n
    return v

@reduce_sample(2, 2)
def avg(*args):
    v = 0
    for n in args :
        v += n
    return v / len(args)

sample = [10, 5, 11, 12, 19, 42, 13, 14]

print(sample)
print('Sum: ', sum(*sample))
print('Avg: ', avg(*sample))