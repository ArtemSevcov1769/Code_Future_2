import time

def counter(s):
    for let in s:
        count = 0
        for sub_let in s:
            if let == sub_let:
                count += 1


start = time.time()
for i in range(1_000_000_000):
    counter("queue")
end = time.time()
print(end - start)

def counter_2(s):
    for let in set(s):
        count = 0
        for sub_let in s:
            if let == sub_let:
                count += 1

start_2 = time.time()
for i in range(1_000_000_000):
    counter_2("queue")
end_2 = time.time()
print(end_2 - start_2)


