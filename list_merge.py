
def list_merge_sort(l1, l2):
    return sorted(l1 + l2)[:5]


def list_merge(l1, l2):
    i, j, result = 0, 0, []
    while len(result) < 5:
        if l1[i] == l2[j]:
            result.append(l1[i])
            result.append(l2[j])
            i += 1
            j += 1
            continue
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
            continue
        else:
            result.append(l2[j])
            j += 1
    return result[:5]


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

print(list_merge(list1, list2))