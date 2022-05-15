from collections import Counter

BOOK_PRICE = 8

DISCOUNTS = {2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}

def price(books):
    groups = group_into_sets(books)
    return sum(set_price(g) for g in groups)

def group_into_sets(books):
    set_sizes = []
    while books:
        unique_books = set(books)
        set_sizes.append(len(unique_books))
        for b in unique_books:
            books.remove(b)
    return set_sizes

def set_price(set_size):
    return BOOK_PRICE * set_size * DISCOUNTS.get(set_size, 1)