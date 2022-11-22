import json
import datetime
import os.path

data  = str(datetime.datetime.now())

if  not os.path.exists("program_time.json"):
    print("the program is launched for the first time")
    data = [data]
    with open("program_time.json", 'w') as write_time:
        json.dump(data, write_time)
        write_time.write('\n')
        
else:
    with open("program_time.json", 'r') as read_time:
        last_data = json.load(read_time)
        
    print("the time of the last 1-3 calls of the program:")
    if len(last_data) <= 3:
        for i in range(len(last_data)):
            print(last_data[i])
    else:
        print(last_data[-3], '\n', last_data[-2], '\n', last_data[-1])
        
    last_data.append(data)
    with open("program_time.json", 'w') as write_time:
        json.dump(last_data, write_time)
        write_time.write('\n')