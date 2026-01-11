# OPT Page Replacement Algorithm Implementation

# Sample Input

# reference_string: sequence of page numbers requested over time
# frames: number of physical frames available
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3


def opt_page_replacement(ref, frame_count):

    if frame_count <= 0:
        return (len(ref), 0, 0.0)

    in_memory = set()
    hits = 0
    faults = 0

    for i, page in enumerate(ref):
        if page in in_memory:
            hits += 1
            continue

        faults += 1
        if len(in_memory) < frame_count:
            in_memory.add(page)
            continue

        # Need to evict one: choose the page used farthest in the future
        farthest_index = -1
        victim = None
        for p in in_memory:
            try:
                next_use = ref.index(p, i + 1)
            except ValueError:
                # Not used again; best victim
                victim = p
                break
            if next_use > farthest_index:
                farthest_index = next_use
                victim = p

        in_memory.remove(victim)
        in_memory.add(page)

    hit_ratio = hits / len(ref) if ref else 0.0
    return faults, hits, hit_ratio


def print_opt_output(ref, frame_count, faults, hits, hit_ratio):

    print("Algorithm: OPT (Page Replacement)")
    print("-" * 52)
    print(f"Reference String: {ref}")
    print(f"Frames: {frame_count}")
    print("-" * 52)
    print(f"Page Faults = {faults}")
    print(f"Hit Ratio   = {hit_ratio:.2f}")


if __name__ == "__main__":
    faults, hits, hit_ratio = opt_page_replacement(reference_string, frames)
    print_opt_output(reference_string, frames, faults, hits, hit_ratio)
