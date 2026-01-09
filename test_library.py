import pytest
from library import Library

def test_add_book():
    lib = Library()
    assert lib.add_book("Python 101") == "Book added"
    assert lib.add_book("Python 101") == "Book already exists"

def test_remove_book():
    lib = Library()
    lib.add_book("Data Science")
    assert lib.remove_book("Data Science") == "Book removed"
    assert lib.remove_book("Data Science") == "Book not found"

def test_list_books():
    lib = Library()
    lib.add_book("AI Basics")
    assert "AI Basics" in lib.list_books()
