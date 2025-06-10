import gc
import tracemalloc
start = tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()
d = [20,30, 40]
def addition(d):
  count = 0
  for i in d:
    count += i
  print(count)
  return count
snapshot2 = tracemalloc.take_snapshot()
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print(addition(d))
#end = tracemalloc.end()
print(top_stats)
# del(count)
