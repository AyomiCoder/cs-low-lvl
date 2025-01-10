def is_safe(processes, max_resources, allocated, max_need, available):
    n = len(processes)  # Number of processes
    m = len(available)  # Number of resource types

    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                # Check if the process can be completed
                if all(max_need[i][j] - allocated[i][j] <= work[j] for j in range(m)):
                    safe_sequence.append(processes[i])
                    work = [work[j] + allocated[i][j] for j in range(m)]
                    finish[i] = True
                    found = True
        if not found:
            break

    if len(safe_sequence) == n:
        print("System is in a safe state. Safe sequence:", safe_sequence)
        return True
    else:
        print("System is not in a safe state.")
        return False

# Example usage
processes = ['P1', 'P2', 'P3']
max_resources = [10]  # Total resources
allocated = [[2], [1], [2]]  # Resources allocated to each process
max_need = [[5], [3], [4]]  # Maximum resources needed by each process
available = [5]  # Currently available resources

is_safe(processes, max_resources, allocated, max_need, available)
