student_name = input("Enter the learner's name: ").title().strip()

count = 1
mark_list = []
average = 0

print("==================================")
while (count <= 3):
    mark = float(input(f"Enter a mark for Subject {count}: "))
    subject_dict = {f'Subject {count}': {count}, 'Grade Input': mark, 'Letter Grade': '', 'Flags': ''}
    mark_list.append(subject_dict)
    count += 1 

print("============================================================================")
print(f"{student_name.title()} Report Card")
print("============================================================================")
print('''Subect No. |   Grade Input    |    Letter Grade   |        Flags       ''')
print("----------------------------------------------------------------------------")
count = 1

# Letter assignment, average calc & display
for subject in mark_list:

    if subject['Grade Input'] >= 80:
        subject['Letter Grade'] = 'A'
        subject['Flags'] = 'None'
    elif subject['Grade Input'] in range(70, 80):
        subject['Letter Grade'] = 'B'
        subject['Flags'] = 'None'
    elif subject['Grade Input'] in range(60, 70):
        subject['Letter Grade'] = 'c'
        subject['Flags'] = 'None'
    elif subject['Grade Input'] in range(50, 60):
        subject['Letter Grade'] = 'D'
        subject['Flags'] = 'None'
    else:
        subject['Letter Grade'] = 'F'
        if subject['Grade Input'] < 40:
            subject['Flags'] = 'Needs intervention'
        else:
            subject['Flags'] = 'None'

    print(f'''    {count}      |       {subject['Grade Input']}       |         {subject['Letter Grade']}         |     {subject['Flags']}''')
    print("----------------------------------------------------------------------------")
    average += subject['Grade Input']
    count += 1

average /= 3
print(f"Average: {round(average, 2)} %")

if average >= 50:
    print("Status: Pass")
else:
    print("Status: Fail")
    