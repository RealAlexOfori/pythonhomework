class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        return len(self.queue)
    
    def add_to_queue(self, person_in_queue):
        self.queue.append(person_in_queue)

    def clear_queue(self):
        self.queue.clear()
        return len(self.queue)
