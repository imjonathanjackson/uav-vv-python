# Day 1

## Completed

- Read Fluent Python Chapter 1
- Read Chapter 2 through pattern recognition
- Read approximately half of Python Tutorial
- Built initial inventory.py
- Implemented add, view, search, remove, and close functions
- Created menu/control flow
- Completed 2 LeetCode problems
- Created LeetCode Premium account

## Things I learned

- Functions
- Function arguments
- Lists
- append()
- remove()
- membership testing
- loops
- input()
- match/case
- basic control flow

## Problems I encountered

- Connecting menu input to functions
- Function arguments
- input() behavior
- Removing items from a list
- Program control flow

## Things I don't fully understand yet

How to integrate a SQL database or FASTAPI into this project

## Day 2

- Continue Fluent Python Chapter 2
- Begin dictionaries/sets
- Continue inventory development
- LeetCode

# Learning Log

## Day 2 — Python Data Structures & Inventory Development

### Fluent Python

- Finished Chapter 2 of *Fluent Python*.
- Continued learning Python's core sequence types and data model.
- Studied:
  - Lists
  - Tuples
  - Strings
  - Slicing
  - List comprehensions
  - Generator expressions
  - Tuples and unpacking
  - Pattern matching
  - Mutable vs. immutable objects
  - References and object identity

### Important Python Concepts I Learned

- Python strings are immutable.
- Methods such as `.strip()` and `.lower()` return a new string rather than modifying the original string.
- Therefore:
  
  `item = item.strip().lower()`
  
  is different from:
  
  `item.strip().lower()`

- `input()` returns a string.
- `match/case` therefore needs to account for the type of the value returned by `input()`.
- Lists can contain duplicate values.
- List methods such as `.append()` and `.remove()` can modify a list.

### Inventory Project

Continued developing `inventory.py`.

Current functionality:

- Add equipment
- View inventory
- Search inventory
- Remove equipment
- Exit application
- Validate empty input
- Normalize equipment names using `.strip().lower()`
- Allow duplicate equipment

Current inventory requirement:

- Multiple pieces of the same equipment type should be allowed.
- Each individual piece of equipment will eventually receive a unique ID.

Example future inventory:

    ID      Equipment
    001     GPS
    002     GPS
    003     Radio
    004     GPS

I have not implemented unique IDs yet.

### V&V Thinking

Started documenting requirements and test cases separately from the implementation.

Important requirement:

- Duplicate equipment should be allowed because multiple physical pieces of the same equipment may exist.

Future requirement:

- Each individual equipment item should have a unique identifier.

Potential test cases include:

- Add a normal item.
- Add duplicate equipment.
- Search for an existing item.
- Search for an item that does not exist.
- Remove an existing item.
- Attempt to remove an item that does not exist.
- Enter empty or whitespace-only input.
- Enter an invalid menu option.

### LeetCode

- Solved Valid Anagram independently.
- Unable to solve Group Anagrams independently.
- Began identifying the difference between checking whether two strings are anagrams and grouping multiple strings by a common key.
- Need additional practice with dictionaries/hash-map based grouping.

### Code Review / Refactoring

Reviewed the inventory code but did not make major refactoring changes.

I recognized that I don't yet have enough Python knowledge to identify all of the best refactoring opportunities.

Questions I need to investigate:

- Global variables vs. passing data into functions.
- How the inventory data structure should change when unique IDs are added.
- How equipment should be represented when additional attributes are needed.

### Git / GitHub

- Created GitHub repository.
- Pushed the inventory project to GitHub.
- Learned how Git authentication works.
- Encountered and resolved a non-fast-forward push.
- Learned about pulling remote changes and merging unrelated histories.
- Configured VS Code as the Git commit-message editor.

### Day 2 Assessment

Day 2 was lighter than originally planned.

Completed:
- Fluent Python Chapter 2
- Inventory development
- Code review
- Git/GitHub work

Not completed:
- Full planned LeetCode workload
- Major refactoring
- All planned project development

### Lessons From Today

The biggest lesson today was that I don't need to immediately know how to improve my code.

I need to continue learning Python and use that new knowledge to recognize better designs.

I also started thinking about the difference between simply making software work and defining requirements and verifying that the software satisfies them.

### Day 3 Priorities

- Begin the next assigned Fluent Python material.
- Continue building the inventory system without adding unnecessary complexity.
- Revisit Group Anagrams.
- Complete the planned LeetCode problems.
- Begin identifying meaningful refactoring opportunities based on what I have learned.
- Continue Git commits after meaningful changes.