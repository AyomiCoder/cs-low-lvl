# Preemptive Shortest Job First (SRTF) Scheduling

def preemptive_sjf(processes):
    # Sort by Arrival Time, then Burst Time
    processes.sort(key=lambda x: x['arrival'])
    
    # Initialize variables
    time = 0
    completed = 0
    n = len(processes)
    ready_queue = []
    results = []

    # Add a "remaining_time" field to track remaining burst time
    for p in processes:
        p['remaining_time'] = p['burst']
    
    while completed < n:
        # Add processes that have arrived to the ready queue
        for p in processes:
            if p['arrival'] <= time and p not in ready_queue and p['remaining_time'] > 0:
                ready_queue.append(p)
        
        # Sort ready queue by remaining time
        ready_queue.sort(key=lambda x: x['remaining_time'])
        
        if ready_queue:
            # Pick the process with the shortest remaining time
            current_process = ready_queue[0]
            current_process['remaining_time'] -= 1
            time += 1
            
            # If the process is complete
            if current_process['remaining_time'] == 0:
                current_process['completion'] = time
                completed += 1
                ready_queue.remove(current_process)
        else:
            # If no process is ready, move time forward
            time += 1

    # Calculate Turnaround Time (TAT) and Waiting Time (WT)
    for p in processes:
        p['tat'] = p['completion'] - p['arrival']
        p['wt'] = p['tat'] - p['burst']
        results.append(p)

    return results


# Example Processes
processes = [
    {'name': 'P1', 'arrival': 0, 'burst': 7},
    {'name': 'P2', 'arrival': 2, 'burst': 4},
    {'name': 'P3', 'arrival': 4, 'burst': 1},
    {'name': 'P4', 'arrival': 5, 'burst': 4}
]

# Run SRTF
results = preemptive_sjf(processes)

# Print Results
print("Process | Arrival | Burst | Completion | Turnaround | Waiting")
for p in results:
    print(f"{p['name']:>7} | {p['arrival']:>7} | {p['burst']:>5} | {p['completion']:>10} | {p['tat']:>10} | {p['wt']:>7}")
