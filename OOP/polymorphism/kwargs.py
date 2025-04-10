def example(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

    

    

example(1, 2, 3, 4, 5, x=10, y=20)