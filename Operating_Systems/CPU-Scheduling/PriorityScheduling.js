// implement non-preemptive priority scheduling algorithm
// The non-preemptive priority scheduling algorithm is designed to select the process with the highest priority for execution. The process with the highest priority is selected from the ready queue and allocated the CPU. The priority of a process is generally an integer value. The process with the lowest priority number is given the highest priority. The priority scheduling algorithm can be preemptive or non-preemptive. In the non-preemptive priority scheduling algorithm, once a process is allocated the CPU, it will continue to


class PriorityQueue {
    constructor() {
        this.items = [];
    }

    enqueue(element, priority) {
        let qElement = { element, priority };
        let contain = false;

        for (let i = 0; i < this.items.length; i++) {
            if (this.items[i].priority > qElement.priority) {
                this.items.splice(i, 0, qElement);
                contain = true;
                break;
            }
        }

        if (!contain) this.items.push(qElement);
    }

    dequeue() {
        if (this.isEmpty()) return "Underflow";
        return this.items.shift();
    }

    front() {
        if (this.isEmpty()) return "No elements in Queue";
        return this.items[0];
    }

    rear() {
        if (this.isEmpty()) return "No elements in Queue";
        return this.items[this.items.length - 1];
    }

    isEmpty() {
        return this.items.length === 0;
    }

    printPQueue() {
        let str = "";
        for (let i = 0; i < this.items.length; i++) str += this.items[i].element + " ";
        return str;
    }
}

class PriorityScheduling {
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
            for (let j = 0; j < n; j++) {
                if (processes[j] <= t && rt[j] < minm && rt[j] > 0) {
                    minm = rt[j];
                    shortest = j;
                    found = true;
                }
            }

            if (!found) {
                t++;
                continue;
            }

            rt[shortest]--;
            minm = rt[shortest];
            if (minm === 0) minm = Number.MAX_VALUE;

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
const ps = new PriorityScheduling();
const wt = [];
const tat = [];
ps.findWaitingTime(processes, n, burst_time, wt, priority);
ps.findTurnAroundTime(processes, n, burst_time, wt, tat);
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

