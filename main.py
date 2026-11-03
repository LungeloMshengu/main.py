import random
from datetime import datetime

print("================================")
print("       ALVEX TECHNOLOGIES")
print("   MACHINE INTELLIGENCE SYSTEM")
print("================================")

machine_name = "Industrial Motor"

def monitor_machine():
    temperature = random.randint(35, 100)
    vibration = round(random.uniform(1, 12), 2)

    print("\nMachine:", machine_name)
    print("Time:", datetime.now().strftime("%H:%M:%S"))
    print("Temperature:", temperature, "°C")
    print("Vibration:", vibration, "mm/s")

    if temperature > 80 or vibration > 8:
        print("WARNING: ABNORMAL MACHINE CONDITION")
        print("Action: Inspect machine")
    else:
        print("Status: NORMAL")
        print("Action: Continue monitoring")

for reading in range(5):
    monitor_machine()
    print("------------------------------")

print("\nMonitoring session completed.")