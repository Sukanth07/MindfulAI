def add_end(l,n):
    l.append(n)
    return l

def add_beg(l,n):
    l.insert(0,n)
    return l

def remove_func(l,n):
    l.remove(n)
    return l

def remove_pop(l):
    l.pop()
    return l

def slice(l, st, end):
    l = l[st:end]
    return l

def rev(l):
    l = l[::-1]
    return l

def check(l,element):
    if element in l:
        return "AVAILABLE"
    else:
        return "NOT AVAILABLE"


def singly_linked_list(l):
    s_list = []
    for i in range(len(l)):
        inner = []
        data = l[i]
        address = i+1
        if i==len(l)-1:
            address = None        
        inner.append(data)
        inner.append(address)
        s_list.append(inner)
    return s_list


def print_res(l):
    print("Original List: ", l)
    print("Append 18 to List: ", add_end(l,18))
    print("Prepend 0 to List: ", add_beg(l,0))
    print("Remove element 13: ", remove_func(l,13))
    print("Pop last element: ", remove_pop(l))
    print("Slice from 1 to 3(exclusive): ", slice(l,1,3))
    print("Reverse the list: ", rev(l))
    print("Checking for element 6 in List: ", check(l,6))


def freq(s):
    d = {}
    for i in s:
        if i==' ':
            continue
        
        if i in d.keys():
            d[i]+=1

        else:
            d[i] = 1
    print(d)
            

    
l = [11, 12, 13, 15, 26]
print_res(l)

print(f"Singly Linked List Simulation for {l} is : {singly_linked_list(l)}")

freq("Mississipi")

