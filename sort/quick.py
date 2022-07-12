def sort(a, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(a)-1
    if left < right:
        pivot = part(a, left, right)
        sort(a, left, pivot-1)
        sort(a, pivot+1, right)


def part(a, left, right):
    # swap middle element with the left most
    (a[left], a[(left + r) // 2]) = (a[(left + r) // 2], a[left])
    # pivot_index
    p_i = l
    # pivot value
    p = a[p_i]
    while left < r:
        while left < len(a) and a[left] <= p:
            left = left + 1
        while a[right] > p:
            right = right - 1
        # Check forightoverlap
        if left < right:
            # swap misplaced elements
            (a[left], a[right]) = (a[right], a[left])
    # put pivot in the correct place
    (a[p_i], a[right]) = (a[right], a[p_i])
    return r
