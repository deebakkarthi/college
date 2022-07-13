def sort(a):
    if len(a) > 1:
        m = len(a) // 2
        left = a[:m]
        right = a[m:]
        sort(left)
        sort(right)
        size_l = len(left)
        size_r = len(right)
        # Merging
        # i ind of left
        # j ind of right
        # k ind of a
        i = j = k = 0
        while True:
            # finding the smallest of the two
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
                k += 1
                # left over
                if i == size_l:
                    while j < size_r:
                        a[k] = right[j]
                        j += 1
                        k += 1
                    return
            else:
                a[k] = right[j]
                j += 1
                k += 1
                # right over
                if j == size_r:
                    while i < size_l:
                        a[k] = left[i]
                        i += 1
                        k += 1
                    return
