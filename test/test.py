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