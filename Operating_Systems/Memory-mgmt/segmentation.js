// implement segmentation in javascript

// Segmentation is a memory management technique in which, the memory is divided into the variable size parts. Each part is known as a segment which can be allocated to a process. Segmentation is a non-contiguous memory allocation technique. It is similar to paging but has different size parts.

// The main advantage of segmentation is that it supports dynamic data structures like stacks, queues, arrays, etc. It is also easier to implement than paging. The main disadvantage of segmentation is that it leads to external fragmentation.


class Segmentation {
    constructor() {
        this.segment = [];
        this.base = [];
        this.limit = [];
    }

    allocateMemory(segment, base, limit) {
        this.segment.push(segment);
        this.base.push(base);
        this.limit.push(limit);
    }

    getPhysicalAddress(segment, offset) {
        if (offset > this.limit[segment]) {
            return -1;
        }
        return this.base[segment] + offset;
    }
}

// Implementation
const segmentation = new Segmentation();
segmentation.allocateMemory(0, 100, 200);
segmentation.allocateMemory(1, 300, 400);
segmentation.allocateMemory(2, 500, 600);
console.log(segmentation.getPhysicalAddress(0, 150)); // 250
console.log(segmentation.getPhysicalAddress(1, 350)); // 650
console.log(segmentation.getPhysicalAddress(2, 550)); // 1050
console.log(segmentation.getPhysicalAddress(0, 250)); // -1
console.log(segmentation.getPhysicalAddress(1, 450)); // -1
