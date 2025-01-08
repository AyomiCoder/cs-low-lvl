class PagingSimulator:
    def __init__(self, total_frames):
        self.total_frames = total_frames
        self.frames = [-1] * total_frames  # Simulate empty frames

    def allocate_pages(self, process_id, pages):
        print(f"\nAllocating pages for Process {process_id}...")
        allocated = 0

        for i in range(len(self.frames)):
            if self.frames[i] == -1 and allocated < pages:
                self.frames[i] = process_id
                allocated += 1

        if allocated < pages:
            print(f"Not enough frames! Only {allocated}/{pages} pages allocated.")
        else:
            print(f"All {pages} pages allocated.")

        self.display_memory()

    def deallocate_pages(self, process_id):
        print(f"\nDeallocating pages for Process {process_id}...")
        for i in range(len(self.frames)):
            if self.frames[i] == process_id:
                self.frames[i] = -1

        self.display_memory()

    def display_memory(self):
        print("Memory Frames:")
        for i, frame in enumerate(self.frames):
            print(f"Frame {i}: {'Empty' if frame == -1 else f'Process {frame}'}")


# Example Usage
simulator = PagingSimulator(total_frames=5)
simulator.allocate_pages(process_id=1, pages=3)
simulator.allocate_pages(process_id=2, pages=2)
simulator.deallocate_pages(process_id=1)
simulator.allocate_pages(process_id=3, pages=4)
