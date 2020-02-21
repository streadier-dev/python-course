if __name__ == '__main__':
    #Sets no permiten elementos repetidos
    s = set([1, 2, 3])
    t = set([3, 4, 5])
    s.add(4)
    #s.remove(2)
    s.update(t)
    print(s)
    print(s.union(t))
    print(s.intersection(t))
    print(s.difference(t))
    print(t.difference(s))
    if 1 in t or s:
        print('esta en la lista')
    else:
        print('no esta en la lista')