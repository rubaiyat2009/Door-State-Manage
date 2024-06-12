# Door State Manage 

This project implements a simple state machine for controlling a door that can be either open or closed. The state machine transitions between states based on events. 

## Features - Initial state is 'Closed'. - Handles `open` and `close` events to transition between states. - Provides the current state of the door. 

## Getting Started These instructions will help you set up the project and run it on your local machine. 

### Prerequisites - Python 3.x 
### Installing 
1. Clone the repository: ```sh git clone https://github.com/rubaiyat2009/door-state-manage.git cd door-state-manage ```
2. (Optional) Create and activate a virtual environment: ```sh python -m venv venv source venv/bin/activate # On Windows use `venv\Scripts\activate` ```
4. Install any dependencies (if applicable): ```sh pip install -r requirements.txt ``` 
## Usage You can use the DoorStateMachine class to simulate door operations. 
### Example ```python from door_state_manage import DoorController door = DoorController() print(f'Initial Status: {door.get_status()}') ```

# Outputs: 
   ### Initial Status: Closed
   ### Status after "open" event: Open
   ### Status after "close" event: Closed

## Contributing Please feel free to submit issues and pull requests for any improvements or bug fixes.
