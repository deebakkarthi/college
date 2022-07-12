def sort(a):
    # Just doing n top level iterations
    # Can check at the end of each iter if the loop is sorted
    # but this is simpler
    for _ in a:
        # Go till the penultimate element
        for j, _ in enumerate(a[:-1]):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return
