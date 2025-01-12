def is_safe(processes, available, max_need, allocation):
    n = len(processes)
    m = len(available)
    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(max_need[i][j] - allocation[i][j] <= work[j] for j in range(m)):
                    safe_sequence.append(processes[i])
                    work = [work[j] + allocation[i][j] for j in range(m)]
                    finish[i] = True
                    found = True
        if not found:
            break

    if len(safe_sequence) == n:
        return True, safe_sequence
    else:
        return False, []

# Example
processes = ['P1', 'P2', 'P3', 'P4']
available = [3, 3, 2]
max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [4, 2, 2]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1]]

is_safe, sequence = is_safe(processes, available, max_need, allocation)
if is_safe:
    print("Safe sequence:", sequence)
else:
    print("No safe sequence. System is in a deadlock.")
