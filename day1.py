# Pair smallest value from left list with right list, then the second smallest etc.
# Find the distance between the ordered values
# Sum all distances

def parse_input(file_dir):
    left = []
    right = []
    with open(file_dir, 'r') as f:
        for line in f:
            l, r = line.strip().split()
            left.append(int(l))
            right.append(int(r))
    return left, right

def get_distance(left, right):
    left.sort()
    right.sort()
    res = 0
    for i in range(len(left)):
        res += abs(left[i] - right[i])
    return res

def calculate_similarity_score(left, right):
    right_counter = {}
    for num in right:
        right_counter[num] = 1 + right_counter.get(num, 0)
    
    res = 0
    for num in left:
        if num in right_counter:
            res += num * right_counter[num]
    return res

if __name__ == "__main__":
    # Part 1
    left, right = parse_input("./day1_input.txt")
    d = get_distance(left, right)
    print(d)
    # Part 2
    l_t, r_t = parse_input("./day1_test_input.txt")
    assert calculate_similarity_score(l_t, r_t) == 31
    s = calculate_similarity_score(left, right)
    print(s)
    