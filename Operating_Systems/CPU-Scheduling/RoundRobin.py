# implement a round robin scheduling algorithm

from collections import deque

class Process:
    def __init__(self, name, arrival, burst):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.remaining_time = burst
        self.completion = 0
        self.tat = 0
        self.wt = 0

def round_robin(processes, quantum):
    # Sort by Arrival Time
    processes.sort(key=lambda x: x.arrival)
    
    # Initialize variables
    time = 0
    n = len(processes)
    ready_queue = deque()
    results = []
    
    while True:
        # Add processes that have arrived to the ready queue
        for p in processes:
            if p.arrival <= time and p.remaining_time > 0:
                ready_queue.append(p)
        
        # If ready queue is empty, break
        if not ready_queue:
            break
        
        # Process the first process in the ready queue
        current_process = ready_queue.popleft()
        if current_process.remaining_time > quantum:
            time += quantum
            current_process.remaining_time -= quantum
            ready_queue.append(current_process)
        else:
            time += current_process.remaining_time
            current_process.remaining_time = 0
            current_process.completion = time
            current_process.tat = current_process.completion - current_process.arrival
            current_process.wt = current_process.tat - current_process.burst
            results.append(current_process)
    
    return results

# Example Processes
processes = [
    Process('P1', 0, 10),
    Process('P2', 1, 4),
    Process('P3', 2, 5),
    Process('P4', 3, 3)
]

quantum = 2

results = round_robin(processes, quantum)

print("Process | Arrival | Burst | Completion | Turnaround | Waiting")
for p in results:
    print(f"{p.name:>7} | {p.arrival:>7} | {p.burst:>5} | {p.completion:>10} | {p.tat:>10} | {p.wt:>7}")

    
