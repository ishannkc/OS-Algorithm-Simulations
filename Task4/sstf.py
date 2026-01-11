# SSTF Disk Scheduling Algorithm Implementation


# Sample Input

# request_queue: set of pending cylinder requests (order doesn't matter)
# start_head: starting cylinder position of the disk head
request_queue = [98, 183, 37, 122, 14, 124, 65, 67]
start_head = 53


def sstf_schedule(queue, head):

    pending = list(queue)
    order = []
    total = 0
    current = head

    while pending:
        # pick closest request to current
        next_req = min(pending, key=lambda r: abs(r - current))
        total += abs(next_req - current)
        current = next_req
        order.append(next_req)
        pending.remove(next_req)

    return order, total


def print_output(queue, head, order, total):
    print("Algorithm: SSTF (Disk Scheduling)")
    print("-" * 56)
    print(f"Start Head      : {head}")
    print(f"Request Queue   : {queue}")
    print("-" * 56)
    print(f"Execution Order : {order}")
    print(f"Total Movement  : {total}")


if __name__ == "__main__":
    order, total = sstf_schedule(request_queue, start_head)
    print_output(request_queue, start_head, order, total)
