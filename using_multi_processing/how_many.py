import multiprocessing
# Reminder: all threads in a multi-threading application run on the SAME processor
# We can invoke python on separate processors - multi-processing
# (in multi processing each process has its own copy of python)

num_proc = multiprocessing.cpu_count()
# we use threading for concurent work e.g. sockets microservices image processing, data analysis
# we use mutliprocessing for e.g. web server, db server, file server ...

print(f'This device has {num_proc} processors')