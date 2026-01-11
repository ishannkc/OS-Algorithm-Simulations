# Disk Scheduling - FCFS Algorithm Implementation


# Sample Input 

# request_queue: cylinder requests in arrival order
# start_head: starting cylinder position of the disk head
request_queue = [98, 183, 37, 122, 14, 124, 65, 67]
start_head = 53


def fcfs_schedule(queue, head):
    order = list(queue)
    total = 0
    current = head
    for r in order:
        total += abs(r - current)
        current = r
    return order, total


def print_output(queue, head, order, total):
    print("Algorithm: FCFS (Disk Scheduling)")
    print("-" * 56)
    print(f"Start Head      : {head}")
    print(f"Request Queue   : {queue}")
    print("-" * 56)
    print(f"Execution Order : {order}")
    print(f"Total Movement  : {total}")


if __name__ == "__main__":
    order, total = fcfs_schedule(request_queue, start_head)
    print_output(request_queue, start_head, order, total)
