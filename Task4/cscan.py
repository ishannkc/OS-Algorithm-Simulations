# Disk Scheduling - C-SCAN Algorithm Implementation


# Sample Input

# request_queue: cylinder requests (unordered)
# start_head: starting cylinder position of the disk head
# direction: 'left' or 'right' — for C-SCAN we typically use 'right'
# disk_min/disk_max: cylinder bounds
request_queue = [98, 183, 37, 122, 14, 124, 65, 67]
start_head = 53
direction = 'right'
disk_min, disk_max = 0, 199


def cscan_schedule(queue, head, direction, dmin, dmax):

    left = sorted([r for r in queue if r < head])
    right = sorted([r for r in queue if r >= head])

    order = []
    total = 0
    current = head

    if direction == 'right':
        # service right side
        for r in right:
            total += abs(r - current)
            current = r
            order.append(r)
        # go to end then jump to start
        if current != dmax:
            total += abs(dmax - current)
            current = dmax
        # jump to dmin
        total += abs(dmax - dmin)
        current = dmin
        # service left side (ascending)
        for r in left:
            total += abs(r - current)
            current = r
            order.append(r)
    else:
        # service left side (descending)
        for r in reversed(left):
            total += abs(r - current)
            current = r
            order.append(r)
        if current != dmin:
            total += abs(current - dmin)
            current = dmin
        # jump to dmax
        total += abs(dmax - dmin)
        current = dmax
        # service right side (descending to ascending start)
        for r in reversed(right):
            total += abs(r - current)
            current = r
            order.append(r)

    return order, total


def print_output(queue, head, direction, dmin, dmax, order, total):
    print("Algorithm: C-SCAN (Disk Scheduling)")
    print("-" * 56)
    print(f"Start Head      : {head}")
    print(f"Request Queue   : {queue}")
    print(f"Direction       : {direction}")
    print(f"Disk Range      : [{dmin}, {dmax}]")
    print("-" * 56)
    print(f"Execution Order : {order}")
    print(f"Total Movement  : {total}")


if __name__ == "__main__":
    order, total = cscan_schedule(request_queue, start_head, direction, disk_min, disk_max)
    print_output(request_queue, start_head, direction, disk_min, disk_max, order, total)
