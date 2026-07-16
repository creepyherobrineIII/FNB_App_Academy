
loop_count = 1
student_list = []
student_status_list = []
average = 0

def assign_letter_grade(mark):
    letter_to_ret = ''
    if mark >= 80:
        letter_to_ret = 'A'
    elif mark in range(70, 80):
        letter_to_ret = 'B'
    elif mark in range(60, 70):
        letter_to_ret = 'c'
    elif mark in range(50, 60):
        letter_to_ret = 'D'
    else:
        letter_to_ret = 'F'

    return letter_to_ret

def assign_subject_flag(marks_dictionary):
    flag_dict = {}

    for subject, mark in marks_dictionary.items():
        if mark < 40:
            flag_dict[subject] = 'Needs intervention'
        else:
            flag_dict[subject] = 'None'
    
    return flag_dict

def calc_class_stats(students):
    class_stats = {'Average': 0, "Highest Mark": {}, "Lowest Mark": {}}
    highest_mark = 0
    lowest_mark = 100
    class_ave = 0
    subject_count = 0

    for student in students:
        for subject, student_mark in student['Marks'].items():
            class_ave += student_mark
            subject_count += 1

            if student_mark > highest_mark:
                highest_mark = student_mark
                class_stats['Highest Mark'] = {'Student Name': student['Name'], 'Subject': subject, 'Mark': student_mark}

            if student_mark < lowest_mark:
                lowest_mark = student_mark
                class_stats['Lowest Mark'] = {'Student Name': student['Name'], 'Subject': subject, 'Mark': student_mark}

    
    class_ave = round((class_ave / subject_count), 2)
    class_stats['Average'] = class_ave
    return class_stats

while (loop_count <= 5):
    student_ave = 0
    student_status = ''

    student_name = input("Enter the learner's name: ").title().strip()
    maths_mark = float(input("Enter a mark for Maths: "))
    english_mark = float(input("Enter a mark for English: "))
    science_mark = float(input("Enter a mark for Science: "))
    student_ave = (maths_mark + english_mark + science_mark) / 3
    student_ave = round(student_ave, 2)
   
    if student_ave < 50:
        student_status = 'Fail'
    else:
        student_status = 'Pass'

    student_mark_dict = {'Name': student_name, 'Marks': {'Maths': maths_mark, 'English': english_mark, 'Science': science_mark}}
    student_status_dict = {'Name': student_name, 'Flags': assign_subject_flag(student_mark_dict['Marks']), 'Status': student_status, 'Average': student_ave}
    student_list.append(student_mark_dict)
    student_status_list.append(student_status_dict)
    print("=========================================================")
    loop_count += 1


print("======================================================================================================================================")
print('''                                                       GRADE REPORT GENERATOR                                                     ''')
print("======================================================================================================================================")
print('''Student Name | Maths | Letter Grade | English | Letter Grade | Science | Letter Grade | Status | Average | Flags                  ''')
print("--------------------------------------------------------------------------------------------------------------------------------------")
count = 0


# Display individual report stats
for student in student_list:

    print(f'''{student['Name']} | {student['Marks']['Maths']} | {assign_letter_grade(student['Marks']['Maths'])} | {student['Marks']['English']} | {assign_letter_grade(student['Marks']['English'])} | {student['Marks']['Science']} | {assign_letter_grade(student['Marks']['Science'])} | {student_status_list[count]['Status']} |  {student_status_list[count]['Average']} | { student_status_list[count]['Flags']}                ''')
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    count += 1

# Display class stats
print(' ')
print("======================================================================================================================================")
print('''                                                            CLASS STATS                                                           ''')
print("======================================================================================================================================")
print('''Class Average   |        Highest Mark            |               Lowest Mark              ''')
class_stats_var = calc_class_stats(student_list)
print(f''' {class_stats_var['Average']}  |          {class_stats_var['Highest Mark']}    |         {class_stats_var['Lowest Mark']}  ''')


