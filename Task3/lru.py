# LRU Page Replacement Algorithm Implementation

# Sample Input 

# reference_string: sequence of page numbers requested over time
# frames: number of physical frames available
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3


def lru_page_replacement(ref, frame_count):

    if frame_count <= 0:
        return (len(ref), 0, 0.0)

    in_memory = set()
    last_used = {}  # page -> last index where it was used

    hits = 0
    faults = 0

    for i, page in enumerate(ref):
        if page in in_memory:
            hits += 1
            last_used[page] = i
        else:
            faults += 1
            if len(in_memory) < frame_count:
                in_memory.add(page)
                last_used[page] = i
            else:
                # Evict least recently used page (smallest last_used index)
                victim = min(in_memory, key=lambda p: last_used[p])
                in_memory.remove(victim)
                last_used.pop(victim, None)

                in_memory.add(page)
                last_used[page] = i

    hit_ratio = hits / len(ref) if ref else 0.0
    return faults, hits, hit_ratio


def print_lru_output(ref, frame_count, faults, hits, hit_ratio):

    print("Algorithm: LRU (Page Replacement)")
    print("-" * 52)
    print(f"Reference String: {ref}")
    print(f"Frames: {frame_count}")
    print("-" * 52)
    print(f"Page Faults = {faults}")
    print(f"Hit Ratio   = {hit_ratio:.2f}")


if __name__ == "__main__":
    faults, hits, hit_ratio = lru_page_replacement(reference_string, frames)
    print_lru_output(reference_string, frames, faults, hits, hit_ratio)
