time_present = int(input("Time: "))

queue_time = int(input("Alarm: "))

time_present = time_present + queue_time%24

if time_present < 12:
  print(str(time_present)+"am")

else:
  time_present = time_present - 12
  print(str(time_present)+"pm")