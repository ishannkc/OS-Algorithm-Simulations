# LOOK Disk Scheduling Algorithm Implementation

# Sample Input

# request_queue: cylinder requests (unordered)
# start_head: starting cylinder position of the disk head
# direction: initial direction, either 'left' or 'right'
request_queue = [98, 183, 37, 122, 14, 124, 65, 67]
start_head = 53
direction = 'right'


def look_schedule(queue, head, direction):

    left = sorted([r for r in queue if r < head])
    right = sorted([r for r in queue if r >= head])

    order = []
    total = 0
    current = head

    if direction == 'right':
        # go to highest request, then reverse
        for r in right:
            total += abs(r - current)
            current = r
            order.append(r)
        for r in reversed(left):
            total += abs(r - current)
            current = r
            order.append(r)
    else:
        for r in reversed(left):
            total += abs(r - current)
            current = r
            order.append(r)
        for r in right:
            total += abs(r - current)
            current = r
            order.append(r)

    return order, total


def print_output(queue, head, direction, order, total):
    print("Algorithm: LOOK (Disk Scheduling)")
    print("-" * 56)
    print(f"Start Head      : {head}")
    print(f"Request Queue   : {queue}")
    print(f"Direction       : {direction}")
    print("-" * 56)
    print(f"Execution Order : {order}")
    print(f"Total Movement  : {total}")


if __name__ == "__main__":
    order, total = look_schedule(request_queue, start_head, direction)
    print_output(request_queue, start_head, direction, order, total)
