
def bi_iter(lst):
    _isEven = len(lst) % 2 == 0
    if _isEven:
        for i in range(0, len(lst), 2):
            print(i, lst[i])
            print(i+1, lst[i+1])
    else:
        for i in range(0, len(lst), 2):
            if i == len(lst) - 1:
                print("QUITTING")
                break;
            else:
                print(i, lst[i])
                print(i+1, lst[i+1])


lst = ['index ONE', 'index TWO', 'index THREE']

bi_iter(lst)