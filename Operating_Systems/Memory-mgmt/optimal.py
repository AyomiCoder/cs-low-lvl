def optimal_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Find the page not used for the longest time in the future
                future_use = []
                for frame in memory:
                    if frame in pages[i+1:]:
                        future_use.append(pages[i+1:].index(frame))
                    else:
                        future_use.append(float('inf'))
                memory.pop(future_use.index(max(future_use)))
                memory.append(page)
            page_faults += 1
        print(f"Pages in Memory: {memory}")

    print(f"Total Page Faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0]
capacity = 3
optimal_page_replacement(pages, capacity)
