from operations import RamataMiniLibraryManagementSystem


def run_demo():
    terminal_width = 70
    print("=" * terminal_width)
    print("🏛️  RAMATA MINI LIBRARY MANAGEMENT SYSTEM - DEMO 🏛️")
    print("=" * terminal_width)

    ramata_library = RamataMiniLibraryManagementSystem()

    # Demo 1: Add Books
    print("\n1. ADDING WOMEN-FOCUSED BOOKS")
    print("-" * terminal_width)

    books_to_add = [
        ("978-0735211292", "Big Magic", "Elizabeth Gilbert", "Self-Help", 5),
        ("978-0385543765", "Where the Crawdads Sing", "Delia Owens", "Mystery", 4),
        ("978-0525562023", "The Vanishing Half", "Brit Bennett", "Contemporary Fiction", 3),
        ("978-1984819873", "The Midnight Library", "Matt Haig", "Contemporary Fiction", 6),
        ("978-0062951626", "Untamed", "Glennon Doyle", "Self-Help", 4),
        ("978-1501160769", "Becoming", "Michelle Obama", "Biography", 5),
        ("978-0525562696", "The Four Winds", "Kristin Hannah", "Historical Fiction", 3),
        ("978-0593318480", "Lessons in Chemistry", "Bonnie Garmus", "Contemporary Fiction", 4),
        ("978-0593299598", "The Personal Librarian", "Marie Benedict", "Historical Fiction", 3),
        ("978-0593356147", "The Christie Affair", "Nina de Gramont", "Mystery", 4)
    ]

    for isbn, title, author, genre, copies in books_to_add:
        print(f"\n📖 Adding '{title}'...")
        ramata_library.add_book(isbn, title, author, genre, copies)

    # Demo 2: Add Members with Sierra Leonean Names
    print("\n2. ADDING MEMBERS")
    print("-" * terminal_width)

    members_to_add = [
        ("Fatmata Bangura", "fatmata.bangura@email.com"),
        ("Kadie Kamara", "kadie.kamara@email.com"),
        ("Isatu Sesay", "isatu.sesay@email.com"),
        ("Mariama Koroma", "mariama.koroma@email.com"),
        ("Hawa Conteh", "hawa.conteh@email.com"),
        ("Aminata Turay", "aminata.turay@email.com"),
        ("Kadiatu Jalloh", "kadiatu.jalloh@email.com"),
        ("Sia Kabia", "sia.kabia@email.com"),
        ("Yabom Sesay", "yabom.sesay@email.com"),
        ("Memuna Mansaray", "memuna.mansaray@email.com")
    ]

    for name, email in members_to_add:
        print(f"\n👤 Adding {name}...")
        ramata_library.add_member(name, email)

    # Demo 3: Display All Books and Members
    print("\n3. CURRENT RAMATA LIBRARY STATUS")
    print("-" * terminal_width)

    print("\n📚 All Books in Ramata Library:")
    ramata_books = ramata_library.get_all_books()
    for isbn, book in ramata_books.items():
        print(f"   {book['title']} - Available: {book['available_copies']}/{book['total_copies']}")

    print("\n👥 All Ramata Library Members:")
    ramata_members = ramata_library.get_all_members()
    for member in ramata_members:
        print(f"   {member['name']} (ID: {member['member_id']}) - Borrowed: {len(member['borrowed_books'])}")

    # Demo 4: Search Books
    print("\n4. SEARCHING BOOKS IN RAMATA LIBRARY")
    print("-" * terminal_width)

    # Search by title
    print("\n🔍 Searching for 'library' in titles...")
    success, results = ramata_library.search_books("title", "library")
    if success and results:
        for isbn, book in results:
            print(f"   Found: {book['title']} by {book['author']}")

    # Search by author
    print("\n🔍 Searching for 'Gilbert' in authors...")
    success, results = ramata_library.search_books("author", "Gilbert")
    if success and results:
        for isbn, book in results:
            print(f"   Found: {book['title']} by {book['author']}")

    # Demo 5: Borrow Books
    print("\n5. BORROWING BOOKS FROM RAMATA LIBRARY")
    print("-" * terminal_width)

    # Get member IDs
    ramata_members = ramata_library.get_all_members()
    fatmata_id = ramata_members[0]['member_id']
    kadie_id = ramata_members[1]['member_id']

    # Fatmata borrows books
    print(f"\n📖 Fatmata (ID: {fatmata_id}) borrowing books:")
    borrow_operations = [
        (fatmata_id, "978-0735211292"),  # Big Magic
        (fatmata_id, "978-0385543765"),  # Where the Crawdads Sing
        (fatmata_id, "978-0525562023"),  # The Vanishing Half
    ]

    for member_id, isbn in borrow_operations:
        book_title = ramata_library.get_book_details(isbn)['title']
        print(f"   Borrowing '{book_title}'...")
        ramata_library.borrow_book(member_id, isbn)

    # Try to borrow fourth book (should fail)
    print(f"\n⚠️ Trying to borrow fourth book...")
    ramata_library.borrow_book(fatmata_id, "978-1984819873")

    # Kadie borrows a book
    print(f"\n📖 Kadie (ID: {kadie_id}) borrowing a book:")
    book_title = ramata_library.get_book_details("978-0062951626")['title']
    print(f"   Borrowing '{book_title}'...")
    ramata_library.borrow_book(kadie_id, "978-0062951626")

    # Demo 6: Try to borrow unavailable book
    print("\n6. TESTING UNAVAILABLE BOOK SCENARIO")
    print("-" * terminal_width)

    # Try to borrow a book with no available copies
    print("\n❌ Trying to borrow 'Big Magic' when no copies available...")
    ramata_library.borrow_book(kadie_id, "978-0735211292")

    # Demo 7: Return Books
    print("\n7. RETURNING BOOKS TO RAMATA LIBRARY")
    print("-" * terminal_width)

    # Fatmata returns a book
    print(f"\n📚 Fatmata returning a book:")
    ramata_library.return_book(fatmata_id, "978-0735211292")

    # Now Kadie can borrow it
    print(f"\n📖 Kadie borrowing the returned book:")
    ramata_library.borrow_book(kadie_id, "978-0735211292")

    # Demo 8: Update Operations
    print("\n8. UPDATING RAMATA LIBRARY RECORDS")
    print("-" * terminal_width)

    # Update book
    print("\n✏️ Updating 'The Midnight Library' copies to 8...")
    ramata_library.update_book("978-1984819873", "total_copies", "8")

    # Update member
    isatu_id = ramata_members[2]['member_id']
    print(f"\n👤 Updating Isatu's email...")
    ramata_library.update_member(isatu_id, "email", "isatu.new@email.com")

    # Demo 9: Final Status
    print("\n9. FINAL RAMATA LIBRARY STATUS")
    print("-" * terminal_width)

    print("\n📚 All Books (Final):")
    ramata_books = ramata_library.get_all_books()
    for isbn, book in ramata_books.items():
        print(f"   {book['title']} - Available: {book['available_copies']}/{book['total_copies']}")

    print("\n👥 All Members (Final):")
    ramata_members = ramata_library.get_all_members()
    for member in ramata_members:
        borrowed_books = member['borrowed_books']
        book_titles = []
        for isbn in borrowed_books:
            book = ramata_library.get_book_details(isbn)
            if book:
                book_titles.append(book['title'])
        print(f"   {member['name']}: {len(borrowed_books)} books - {book_titles}")

    # Demo 10: Delete Operations (with constraints)
    print("\n10. DELETE OPERATIONS WITH CONSTRAINTS")
    print("-" * terminal_width)

    # Try to delete member with borrowed books (should fail)
    print(f"\n👋 Trying to delete Fatmata (has borrowed books)...")
    ramata_library.delete_member(fatmata_id)

    # Try to delete book with borrowed copies (should fail)
    print(f"\n🗑️ Trying to delete 'Where the Crawdads Sing' (borrowed copies)...")
    ramata_library.delete_book("978-0385543765")

    print("\n" + "=" * terminal_width)
    print("🎉 RAMATA LIBRARY DEMO COMPLETED SUCCESSFULLY!")
    print("=" * terminal_width)


if __name__ == "__main__":
    run_demo()