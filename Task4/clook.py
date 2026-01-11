# Disk Scheduling - C-LOOK Algorithm Implementation


# Sample Input

# request_queue: cylinder requests (unordered)
# start_head: starting cylinder position of the disk head
# direction: 'left' or 'right' — typically 'right'
request_queue = [98, 183, 37, 122, 14, 124, 65, 67]
start_head = 53
direction = 'right'


def clook_schedule(queue, head, direction):
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
        # jump to smallest on left if any
        if left:
            jump_from, jump_to = current, left[0]
            total += abs(jump_from - jump_to)
            current = jump_to
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
        if right:
            jump_from, jump_to = current, right[-1]
            total += abs(jump_from - jump_to)
            current = jump_to
            for r in reversed(right):
                total += abs(r - current)
                current = r
                order.append(r)

    return order, total


def print_output(queue, head, direction, order, total):
    print("Algorithm: C-LOOK (Disk Scheduling)")
    print("-" * 56)
    print(f"Start Head      : {head}")
    print(f"Request Queue   : {queue}")
    print(f"Direction       : {direction}")
    print("-" * 56)
    print(f"Execution Order : {order}")
    print(f"Total Movement  : {total}")


if __name__ == "__main__":
    order, total = clook_schedule(request_queue, start_head, direction)
    print_output(request_queue, start_head, direction, order, total)
