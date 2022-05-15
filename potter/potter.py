from collections import Counter

BOOK_PRICE = 8

DISCOUNTS = {2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}

def price(books):
    sets = group_into_sets(books)
    groups = optimize_sets(sets)
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

def optimize_sets(groups):
    # It's better to group 8 books as 2 4s than a 3 and a 5.
    # Do this manually.
    #
    # This is hard coded, and there may well be edge cases
    # for combinations other than (3 + 5) | (4 + 4).
    # A solution that looks at the value of the discount per book
    # would be more flexible.
    set_sizes = Counter(groups)

    while set_sizes[3] and set_sizes[5]:
        set_sizes[3] -= 1
        set_sizes[5] -= 1
        set_sizes[4] += 2

    return list(set_sizes.elements())