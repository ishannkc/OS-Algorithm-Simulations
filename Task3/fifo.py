# FIFO Page Replacement Algorithm Implementation

# Sample Input

# reference_string: sequence of page numbers requested over time
# frames: number of physical frames available
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3


def fifo_page_replacement(ref, frame_count):

    if frame_count <= 0:
        return (len(ref), 0, 0.0)

    from collections import deque

    in_memory = set()       # which pages are currently loaded
    order = deque()         # queue to track the order pages were loaded

    hits = 0
    faults = 0

    for page in ref:
        if page in in_memory:
            hits += 1
        else:
            faults += 1
            if len(in_memory) < frame_count:
                in_memory.add(page)
                order.append(page)
            else:
                # Evict the oldest page (front of the queue)
                victim = order.popleft()
                in_memory.remove(victim)
                in_memory.add(page)
                order.append(page)

    hit_ratio = hits / len(ref) if ref else 0.0
    return faults, hits, hit_ratio


def print_fifo_output(ref, frame_count, faults, hits, hit_ratio):
    
    print("Algorithm: FIFO (Page Replacement)")
    print("-" * 52)
    print(f"Reference String: {ref}")
    print(f"Frames: {frame_count}")
    print("-" * 52)
    print(f"Page Faults = {faults}")
    print(f"Hit Ratio   = {hit_ratio:.2f}")


if __name__ == "__main__":
    faults, hits, hit_ratio = fifo_page_replacement(reference_string, frames)
    print_fifo_output(reference_string, frames, faults, hits, hit_ratio)
