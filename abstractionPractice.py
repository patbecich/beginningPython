z = 8

def fibs(ran):
    seq = [0,1]
    for i in range (ran-2):
        seq.append(seq[-2] + seq[-1])
    return seq

def test():
    print 'This is printed'
    return
    print 'This is not'

def try_to_change(n):
    print n
    n = 10
    z = 5
    print n
    return n



def add(m):
    m = try_to_change(m)
    return m + 5

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1,'')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
def print_params(*params):
    print params

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def power(x,n):
    result = 1
    for i in range(n):
        result *= x
    return result
