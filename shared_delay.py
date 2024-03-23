import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
bufsize = 100
write_pos = 0
delays = [20, 40, 60]  # Delay times in samples
buffer = np.zeros(bufsize)

# Initialize figure for animation
fig, ax = plt.subplots()
line, = plt.plot(buffer, label='Buffer State')
plt.ylim(-2, 3)  # Adjust as necessary to view changes
plt.xlabel('Buffer Position')
plt.ylabel('Value')
plt.title('Shared Buffer Animation')
plt.legend()

# Simulation function to update buffer
def simulate_tick(tick):
    global write_pos, buffer
    input_signal = np.sin(0.1 * tick)
    buffer[write_pos] = input_signal  # Write input to buffer

    for delay in delays:
        read_pos = (write_pos - delay) % bufsize
        buffer[read_pos] += 0.5  # Simulate read operation
    
    write_pos = (write_pos + 1) % bufsize
    line.set_ydata(buffer)  # Update the plotted data

# Animation function
def update(frame):
    simulate_tick(frame)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(100), blit=True)

plt.show()
