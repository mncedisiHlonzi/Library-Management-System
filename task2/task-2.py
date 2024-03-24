#TASK 2
library_codes = [14, 15, 16, 17, 18, 19, 20]

normal_list = []
for code in library_codes:
    normal_list.append(code)

comprehensive_list = [code for code in library_codes]

print("Normal List:", normal_list)
print("Comprehensive List:", comprehensive_list)

normal_list_audit = []
for code in library_codes:
    normal_list_audit.append(code)

comprehensive_list_audit = sum([code for code in library_codes])

print("Normal List for Audit:", normal_list_audit)
print("Comprehensive List for Audit:", comprehensive_list_audit)

normal_odd_list = []
for code in library_codes:
    if code % 2 != 0:
        normal_odd_list.append(code)

comprehensive_odd_list = [code for code in library_codes if code % 2 != 0]

print("Normal Odd Numbers List:", normal_odd_list)
print("Comprehensive Odd Numbers List:", comprehensive_odd_list)

code_set = set(library_codes)
print("Code Set:", code_set)