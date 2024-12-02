def readReports(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    lines = data.splitlines()
    reports = []
    for line in lines:
        reports.append([int(l) for l in line.split(" ")]) 
    
    return reports

def numberOfSafeReports(file_path):
    reports = readReports(file_path)
    safeReports = sum(1 for report in reports if isSafeReport(report))
    return safeReports

def isSafeReport(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    all_positive = all(difference > 0 for difference in differences)
    all_negative = all(difference < 0 for difference in differences)

    if not all_negative and not all_positive:
        return False
    
    if all_positive:
        return max(differences) <= 3
    
    if all_negative:
        return min(differences) >= -3
    
    return True

def numberOfSafeReportsDamped(file_path):
    reports = readReports(file_path)
    safeReports = sum(1 for report in reports if isSafeReportDamped(report))
    return safeReports

def isSafeReportDamped(report):
    dampedReports = [report[:i] + report[i+1:] for i in range(len(report))]

    for dampedReport in dampedReports:
        if isSafeReport(dampedReport):
            return True

    return False