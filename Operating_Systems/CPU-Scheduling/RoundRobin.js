// implement a round robin scheduling algorithm
// The round-robin scheduling algorithm is designed especially for time-sharing systems. It is similar to the first-come, first-served scheduling algorithm, but preemption is added to switch between processes. A small unit of time, called a time quantum or time slice, is defined. A time quantum is generally from 10 to 100 milliseconds. The ready queue is treated as a circular queue. The CPU scheduler goes around the ready queue, allocating the CPU to each process for a time interval of up to one time quantum. To implement the round-robin scheduling algorithm, we will use a queue data structure.

class Queue {
    constructor() {
        this.items = [];
    }
    
    enqueue(element) {
        this.items.push(element);
    }
    
    dequeue() {
        if (this.isEmpty()) return "Underflow";
        return this.items.shift();
    }
    
    front() {
        if (this.isEmpty()) return "No elements in Queue";
        return this.items[0];
    }
    
    isEmpty() {
        return this.items.length === 0;
    }
    
    printQueue() {
        let str = "";
        for (let i = 0; i < this.items.length; i++) str += this.items[i] + " ";
        return str;
    }
    }

    class RoundRobin {
    constructor() {
        this.queue = new Queue();
    }

    findWaitingTime(processes, n, bt, wt, quantum) {
        let rem_bt = [];
        for (let i = 0; i < n; i++) rem_bt[i] = bt[i];
        let t = 0;
        while (true) {
            let done = true;
            for (let i = 0; i < n; i++) {
                if (rem_bt[i] > 0) {
                    done = false;
                    if (rem_bt[i] > quantum) {
                        t += quantum;
                        rem_bt[i] -= quantum;
                    } else {
                        t = t + rem_bt[i];
                        wt[i] = t - bt[i];
                        rem_bt[i] = 0;
                    }
                }
            }
            if (done === true) break;
        }
    }

    findTurnAroundTime(processes, n, bt, wt, tat) {
        for (let i = 0; i < n; i++) tat[i] = bt[i] + wt[i];
    }

    findavgTime(processes, n, bt, quantum) {
        let wt = [],
            tat = [];
        this.findWaitingTime(processes, n, bt, wt, quantum);
        this.findTurnAroundTime(processes, n, bt, wt, tat);
        let total_wt = 0,
            total_tat = 0;
        for (let i = 0; i < n; i++) {
            total_wt += wt[i];
            total_tat += tat[i];
        }
        return {
            avg_wt: total_wt / n,
            avg_tat: total_tat / n,
        };
    }

    }

    // Implementation
    const processes = [1, 2, 3];
    const n = processes.length;
    const burst_time = [10, 5, 8];
    const quantum = 2;
    const roundRobin = new RoundRobin();
    const result = roundRobin.findavgTime(processes, n, burst_time, quantum);
    console.log(`Average Waiting Time: ${result.avg_wt}`);
    console.log(`Average Turnaround Time: ${result.avg_tat}`);
