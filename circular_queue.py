class CircularQueue:
    def __init__(self, max_size=5):
        self.queue = {} 
        self.max_size = max_size 
        self.current_index = 0 

    def enqueue(self, item):
        if len(self.queue) >= self.max_size:
            # Remove the first element (oldest)
            self.queue.pop(min(self.queue.keys()))

        # Add the new element 
        self.queue[self.current_index] = item
        
        # Update the current index
        self.current_index = (self.current_index + 1) % self.max_size

    def display(self):
        print("Queue:", self.queue)

# Test the Circular Queue
if __name__ == "__main__":
    cq = CircularQueue()

    cq.enqueue(1)
    cq.display()  # Should display{0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

    cq.enqueue(6)
    cq.display()  # Should displa {1: 2, 2: 3, 3: 4, 4: 5, 0: 6}

    cq.enqueue(7)
    cq.display()  # should display {2: 3, 3: 4, 4: 5, 0: 6, 1: 7}