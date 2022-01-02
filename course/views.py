from django.shortcuts import render

# Create your views here.
general_mandatory_university = [
    ("ENG1011", "Communicative English Skills", 3, "None"),
    ("ENG1022", "Basic Writing Skills", 3, "ENG1011"),
    ("LAR1011", "Introduction to Civics and Ethics", 3, "None"),
    ("LAR1012", "Logic and Critical thinking", 3, "None"),
    ("HPEd1011", "Health and Physical Education I", 0, "None"),
    ("HPEd1022", "Health and Physical Education II", 0, "None"),
]
general_mandatory_school = [
    ("SOS311", "Principles of Economics", 3, "None"),
    ("SOS412", "Entrepreneurship for Engineers", 2, "None"),
    ("CSE4221", "Engineering Research and Development Methodology", 2, "None"),
]

general_elective = [

    ("ENG2031", "Technical Report Writing for Science and Technology", 2, "None"),
    ("SOS362", "Organizational Behavior", 2, "None"),
    ("SOS372", "Leadership and Change", 2, "None"),
    ("SOS313", "Introduction to Management", 2, "None"),
    ("LAR3032", "Industrial and Organizational Psychology", 3, "None"),
    ("LAR4022", "Cognitive Psychology", 3, "None"),
    ("LAR3042", "Introduction to LAW", 3, "None"),
]

basic_mandatory_university = [
    ("Math1101", "Applied Mathematics I", 4, "None"),
    ("Phys1101", "General Physics I", 3, "None"),
    ("Chem1101", "General Chemistry", 3, "None"),
    ("CSE1101", "Introduction to Computing", 3, "None"),
    ("Math1102", "Applied Mathematics II", 4, "Math1101"),
    ("DME1102", "Engineering Drawing", 3, "None"),
    ("Phys1102", "General Physics II", 3, "Phys1101"),
    ("CSE1102", "Fundamentals of Programming", 3, "CSE1101"),
]

basic_mandatory_school = [
    ("Math2101", "Applied Mathematics III", 4, "Math1102"),
    ("PCE2101", "Fundamentals of Electrical Engineering", 4, "Math1101"),
    ("ECE2101", "Electronic Circuit I", 4, "PCE2101"),
    ("CSE2101", "Data Structures and Algorithms", 3, "CSE1102"),
    ("ISE2101", "Fundamentals of Information", 3, "None"),
]

basic_mandatory_program = [
    ("CSE2206", "Discrete Mathematics for Computer Science", 3, "Math1101"),
    ("ECE3103", "Probability and Random Process", 3, "Math2101"),
]

major_mandatory = [
    ("CSE2202", "Object Oriented Programming", 3, "None"),
    ("CSE2222", "Data Structures and Algorithm", 3, "CSE1102"),
    ("CSE3211", "Algorithms", 3, "CSE2222 or CSE2101"),
    ("ECE3204", "Digital Logic Design", 3, "ECE2201"),
    ("CSE3203", "Computer Architecture & Organization", 3, "ECE3204"),
    ("CSE3204", "Operating Systems", 4, "CSE3203"),
    ("CSE3206", "Introduction to Artificial Intelligence", 3, "None"),
    ("CSE3213", "Fundamentals of Software Engineering", 3, "None"),
    ("CSE3207", "Database Systems", 3, "None"),
    ("CSE3221", "Data Communication and computer Networks", 3, "None"),
    ("CSE4202", "Programming Languages", 3, "None"),
    ("CSE4201", "Formal Language & Automata Theory", 3, "None"),
]

research = [
    ("CSE5213", "Seminar", 1, "None"),
    ("CSE5211", "Semester Project", 2, "Senior standing courses"),
    ("CSE5221", "B.Sc. Project", 4, "Senior standing courses"),
]

major_elective = [
    ("ECE2202", "Electronic Circuit II", 4, "ECE2201"),
    ("CSE2320", "System Programming", 3, "None"),

    ("CSE3306", "Web Programming", 3, "None"),
    ("CSE3310", "Computer Graphics", 3, "None"),
    ("CSE3312", "Advanced Programming", 3, "CSE2202"),
    ("CSE3308", "Software Requirement Engineering", 3, "CSE3213"),
    ("CSE4304", "Information Storage and Retrieval", 3, "None"),
    ("CSE3314", "Microcomputer & interfacing", 3, "CSE3203"),

    ("ECE2204", "Signals and Systems", 3, "Math2101"),
    ("CSE4303", "Multimedia Technologies", 3, "None"),
    ("CSE4307", "Network and information security", 3, "None"),
    ("CSE4311", "Mobile Computing and Applications", 3, "CSE2202"),
    ("CSE5317", "Introduction to Data mining", 3, "CSE3207"),
    ("CSE5321", "Introduction to NLP", 3, "None"),
    ("CSE4309", "Software Design and Architecture", 3, "CSE3213"),

    ("ECE3205", "Digital Signal Processing", 3, "ECE2204"),
    ("PCE3201", "Electrical Network Analysis and synthesis", 3, "ECE2206"),
    ("CSE4312", "Introduction to Computer Vision", 3, "None"),
    ("CSE4310", "Compiler Design", 3, "CSE4201"),
    ("CSE4302", "Project Management", 3, "None"),
    ("ECE5303", "VLSI Design", 3, "CSE3203"),

    ("CSE5307", "Distributed Systems", 3, "CSE2202"),
    ("CSE5309", "Wireless Mobile Networks", 3, "CSE3221"),
    ("CSE5311", "Image Processing", 3, "ECE3205"),
    ("CSE5313", "Human Computer Interaction", 3, "None"),
    ("CSE5315", "Introduction to Audio & Video Production", 3, "None"),
    ("CSE5319", "Advanced Network", 3, "CSE3221"),
    ("PCE3204", "Introduction to Control Systems", 3, "PCE3201"),

    ("CSE5312", "Computer Ethic & Social Issues", 3, "None"),
    ("CSE5304", "Computer Games & Animation", 3, "None"),
    ("CSE5306", "Special Topics in Computer Science and Engineering", 3, "None"),
    ("CSE5308", "Real time and Embedded Systems", 3, "ECE4202"),
    ("CSE5310", "Software Quality & Testing", 3, "CSE3213"),
    ("PCE5308", "Introduction to Robotics and Industrial Automation", 3, "PCE3204"),
]

mandatory = {
    "general_mandatory_university": general_mandatory_university, 
    "general_mandatory_school": general_mandatory_school,
    'major_mandatory': major_mandatory,
    'basic_mandatory_program': basic_mandatory_program,
    'basic_mandatory_school': basic_mandatory_school,
    'basic_mandatory_university': basic_mandatory_university,
    'research': research
}

all_course_group = {
    "general_mandatory_university": general_mandatory_university, 
    "general_mandatory_school": general_mandatory_school,
    'major_mandatory': major_mandatory,
    'basic_mandatory_program': basic_mandatory_program,
    'basic_mandatory_school': basic_mandatory_school,
    'basic_mandatory_university': basic_mandatory_university,
    'research': research,
    'general_elective': general_elective,
    'major_elective': major_elective
} 
all_course_code = []
for i in all_course_group:
    for j in all_course_group[i]:
        all_course_code.append(j[0])

elective = [(0, 2, 1, "2nd year 2nd semister"), (2, 8, 1, "3rd year 2nd semister"), 
            (8, 15, 4, "4th year 1st semister"), (15, 21, 3, "4th year 2nd semister"),
            (21, 28, 3, "5th year 1st semister"), (28, 34, 2, "5th year 2nd semister")]

all_course_dict = {}
for i in all_course_group:
    for j in all_course_group[i]:
        all_course_dict[j[0]] = j[1:]

def index(request):
    return render(request, 'index.html')

def course(request):
    return render(request, 'courses.html', all_course_group)

def ajax_audit(request):
    total = request.GET.getlist('total_submit[]')  
    free = request.GET.getlist('final_arr[]')
    free_elective = []
    for i in free:
        if i == ',,,':
            continue
        if i[0] in all_course_code:
            continue
        x = i.split(',')
        free_elective.append((x[0], x[1], int(x[2]), x[3]))
    courses = [i for i in total]
    total_credit = 0
    for cou in courses:
        total_credit += all_course_dict[cou][1]

    for cou in free_elective:
        total_credit += cou[2]

    reserve = []
    not_taken = dict()
    man_not_taken = []
    for i in mandatory:
        for j in mandatory[i]:
            if j[0] not in courses:
                man_not_taken.append(j)
    not_taken["mandatory"] = man_not_taken
    semester_elective = []
    general_elective_not_taken =  {}
    for i in elective:
        x = major_elective[i[0]: i[1]]
        y = i[2]
        c = 0
        for j in x:
            if j[0] in courses:
                c += 1
                if c > y:
                    reserve.append(j[0])
        if c < y:
            semester_elective.append((i[3], y-c))
    if semester_elective:
        not_taken["major_elective"] = semester_elective
    else:
        not_taken["major_elective"] = None
    not_taken["general_elective"] = None
    c = 0
    for j in general_elective:
        if j[0] in courses:
            c += 1
            if c > 2 and j[2] == 3:
                reserve.append(j[0])
                print(j[0])
    if c < 2:
        not_taken["general_elective"] = 2-c
    if len(reserve) >= 3:
        not_taken["free_elective"] = None
    else:
        free_count = 3 - len(reserve)
        for i in free_elective:
            if i[2] == 3:
                free_count -= 1
        if free_count <= 0:
            not_taken["free_elective"] = None
        else:
            not_taken["free_elective"] = free_count
    
    if not_taken["mandatory"] or not_taken["general_elective"] or not_taken["major_elective"] or not_taken["free_elective"]   :
        not_taken["ok"] = "No"
    else:
        not_taken["ok"] = "yes"
    return render(request, 'result.html', {"total_credit": total_credit, 'not_taken': not_taken})
