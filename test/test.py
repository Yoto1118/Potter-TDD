from __future__ import absolute_import
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from potter.potter import price

def testBasics():
    book_list = []
    assert price(book_list) == 0

    for i in range(1, 5):
        book_list = [i]
        assert price(book_list) == 8
    
    book_list = [1, 1, 1]
    assert price(book_list) == 8 * 3

def testSimpleDiscounts():
    book_list = [0, 1]
    assert price(book_list) == 8*2 * 0.95

    book_list = [0, 2, 4]
    assert price(book_list) == 8*3 * 0.9

    book_list = [0, 1, 2, 4]
    assert price(book_list) == 8*4 * 0.8

    book_list = [0, 1, 2, 3, 4]
    assert price(book_list) == 8*5 * 0.75

def testSeveralDiscounts():
    book_list = [0, 0, 1]
    assert price(book_list) == 8 + (8 * 2 * 0.95)

    book_list = [0, 0, 1, 1]
    assert price(book_list) == 2 * (8 * 2 * 0.95)

    book_list = [0, 0, 1, 2, 2, 3]
    assert price(book_list) == (8 * 4 * 0.8) + (8 * 2 * 0.95)

    book_list = [0, 1, 1, 2, 3, 4]
    assert price(book_list) == 8 + (8 * 5 * 0.75)