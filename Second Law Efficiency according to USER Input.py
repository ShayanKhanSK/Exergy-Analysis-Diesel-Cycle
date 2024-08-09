# Define the heat input (Qin) and work output (Wout)
Qin = float(input("Enter heat input (in Joules): "))
Wout = float(input("Enter work output (in Joules): "))

# Calculate efficiency
efficiency = Wout / Qin

# Convert efficiency to a percentage
efficiency_percentage = efficiency * 100

# Print the results
print(f"Efficiency: {efficiency_percentage:.2f}%")


# Define the absolute temperatures of the hot and cold reservoirs in Kelvin
Th = float(input("Enter the absolute temperature of the hot reservoir (in Kelvin): "))
Tc = float(input("Enter the absolute temperature of the cold reservoir (in Kelvin): "))

# Calculate the second law efficiency
second_law_efficiency = 1 - (Tc / Th)

# Convert efficiency to a percentage
second_law_efficiency_percentage = second_law_efficiency * 100

# Print the results
print(f"Second Law Efficiency: {second_law_efficiency_percentage:.2f}%")
