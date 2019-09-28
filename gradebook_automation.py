import openpyxl
gradebook = openpyxl.load_workbook("sample_grades.xlsx")
grades = gradebook.get_sheet_by_name("Sheet1")
test_1_scores = []
for i in range(2, grades.max_row + 1):
  test_1_scores.append(grades["B" + str(i)].value)
print(test_1_scores)
