# Ramata Mini Library Management System

A Python-based library management system designed for women-focused literature with Sierra Leonean cultural context.

## 🌸 Features
- **📚 Book Management**: Add, search, update, and delete books with validation
- **👥 Member Management**: Register members with authentic Sierra Leonean names
- **📖 Borrowing System**: Track book loans with 3-book limit per member
- **🔄 Return System**: Process book returns and update availability
- **🔍 Search Functionality**: Find books by title or author
- **🎯 Women-Focused Collection**: Curated books appealing to women readers
- **🇸🇱 Cultural Context**: Sierra Leonean names and relevance

## 📚 Supported Genres
- 💕 Romance
- 📖 Contemporary Fiction  
- 💪 Self-Help
- 📝 Biography
- 🕵️ Mystery
- 📜 Historical Fiction
- 🌿 Health & Wellness

## 🛠️ Installation & Setup

### Requirements
- Python 3.6 or higher
- Windows, macOS, or Linux
- No external dependencies required

### Quick Start
```bash
# Interactive Mode (Recommended)
python operations.py

# Demo Mode (See system in action)
python demo.py

# Test Mode (Verify functionality)
python tests.py

```

# 📁 Project Structure
ramata-library-system/
├── operations.py          # Main library system implementation
├── demo.py               # Demonstration script with sample data
├── tests.py              # Comprehensive unit tests
├── README.md             # Project documentation
├── DesignRationale.pdf   # Design decisions and rationale
└── UML.png              # System architecture diagram

# 👥 Member Names
The system features authentic names:

* 👤 Fatmata Bangura 
* 👤 Kadie Kamara 
* 👤 Isatu Sesay 
* 👤 Mariama Koroma 
* 👤 Hawa Conteh 
* 👤 Aminata Turay 
* 👤 Kadiatu Jalloh 
* 👤 Sia Kabia 
* 👤 Yabom Sesay 
* 👤 Memuna Mansaray

# 📖 Sample Book Collection

**Title	Author	Genre	Copies**
* Big Magic	Elizabeth Gilbert	Self-Help	5 
* Where the Crawdads Sing	Delia Owens	Mystery	4 
* The Vanishing Half	Brit Bennett	Contemporary Fiction	3 
* The Midnight Library	Matt Haig	Contemporary Fiction	6 
* Untamed	Glennon Doyle	Self-Help	4 
* Becoming	Michelle Obama	Biography	5 
* The Four Winds	Kristin Hannah	Historical Fiction	3 
* Lessons in Chemistry	Bonnie Garmus	Contemporary Fiction	4 
* The Personal Librarian	Marie Benedict	Historical Fiction	3 
* The Christie Affair	Nina de Gramont	Mystery	4

# 🎯 Core Functions
Book Operations
python
# Add new book with validation
add_book(isbn, title, author, genre, copies)

# Search books by title or author
search_books(search_type, term)

# Update book details
update_book(isbn, field, value)

# Delete book (only if not borrowed)
delete_book(isbn)

# Get all books in collection
get_all_books()
Member Operations
python
# Register new member
add_member(name, email)

# Update member information
update_member(member_id, field, value)

# Remove member (only if no borrowed books)
delete_member(member_id)

# Display all registered members
get_all_members()
Borrowing Operations
python
# Loan books to members (max 3 per member)
borrow_book(member_id, isbn)

# Process book returns
return_book(member_id, isbn)

# View specific book information
get_book_details(isbn)

# View specific member information
get_member_details(member_id)

# 🏛️ System Architecture

## Data Structures
* 📚 **Books**: Dictionary with ISBN as key and book details as value 
* 👥 **Members**: List of dictionaries, each representing a member 
* 📋 **Genres**: Tuple of valid genre categories

## Design Principles
* **Modular Code**: Separate functions for each operation 
* **Input Validation**: Comprehensive error checking 
* **User-Friendly**: Clear messages and intuitive interface 
* **Cultural Relevance**: Sierra Leonean context throughout

## 📊 Testing Suite
The system includes 19 comprehensive tests covering:

### ✅ Book Management Tests
* Add book with valid data 
* Prevent duplicate ISBNs 
* Validate genre types 
* Reject negative copy numbers

### ✅ Member Management Tests
* Add member successfully 
* Prevent duplicate emails 
* Search functionality 
* Update operations

### ✅ Borrowing System Tests
* Successful book borrowing 
* Copy availability checks 
* 3-book limit enforcement 
* Return process validation

### ✅ Constraint Tests
* Delete prevention for borrowed books 
* Member deletion with active loans 
* Data integrity maintenance

**Run all tests:**

```bash
python tests.py

```
### 🎮 Interactive System Menu
When you run python operations.py, you'll see:

🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 

    🏛️  RAMATA MINI LIBRARY MANAGEMENT SYSTEM 🏛️ 


🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
* 📚 1. Add New Book 
* 👥 2. Add New Member 
* 🔍 3. Search Books 
* ✏️  4. Update Book Details 
* 👤 5. Update Member Details 
* 🗑️  6. Delete Book 
* 👋 7. Delete Member 
* 📖 8. Borrow Book 
* 📚 9. Return Book 
* 📖 10. Display All Books 
* 👥 11. Display All Members 
* 🚪 12. Exit System 

🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 

# 🔧 Error Handling & Messages
The system provides clear error messages for:

* ❌ Invalid input formats - Incorrect data types or formats 
* ⚠️ Borrowing limits exceeded - More than 3 books per member 
* 📚 Book availability issues - No copies available 
* 👤 Member validation errors - Invalid member IDs or emails 
* 🗑️ Delete constraints - Cannot delete borrowed books or members with loans

# 🌟 Demo Highlights
Running python demo.py demonstrates:

* 📚 Adding Books - Women-focused literature to the collection 
* 👥 Member Registration - Sierra Leonean members with unique IDs 
* 🔍 Search Operations - Find books by title and author 
* 📖 Borrowing Process - Loan books with limit enforcement 
* 🔄 Return System - Process returns and update availability 
* ✏️ Update Operations - Modify book and member information 
* 🗑️ Delete Constraints - Test prevention of invalid deletions 
* 📊 Status Display - Final library and member status

# 🆘 Troubleshooting
**Common Issues & Solutions**
* **"Command not found: python"**
*     Use python3 instead of python
*     Ensure Python is installed and in your PATH
* **Import errors**
*     Ensure all files are in the same directory
*     Check file names match exactly (operations.py, demo.py, tests.py)
* **Menu display issues**
*     Use a terminal that supports UTF-8 characters
*     Ensure terminal window is wide enough for proper formatting
* **Test failures**
*     Check Python version compatibility (3.6+ required)
*     Verify all required methods are implemented

### Getting Help
* Verify Python installation: python --version
* Check file permissions and locations 
* Ensure terminal supports emoji and special characters

### 🎉 Success Indicators
When the system works correctly, you'll see:

* ✅ Book 'Big Magic' added successfully to Ramata Library!
* ✅ Member 'Fatmata Bangura' added successfully with ID: RAM001 
* ✅ Book 'The Midnight Library' borrowed successfully!
* 🎉 RAMATA LIBRARY DEMO COMPLETED SUCCESSFULLY!

### 🤝 Contributing
This project demonstrates:

* Object-oriented programming principles 
* Data structure implementation 
* User interface design 
* Comprehensive testing strategies 
* Cultural context in software design

## 📄 License
Educational project - developed for learning Python programming concepts. Feel free to use and modify for educational purposes.
