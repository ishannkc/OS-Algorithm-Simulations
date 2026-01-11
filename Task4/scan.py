# Disk Scheduling - SCAN Algorithm Implementation

# Sample Input

# request_queue: cylinder requests (unordered)
# start_head: starting cylinder position of the disk head
# direction: initial direction, either 'left' (toward 0) or 'right' (toward max)
# disk_min/disk_max: cylinder bounds
request_queue = [98, 183, 37, 122, 14, 124, 65, 67]
start_head = 53
direction = 'right'
disk_min, disk_max = 0, 199


def scan_schedule(queue, head, direction, dmin, dmax):

    left = sorted([r for r in queue if r < head])
    right = sorted([r for r in queue if r >= head])

    order = []
    total = 0
    current = head

    if direction == 'right':
        # go right first
        if right:
            for r in right:
                total += abs(r - current)
                current = r
                order.append(r)
            # go to end if last request isn't at end
            if current != dmax:
                total += abs(dmax - current)
                current = dmax
        # reverse and go left
        for r in reversed(left):
            total += abs(r - current)
            current = r
            order.append(r)
    else:
        # go left first
        if left:
            for r in reversed(left):
                total += abs(r - current)
                current = r
                order.append(r)
            if current != dmin:
                total += abs(current - dmin)
                current = dmin
        # reverse and go right
        for r in right:
            total += abs(r - current)
            current = r
            order.append(r)

    return order, total


def print_output(queue, head, direction, dmin, dmax, order, total):
    print("Algorithm: SCAN (Disk Scheduling)")
    print("-" * 56)
    print(f"Start Head      : {head}")
    print(f"Request Queue   : {queue}")
    print(f"Direction       : {direction}")
    print(f"Disk Range      : [{dmin}, {dmax}]")
    print("-" * 56)
    print(f"Execution Order : {order}")
    print(f"Total Movement  : {total}")


if __name__ == "__main__":
    order, total = scan_schedule(request_queue, start_head, direction, disk_min, disk_max)
    print_output(request_queue, start_head, direction, disk_min, disk_max, order, total)
