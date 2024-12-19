from collections import defaultdict

def parse_input(file_dir):
    reports = []
    prereqs = defaultdict(list)
    with open(file_dir, "r") as f:
        for line in f:
            if "," in line:
                report = [int(page) for page in line.strip().split(",")]
                reports.append(report)
            elif "|" in line:
                pre, aft = line.strip().split("|")
                prereqs[int(aft)].append(int(pre))
    return prereqs, reports

def get_valid_reports(prereqs, reports):
    valid = []
    for report in reports:
        if is_valid_report(prereqs, report):
            valid.append(report)
    return valid

def is_valid_report(prereqs, report):
    seen = set()
    for page in report:
        for seen_page in seen:
            if page in prereqs[seen_page]:
                return False
        seen.add(page)
    return True

def get_total(valid_reports):
    res = 0
    for report in valid_reports:
        res += report[(len(report) - 1)//2]
    return res

if __name__ == "__main__":
    prerequs, reports = parse_input("./day5_input.txt")
    valid = get_valid_reports(prerequs, reports)
    print(get_total(valid))

                


