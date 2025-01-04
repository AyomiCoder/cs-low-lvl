// Implement a FCFS algorithm in JavaScript

// function to find the arrival time of each process
function findArrivalTime(processes, n, bt, at) {
    at[0] = 0;
    for (let i = 1; i < n; i++) {
        at[i] = at[i - 1] + bt[i - 1];
    }
}

// Function to find the waiting time for all processes
function findWaitingTime(processes, n, bt, wt, at) {
    let service_time = new Array(n);
    service_time[0] = at[0];
    wt[0] = 0;

    // calculating waiting time
    for (let i = 1; i < n; i++) {
        service_time[i] = service_time[i - 1] + bt[i - 1];
        wt[i] = service_time[i] - at[i];
        if (wt[i] < 0) {
            wt[i] = 0;
        }
    }
}

// Function to calculate turn around time
function findTurnAroundTime(processes, n, bt, wt, tat) {
    // calculating turnaround time by adding bt[i] + wt[i]
    for (let i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
    }
}

// console.log function to print the output
function printData(processes, n, bt, wt, tat) {
    let total_wt = 0;
    let total_tat = 0;
    for (let i = 0; i < n; i++) {
        total_wt = total_wt + wt[i];
        total_tat = total_tat + tat[i];
        console.log(" " + processes[i] + "\t\t" + bt[i] + "\t " + wt[i] + "\t\t " + tat[i]);
    }
    console.log("Average waiting time = " + total_wt / n);
    console.log("Average turn around time = " + total_tat / n);
}

// Function to implement FCFS scheduling
function findFCFS(processes, n, bt) {
    let wt = new Array(n);
    let tat = new Array(n);
    let at = new Array(n);

    findArrivalTime(processes, n, bt, at);
    findWaitingTime(processes, n, bt, wt, at);
    findTurnAroundTime(processes, n, bt, wt, tat);
    console.log("Processes\tBurst Time\tWaiting Time\tTurn Around Time");
    printData(processes, n, bt, wt, tat);
}

// Driver code
let processes = [1, 2, 3];
let n = processes.length;
let burst_time = [10, 5, 8];
findFCFS(processes, n, burst_time);
