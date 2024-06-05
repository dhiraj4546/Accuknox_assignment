import psutil

# Define thresholds
cpu_threshold = 80  # percentage
mem_threshold = 80  # percentage
disk_threshold = 80  # percentage
process_threshold = 100  # number of processes

# Function to send alert
def send_alert(metric, value, threshold):
    print(f"ALERT: {metric} usage is {value}%, exceeding threshold of {threshold}%")

# Check CPU usage
cpu_percent = psutil.cpu_percent(interval=1)
if cpu_percent > cpu_threshold:
    send_alert("CPU", cpu_percent, cpu_threshold)

# Check memory usage
mem_percent = psutil.virtual_memory().percent
if mem_percent > mem_threshold:
    send_alert("Memory", mem_percent, mem_threshold)

# Check disk usage
disk_usage = psutil.disk_usage('/')
disk_percent = disk_usage.percent
if disk_percent > disk_threshold:
    send_alert("Disk", disk_percent, disk_threshold)

# Check number of running processes
num_processes = len(psutil.pids())
if num_processes > process_threshold:
    send_alert("Processes", num_processes, process_threshold)
print("CPU PERCENTAGE:",cpu_percent)
print("MEMORY PERCENTAGE:",mem_percent)
print("DISK PERCENTAGE:",disk_percent)
print("NO. OF PROCESSES:",num_processes)
