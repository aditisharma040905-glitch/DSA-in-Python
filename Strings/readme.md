# Day 11 - Strings in DSA 

## Strings Concepts in Python

## String Basics
- **Definition** : A string is a sequence of characters.
- **Immutable**: Strings cannot be changed after the creation.
- **Indexing**: Characters can be accessed using indices.
Example: `s[0]` gives the first character.
- **Slicing**: Extract parts of a string.
Example: s[1:4] gives the substring from index 1 to 3.


---
## Common String Operations
- **Concatenation** → `"abc" + "def" = "abcdef"`
- **Repetition** → `"a" * 3 = "aaa"`
- **Membership Test** → `"a" in "abc"  → True`
- **Length of String** → `len("hello") = 5`
- **String Methods**:
  - `lower(), upper()` → Case conversion
  - `strip()` → Remove spaces
  - `split()` → Convert string to list
  - `join()` → Combine list into string
  - `replace("a", "b")` → Replace characters

---
## String Traversal
- **For loop**:
for ch in "hello":
    print(ch)

- **While loop**:
  i=0
  s="hello"
  while i<len(s):
      print(s[i])
      i+=1

---
## Time and space Complexity in string operations
- **Indexing & Slicing** → O(1) for indexing, O(k) for slicing (k = slice length)

- **Concatenation** → O(n) (creates new string)

- **Searching (in operator)** → O(n)

- **Comparison** → O(min(n, m)) (n, m = lengths of strings)

- **Built-in Functions** → Most run in linear time (O(n))

