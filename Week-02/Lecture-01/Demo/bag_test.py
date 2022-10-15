# بسم الله الرحمن الرحيم

def main():
    from bag import Bag

    my_bag = Bag()

    my_bag.add(12)
    my_bag.add(14)
    my_bag.add(13)

    print(f'Length of items in my bag: {len(my_bag)}')

    for item in my_bag:
        print(item)

    12 in my_bag

if __name__ == '__main__':
    main()