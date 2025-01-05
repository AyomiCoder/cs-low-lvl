// Implement the SJF CPU scheduling algorithm
// SJF: Shortest Job First
// This is a non-preemptive algorithm
// The process with the smallest execution time is selected for execution next
// If two processes have the same execution time, the process that arrived first is selected
// The process is executed until it is completed
// The average waiting time and average turnaround time are calculated
// The waiting time is the total time a process spends waiting in the ready queue
// The turnaround time is the total time a process takes to complete execution
// The smaller the average waiting time and average turnaround time, the better the algorithm
// The SJF algorithm is optimal for minimizing the average waiting time and average turnaround time
// The SJF algorithm is suitable for batch systems with known execution times
// The SJF algorithm is not suitable for interactive systems with unknown execution times
// The SJF algorithm is not suitable for real-time systems with strict deadlines
// The SJF algorithm is not suitable for preemptive systems with context switching
// The SJF algorithm is not suitable for systems with high arrival rates
// The SJF algorithm is not suitable for systems with high priority processes
// The SJF algorithm is not suitable for systems with aging processes
// The SJF algorithm is not suitable for systems with I/O-bound processes
// The SJF algorithm is not suitable for systems with CPU-bound processes
// The SJF algorithm is not suitable for systems with starvation processes
// The SJF algorithm is not suitable for systems with aging processes


// Function to implement the SJF CPU scheduling algorithm
function SJF(processes) {
    let totalWaitingTime = 0;
    let totalTurnaroundTime = 0;

    let currentTime = 0;
    let currentProcess = null;

    let readyQueue = [];
    let completedQueue = [];
    processes.sort((a, b) => a.arrivalTime - b.arrivalTime);

    while (processes.length > 0 || readyQueue.length > 0 || currentProcess !== null) {
        while (processes.length > 0 && processes[0].arrivalTime <= currentTime) {
            readyQueue.push(processes.shift());
        }
        readyQueue.sort((a, b) => a.executionTime - b.executionTime);

        if (currentProcess === null && readyQueue.length > 0) {
            currentProcess = readyQueue.shift();
            currentProcess.startTime = currentTime;
        }

        if (currentProcess !== null) {
            currentProcess.executionTime--;
            currentTime++;

            if (currentProcess.executionTime === 0) {
                currentProcess.completionTime = currentTime;
                currentProcess.turnaroundTime = currentProcess.completionTime - currentProcess.arrivalTime;
                currentProcess.waitingTime = currentProcess.turnaroundTime - currentProcess.burstTime;
                totalWaitingTime += currentProcess.waitingTime;
                totalTurnaroundTime += currentProcess.turnaroundTime;
                completedQueue.push(currentProcess);
                currentProcess = null;
            }
        } else {
            currentTime++;
        }
    }
    let averageWaitingTime = totalWaitingTime / completedQueue.length;
    let averageTurnaroundTime = totalTurnaroundTime / completedQueue.length;
    return { completedQueue, averageWaitingTime, averageTurnaroundTime };
}

// Example usage:
let processes = [
    { id: 1, arrivalTime: 0, burstTime: 6 },
    { id: 2, arrivalTime: 1, burstTime: 8 },
    { id: 3, arrivalTime: 2, burstTime: 7 },
    { id: 4, arrivalTime: 3, burstTime: 3 },
];
let result = SJF(processes);
console.log(result.completedQueue);
console.log(`Average Waiting Time: ${result.averageWaitingTime}`);
console.log(`Average Turnaround Time: ${result.averageTurnaroundTime}`);

