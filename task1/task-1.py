#Task 1
books = []
members = []

def add_book(book_id, title, author, status):
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })

def add_member(member_id, name):
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []
    })

#Task 1A
add_book(2024001, "Python Programming", "Jacob Zuma", "available")
add_member(1, "Anelisa Maleka")

#Task 1B
print("Books List:")
print(books)
print("\nMembers List:")
print(members)

books = []
members = []

#Task 1C
books.append({
    "book_id": 2024001,
    "title": "Python Programming",
    "author": "Jacob Zuma",
    "status": "available"
})

members.append({
    "member_id": 1,
    "name": "Anelisa Maleka",
    "borrowed_books": []
})

print("Books List:")
print(books)
print("\nMembers List:")
print(members)

#Task 1D
import pandas as pd

books_df = pd.DataFrame(columns=["book_id", "title", "author", "status"])
members_df = pd.DataFrame(columns=["member_id", "name", "borrowed_books"])

books_df = pd.concat([books_df, pd.DataFrame({
    "book_id": [2024001],
    "title": ["Python Programming"],
    "author": ["Jacob Zuma"],
    "status": ["available"]
})], ignore_index=True)

members_df = pd.concat([members_df, pd.DataFrame({
    "member_id": [1],
    "name": ["Anelisa Maleka"],
    "borrowed_books": [[]]
})], ignore_index=True)

print("Books DataFrame:")
print(books_df)
print("\nMembers DataFrame:")
print(members_df)