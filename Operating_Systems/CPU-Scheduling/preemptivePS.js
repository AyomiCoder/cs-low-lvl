// preemtive priority scheduling
// The preemptive priority scheduling algorithm is designed to select the process with the highest priority for execution. The process with the highest priority is selected from the ready queue and allocated the CPU. The priority of a process is generally an integer value. The process with the lowest priority number is given the highest priority. The priority scheduling algorithm can be preemptive or non-preemptive. In the preemptive priority scheduling algorithm, the process with the highest priority can be preempted by a process with a higher priority. The preemptive priority scheduling algorithm is implemented using a priority queue. The process with the highest priority is selected from the priority queue and allocated the CPU. If a process with a higher priority arrives, it preempts the currently executing process and is allocated the CPU. The preemptive priority scheduling algorithm is used in real-time systems where the priority of a process can change dynamically.

class PreemptivePriorityScheduling {
    constructor() {
        this.queue = new PriorityQueue();
    }

    findWaitingTime(processes, n, bt, wt, priority) {
        let rt = [];
        for (let i = 0; i < n; i++) rt[i] = bt[i];
        let complete = 0;
        let t = 0;
        let minm = Number.MAX_VALUE;
        let shortest = 0;
        let finish_time;
        let found = false;
        let check = false;

        while (complete !== n) {
            let min_priority = Number.MAX_VALUE;

            for (let j = 0; j < n; j++) {
                if (processes[j] <= t && priority[j] < min_priority && rt[j] > 0) {
                    min_priority = priority[j];
                    shortest = j;
                    found = true;
                }
            }

            if (!found) {
                t++;
                continue;
            }

            rt[shortest]--;
            min_priority = priority[shortest];
            if (rt[shortest] === 0) {
                complete++;
                found = false;
                finish_time = t + 1;
                wt[shortest] = finish_time - bt[shortest] - processes[shortest];
                if (wt[shortest] < 0) wt[shortest] = 0;
            }

            t++;
        }
    }

    findTurnAroundTime(processes, n, bt, wt, tat) {
        for (let i = 0; i < n; i++) tat[i] = bt[i] + wt[i];
    }
}   

// Implementation
const processes = [1, 2, 3];
const n = processes.length;
const burst_time = [6, 8, 7];
const priority = [2, 1, 3];
const pps = new PreemptivePriorityScheduling();
const wt = [];
const tat = [];
pps.findWaitingTime(processes, n, burst_time, wt, priority);
pps.findTurnAroundTime(processes, n, burst_time, wt, tat);
let total_wt = 0,
    total_tat = 0;
for (let i = 0; i < n; i++) {
    total_wt += wt[i];
    total_tat += tat[i];
}
const avg_wt = total_wt / n;
const avg_tat = total_tat / n;
console.log(`Average waiting time: ${avg_wt}`);
console.log(`Average turnaround time: ${avg_tat}`);
