class DoorController:
	def __init__(self):
		self.status = 'Closed'
        
	def handle_event(self, event):
		if self.status == 'Closed' and event == 'open':
			self.status = 'Open'
		elif self.status == 'Open' and event == 'close':
			self.status = 'Closed'
            
	def get_status(self):
		return self.status

# Example usage:
door = DoorController()
# Print initial status
print(f'Initial Status: {door.get_status()}')
# Process events
door.handle_event('open')
print(f'Status after "open" event: {door.get_status()}')
door.handle_event('close')
print(f'Status after "close" event: {door.get_status()}')