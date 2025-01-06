# implement non-preemptive priority scheduling
# non-preemptive priority scheduling is a scheduling algorithm where the process with the highest priority is selected for execution. If two processes have the same priority, the process that arrived first is selected. The algorithm is non-preemptive, meaning that once a process is selected, it runs to completion without interruption.


def non_preemptive_priority_scheduling(processes):
    # Sort by Arrival Time, then Priority
    processes.sort(key=lambda x: (x['arrival'], x['priority']))
    
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
        
        # Sort ready queue by priority
        ready_queue.sort(key=lambda x: x['priority'], reverse=True)
        
        if ready_queue:
            # Pick the process with the highest priority
            current_process = ready_queue[0]
            time += current_process['remaining_time']
            current_process['completion'] = time
            current_process['remaining_time'] = 0
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
    {'name': 'P1', 'arrival': 0, 'burst': 7, 'priority': 3},
    {'name': 'P2', 'arrival': 2, 'burst': 4, 'priority': 1},
    {'name': 'P3', 'arrival': 4, 'burst': 1, 'priority': 4},
    {'name': 'P4', 'arrival': 5, 'burst': 4, 'priority': 2}
]

# Run Non-Preemptive Priority Scheduling
results = non_preemptive_priority_scheduling(processes)

# Print Results
print("Process | Arrival | Burst | Priority | Completion | Turnaround | Waiting")
for p in results:
    print(f"{p['name']:>7} | {p['arrival']:>7} | {p['burst']:>5} | {p['priority']:>8} | {p['completion']:>10} | {p['tat']:>10} | {p['wt']:>7}")


# pre-emptive priority scheduling
# pre-emptive priority scheduling is a scheduling algorithm where the process with the highest priority is selected for execution. If two processes have the same priority, the process that arrived first is selected. The algorithm is pre-emptive, meaning that a process can be interrupted and replaced by a higher priority process.

def preemptive_priority_scheduling(processes):
    # Sort by Arrival Time, then Priority
    processes.sort(key=lambda x: (x['arrival'], x['priority']))
    
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
        
        # Sort ready queue by priority
        ready_queue.sort(key=lambda x: x['priority'], reverse=True)
        
        if ready_queue:
            # Pick the process with the highest priority
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
    {'name': 'P1', 'arrival': 0, 'burst': 7, 'priority': 3},
    {'name': 'P2', 'arrival': 2, 'burst': 4, 'priority': 1},
    {'name': 'P3', 'arrival': 4, 'burst': 1, 'priority': 4},
    {'name': 'P4', 'arrival': 5, 'burst': 4, 'priority': 2}
]

# Run Preemptive Priority Scheduling
results = preemptive_priority_scheduling(processes)

# Print Results
print("Process | Arrival | Burst | Priority | Completion | Turnaround | Waiting")
for p in results:
    print(f"{p['name']:>7} | {p['arrival']:>7} | {p['burst']:>5} | {p['priority']:>8} | {p['completion']:>10} | {p['tat']:>10} | {p['wt']:>7}")

# Output: