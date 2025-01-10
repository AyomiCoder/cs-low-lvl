def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru = memory.pop(0)  # Remove least recently used
                memory.append(page)
            page_faults += 1
        else:
            # Move the accessed page to the most recent position
            memory.remove(page)
            memory.append(page)
        print(f"Pages in Memory: {memory}")

    print(f"Total Page Faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0]
capacity = 3
lru_page_replacement(pages, capacity)
