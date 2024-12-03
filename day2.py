# Each row is a report
# Report is only safe if:
#   1. Strictly increasing or decreasing
#   2. Adjacent difference is at least 1, at most 3

def parse_input(file_dir):
    reports = []
    with open(file_dir, 'r') as f:
        for line  in f:
            report = [int(num) for num in line.split()]
            reports.append(report)
    return reports
# Q1
def calculate_safe_reports(reports):
    res = 0
    for report in reports:
        if is_safe(report):
            res += 1
    return res

def is_safe(report):
    if len(report) == 1:
        return True
    _increasing = report[0] < report[1]
    for i in range(1, len(report)):
        # increasing or decreasing check
        if _increasing:
            if report[i - 1] > report[i]:
                return False
        else:
            if report[i - 1] < report[i]:
                return False
        # diff check
        if not 1 <= abs(report[i - 1] - report[i]) <= 3:
            return False 
    return True

#Q2
def calculate_safe_reports2(reports):
    res = 0
    for report in reports:
        if is_safe(report):
            res +=1 
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1:]):
                    res += 1
                    break
    return res

if __name__ == "__main__":
    # test
    reports = parse_input("./day2_test_input.txt")
    assert calculate_safe_reports(reports) == 2
    assert calculate_safe_reports2(reports) == 4

    reports = parse_input("./day2_input.txt")
    total = calculate_safe_reports(reports)
    print(total)
    
    total2 = calculate_safe_reports2(reports)
    print(total2)