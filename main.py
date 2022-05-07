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
    result = 0
    while(len(books) != 0):
        uniNum = len(Counter(books).keys())
        if len(books) < 10 and uniNum == 5:
            c = 0
            for k in Counter(books).keys():
                if c == 0:
                    uniNum -= 1
                    c += 1
                    continue
                c += 1
                books.remove(Counter(books).most_common()[0][0])
        else:
            for k in Counter(books).keys():
                books.remove(Counter(books).most_common()[0][0])
        print(uniNum, (1-Discount[uniNum]))
        result += EUR_ONE_BOOK * (uniNum * (1-Discount[uniNum]))
    return round(result, 2)


if __name__ == "__main__":
    books = [0, 0, 1, 1, 2, 2, 3, 4]
    print(price(books))
# 2 * (8 * 4 * 0.8), price(
