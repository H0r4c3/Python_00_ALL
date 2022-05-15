'''
Created on Dec 26, 2020

@author: Horace.000
'''

from app0 import books

def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)
        
print('---BEST---')
print_best_books()
print('---CHEAPEST---')
print_cheapest_books()