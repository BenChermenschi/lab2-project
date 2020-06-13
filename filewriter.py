#filewriter
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%d-%m-%Y_%H:%M:%S")
print ("Current time is ", current_time)

filename = current_time + ".txt"
file_object = open(filename,"w+")

file_object.write("This is a test")
file_object.close()
print ("done")

