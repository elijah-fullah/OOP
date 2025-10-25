from operations import RamataMiniLibraryManagementSystem


class TestRamataMiniLibraryManagementSystem:

    def setup_method(self):
        """Set up a fresh Ramata library system for each test"""
        self.ramata_library = RamataMiniLibraryManagementSystem()

        # Add some test data
        self.ramata_library.add_book("RAM-001", "Test Book 1", "Author One", "Self-Help", 3)
        self.ramata_library.add_book("RAM-002", "Test Book 2", "Author Two", "Romance", 1)
        self.ramata_library.add_member("Fatmata Bangura", "fatmata@email.com")

        # Get the auto-generated member ID
        self.ramata_member_id = self.ramata_library.get_all_members()[0]['member_id']

    def test_add_book_success(self):
        """Test adding a book successfully to Ramata Library"""
        success = self.ramata_library.add_book("RAM-003", "New Book", "New Author", "Mystery", 5)
        assert success == True
        assert "RAM-003" in self.ramata_library.get_all_books()

    def test_add_book_duplicate_isbn(self):
        """Test adding a book with duplicate ISBN to Ramata Library"""
        success = self.ramata_library.add_book("RAM-001", "Duplicate Book", "Some Author", "Self-Help", 2)
        assert success == False

    def test_add_book_invalid_genre(self):
        """Test adding a book with invalid genre to Ramata Library"""
        success = self.ramata_library.add_book("RAM-004", "Invalid Genre Book", "Author", "InvalidGenre", 2)
        assert success == False

    def test_add_book_negative_copies(self):
        """Test adding a book with negative copies to Ramata Library"""
        success = self.ramata_library.add_book("RAM-005", "Negative Copies", "Author", "Self-Help", -1)
        assert success == False

    def test_add_member_success(self):
        """Test adding a member successfully to Ramata Library"""
        success = self.ramata_library.add_member("Kadie Kamara", "kadie@email.com")
        assert success == True
        assert len(self.ramata_library.get_all_members()) == 2

    def test_add_member_duplicate_email(self):
        """Test adding a member with duplicate email to Ramata Library"""
        success = self.ramata_library.add_member("Different Name", "fatmata@email.com")
        assert success == False

    def test_search_books_by_title(self):
        """Test searching books by title in Ramata Library"""
        success, results = self.ramata_library.search_books("title", "Test Book")
        assert success == True
        assert len(results) == 2

    def test_search_books_by_author(self):
        """Test searching books by author in Ramata Library"""
        success, results = self.ramata_library.search_books("author", "Author One")
        assert success == True
        assert len(results) == 1
        assert results[0][1]['title'] == "Test Book 1"

    def test_borrow_book_success(self):
        """Test borrowing a book successfully from Ramata Library"""
        success = self.ramata_library.borrow_book(self.ramata_member_id, "RAM-001")
        assert success == True

        # Check that available copies decreased
        book = self.ramata_library.get_book_details("RAM-001")
        assert book['available_copies'] == 2

        # Check that member has the book
        member = self.ramata_library.get_member_details(self.ramata_member_id)
        assert "RAM-001" in member['borrowed_books']

    def test_borrow_book_no_copies_left(self):
        """Test borrowing when no copies are available in Ramata Library"""
        # First, borrow the only copy
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-002")

        # Add another member to try borrowing the same book
        self.ramata_library.add_member("Isatu Sesay", "isatu@email.com")
        second_member_id = self.ramata_library.get_all_members()[1]['member_id']

        success = self.ramata_library.borrow_book(second_member_id, "RAM-002")
        assert success == False

    def test_borrow_book_max_limit(self):
        """Test borrowing beyond maximum limit (3 books) in Ramata Library"""
        # Add more books
        self.ramata_library.add_book("RAM-003", "Book 3", "Author", "Self-Help", 1)
        self.ramata_library.add_book("RAM-004", "Book 4", "Author", "Romance", 1)
        self.ramata_library.add_book("RAM-005", "Book 5", "Author", "Mystery", 1)

        # Borrow 3 books successfully
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-001")
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-003")
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-004")

        # Try to borrow fourth book
        success = self.ramata_library.borrow_book(self.ramata_member_id, "RAM-005")
        assert success == False

    def test_return_book_success(self):
        """Test returning a book successfully to Ramata Library"""
        # First borrow a book
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-001")

        # Then return it
        success = self.ramata_library.return_book(self.ramata_member_id, "RAM-001")
        assert success == True

        # Check that available copies increased
        book = self.ramata_library.get_book_details("RAM-001")
        assert book['available_copies'] == 3

        # Check that member no longer has the book
        member = self.ramata_library.get_member_details(self.ramata_member_id)
        assert "RAM-001" not in member['borrowed_books']

    def test_return_book_not_borrowed(self):
        """Test returning a book that wasn't borrowed from Ramata Library"""
        success = self.ramata_library.return_book(self.ramata_member_id, "RAM-001")
        assert success == False

    def test_update_book_success(self):
        """Test updating book details successfully in Ramata Library"""
        success = self.ramata_library.update_book("RAM-001", "title", "Updated Title")
        assert success == True

        book = self.ramata_library.get_book_details("RAM-001")
        assert book['title'] == "Updated Title"

    def test_update_book_copies(self):
        """Test updating book copies in Ramata Library"""
        # First borrow a copy to test available copies adjustment
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-001")

        success = self.ramata_library.update_book("RAM-001", "total_copies", "5")
        assert success == True

        book = self.ramata_library.get_book_details("RAM-001")
        assert book['total_copies'] == 5
        assert book['available_copies'] == 4  # 5 total - 1 borrowed

    def test_delete_book_success(self):
        """Test deleting a book successfully from Ramata Library"""
        success = self.ramata_library.delete_book("RAM-002")
        assert success == True
        assert "RAM-002" not in self.ramata_library.get_all_books()

    def test_delete_book_with_borrowed_copies(self):
        """Test deleting a book with borrowed copies from Ramata Library"""
        # First borrow the book
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-001")

        # Try to delete it
        success = self.ramata_library.delete_book("RAM-001")
        assert success == False

    def test_delete_member_success(self):
        """Test deleting a member successfully from Ramata Library"""
        success = self.ramata_library.delete_member(self.ramata_member_id)
        assert success == True
        assert len(self.ramata_library.get_all_members()) == 0

    def test_delete_member_with_borrowed_books(self):
        """Test deleting a member with borrowed books from Ramata Library"""
        # First borrow a book
        self.ramata_library.borrow_book(self.ramata_member_id, "RAM-001")

        # Try to delete the member
        success = self.ramata_library.delete_member(self.ramata_member_id)
        assert success == False


def run_tests():
    """Run all tests and display results for Ramata Library"""
    terminal_width = 60
    print("🌸" * terminal_width)
    print("🧪 RUNNING RAMATA LIBRARY SYSTEM TESTS 🧪")
    print("🌸" * terminal_width)

    test_class = TestRamataMiniLibraryManagementSystem()

    # List of test methods to run
    test_methods = [
        test_class.test_add_book_success,
        test_class.test_add_book_duplicate_isbn,
        test_class.test_add_book_invalid_genre,
        test_class.test_add_book_negative_copies,
        test_class.test_add_member_success,
        test_class.test_add_member_duplicate_email,
        test_class.test_search_books_by_title,
        test_class.test_search_books_by_author,
        test_class.test_borrow_book_success,
        test_class.test_borrow_book_no_copies_left,
        test_class.test_borrow_book_max_limit,
        test_class.test_return_book_success,
        test_class.test_return_book_not_borrowed,
        test_class.test_update_book_success,
        test_class.test_update_book_copies,
        test_class.test_delete_book_success,
        test_class.test_delete_book_with_borrowed_copies,
        test_class.test_delete_member_success,
        test_class.test_delete_member_with_borrowed_books,
    ]

    passed = 0
    failed = 0

    for test_method in test_methods:
        try:
            # Reset for each test
            test_class.setup_method()
            test_method()
            print(f"✅ {test_method.__name__}: PASSED")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_method.__name__}: FAILED - {e}")
            failed += 1
        except Exception as e:
            print(f"💥 {test_method.__name__}: ERROR - {e}")
            failed += 1

    print("🌸" * terminal_width)
    print(f"📊 RESULTS: {passed} passed, {failed} failed, {len(test_methods)} total")

    if failed == 0:
        print("🎉 ALL RAMATA LIBRARY TESTS PASSED!")
    else:
        print(f"⚠️  {failed} RAMATA LIBRARY TESTS FAILED!")

    print("🌸" * terminal_width)


if __name__ == "__main__":
    run_tests()