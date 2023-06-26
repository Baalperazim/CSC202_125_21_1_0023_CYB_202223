import matplotlib.pyplot as plt

# Data collection and analysis (Person 1)
distance = [1, 2, 3, 4, 5]  # Distance from the lawn mower in meters
sound_intensity = [80, 75, 70, 65, 60]  # Sound intensity levels in decibels (dB) at each distance

# Data analysis
plt.plot(distance, sound_intensity, marker='o')  # Plotting the collected data points
plt.xlabel('Distance (m)')  # Label for x-axis
plt.ylabel('Sound Intensity (dB)')  # Label for y-axis
plt.title('Sound Intensity of Lawn Mower')  # Title of the plot
plt.grid(True)  # Enable grid lines
plt.show()  # Display the plot

# Calculate sound reduction levels needed for the simulation
reduction_levels = [max(sound_intensity) - intensity for intensity in sound_intensity]  # Calculating reduction levels

print("Sound Reduction Levels:")
for distance, reduction in zip(distance, reduction_levels):
    print(f"At {distance} meters: {reduction} dB")  # Displaying the reduction levels
