import re
import time
import csv
# Opens the data file tegrastats.log and reads each line individually
fh = open("tegrastats.log","r").readlines()

# Opens the data file tegrastats.log and reads the whole file in order to use later
r= open("tegrastats.log","r").read()
count = re.findall(r"RAM.\d\d\d\d\D\d\d\d\d\w\w", r)
data = []
# loops through the program using the length of the count variable for how many times it should loop
# It also loops line by line. So each variable is using its respective data from the line.
for num in range(len(count)):
    # Searches for RAM in the dataset.
    ram = re.search(r"RAM.(\d\d\d\d\D\d\d\d\d)", fh[num]).group(1)
    # Searches for the GPU usage and frequency.
    gpu = re.search(r"GR3D_FREQ (\d\d\D\D\d\d\d\d)", fh[num])
    # Searches for the CPU usage and frequency.
    cpu = re.search(r"CPU \[(.+?)\]", fh[num]).group(1)
    # Searches for the GPU Temperature. The regex pattern allows for a two digit number followed by a possible decimal.
    gpu_temp = re.search(r"GPU.(\d\d(\.\d)?C)", fh[num]).group(1)
    # Searches for the MCPU Temperature. The regex pattern allows for a two digit number followed by a possible decimal.
    mcpu_temp = re.search(r"MCPU.(\d\d(\.\d)?C)", fh[num]).group(1)
    # Searches for the BCPU Temperature. The regex pattern allows for a two digit number followed by a possible decimal.
    bcpu_temp = re.search(r"BCPU.(\d\d(\.\d)?C)", fh[num]).group(1)
    split_gpu = [None, None]
    # Checks to see if the GPU is equal to None. If it isn't then it adds the GPU information
    if gpu !=None:
        split_gpu = gpu.group(1).split('@')
    # Separates the RAM data by the slash symbol
    split_ram = ram.split('/')
    # Separates the CPU data by the comma symbol
    split_cpu = cpu.split(',')
    # Splits the CPU data that was taken in the previous line by the @ symbol,
    # which allows CPU usage and frequency to be separated
    real_split_cpu = [i.split('@') for i in split_cpu]
    # Data is being saved in the variable row. The data is also being formatted with an F-string to make it clearer.
    # Also the Ram Usage Percentage is the ram usage divided by the total ram, then multiplied by 100 and rounded up
    row = [num+1, time.time(), f" Ram Used:{split_ram[0]}", f" Ram total:{split_ram[-1]} MB", f" Ram Usage Percentage:{round((int(split_ram[0])/int(split_ram[-1])),2)*100}% "]
    # Adds the CPU Usage after looping through all the data in cpu.
    [row.append(cpu[0])for cpu in real_split_cpu]
    # Adds the CPU frequency after looping through all the data in cpu.
    [row.append(cpu[1]) for cpu in real_split_cpu]
    # Adds the GPU used to the list "row" and it is formatted with an f-string to make the data clearer.
    row.append(f" GPU Used:{split_gpu[0]}")
    # Adds the GPU frequency to the list "row" and it is formatted with an f-string to make the data clearer.
    row.append(f" GPU Frequency:{split_gpu[1]}")
    # Adds the BCPU temperature and it is formatted with an f-string to have clear data.
    row.append(f" BCPU Temp:{bcpu_temp}")
    # Adds the MCPU temperature and it is formatted with an f-string to keep the data clear.
    row.append(f" MCPU Temp:{mcpu_temp}")
    # Adds the GPU temperature to the list "row" and it is formatted with an f-string to make the data clearer.
    row.append(f" GPU Temp:{gpu_temp}")


    # Adds the list "row" to the variable data.
    data.append(row)
# Opens the csv file under the name file. If a csv file does not exist it will then create one.

with open("data.csv", mode="w") as file:
    writer = csv.writer(file)
    # Writes the data as rows and not individual data.
    writer.writerows(data)