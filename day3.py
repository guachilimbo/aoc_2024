import re

def parse_input(file_dir):
    with open(file_dir) as f:
        return f.read()

def get_muls(memory):
    return re.findall(r"mul\((\d+),(\d+)\)", memory)

def get_total(memory):
    res = 0
    for a, b in get_muls(memory):
        res += int(a) * int(b)
    return res



def get_total2(memory):
    res = 0
    multiplications = re.findall(r"(?s)don't\(\).*?(?:do\(\)|$)|mul\((\d+),(\d+)\)", memory)
    for a, b in multiplications:
        if a and b:
            res += int(a) * int(b)
    return res

    
if __name__ == "__main__":
    assert get_total("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161
    assert get_total2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48

    memory = parse_input("./day3_input.txt")
    print(get_total(memory))
    print(get_total2(memory))
    
