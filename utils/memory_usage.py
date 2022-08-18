#! /usr/bin/env python3
import argparse
import psutil
import time
sleep_time = 2
parser = argparse.ArgumentParser()
parser.add_argument('fn')
args=parser.parse_args()
f = open(args.fn, 'w')
f.write('time,mem_used\n')
for i in range(1000):
    mem_used = psutil.virtual_memory().used/1e9
    time_ = i * sleep_time
    print(i, mem_used)
    f.write('{},{}\n'.format(time_, mem_used))
    f.flush()
    time.sleep(sleep_time)
f.close()


