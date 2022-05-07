from collections import Counter
# One copy of any of the five books costs 8 EUR.
EUR_ONE_BOOK = 8
# 2 different books: 5 % discount on those two books.
Discount = {
    1: 0,
    2: .05,
    3: .10,
    4: .20,
    5: .25
}
# 3 different books: 10 % discount.
# 4 different books, 20 % discount.
# 5, you get a huge 25 % discount.


def price(books: list):
    total = Counter(books).total()
    uniNum = len(Counter(books).keys())
    return EUR_ONE_BOOK * total * (1-Discount[uniNum])


if __name__ == "__main__":
    books = [0, 1, 2, 3, 3]
    price(books)
