# Task_3  TV controller

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0                          # початковий індекс 0

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_index = n - 1
            return self.channels[self.current_index]
        else:
            return "No such channel"

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, query):
        if isinstance(query, int):
            return "Yes" if 1 <= query <= len(self.channels) else "No"
        elif isinstance(query, str):
            return "Yes" if query in self.channels else "No"
        else:
            return "No"

# перевірка
controller = TVController(CHANNELS)

print(controller.first_channel())               # BBC
print(controller.last_channel())                # TV1000
print(controller.turn_channel(1))               # BBC
print(controller.next_channel())                # Discovery
print(controller.previous_channel())            # BBC
print(controller.current_channel())             # BBC
print(controller.exists(4))                     # No
print(controller.exists("BBC"))                 # Yes