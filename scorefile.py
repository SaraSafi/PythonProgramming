from pandas import *
import csv
from csv import writer
class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score

class CourseUtil:
    def __init__(self,address):
        self.address=address

    def set_file(self):
        column=Grade('student_id','course_code','score')
        col=[]
        col.append(column.student_id)
        col.append(column.course_code)
        col.append(column.score)

        with open(self.address, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(col)

    def load(self,line_number):
        file = open(self.address, 'r')
        c = csv.DictReader(file)
        row=[]
        for r in c:
            row.append(r)
        return f'the selected row of line number {line_number} is : {row[line_number]}'

    def calc_student_average(self,student_id):
        df=read_csv(self.address)
        user = df[df['student_id'] == student_id]
        u=user.to_dict()
        v=list(u.values())[2]
        score1=list(v.values())
        print(f'the score of student with student id {student_id} is: {score1}')
        ave=sum(score1)/len(score1)
        print(f'the average of student score with student id {student_id} is: {ave}')

    def calc_course_average(self, course_code):
        df=read_csv(self.address)
        user = df[df['course_code'] == course_code]
        n=user.to_dict()
        m=list(n.values())[2]
        score2=list(m.values())
        print(f'the score of student with student id {course_code} is: {score2}')
        ave1=sum(score2)/len(score2)
        print(f'the average of student score with course id {course_code} is: {ave1}')

    def count(self):
        df = read_csv(self.address)
        score = df['score'].tolist()
        return f'the number of scores:{len(score)}'

    def save(self):
        while True:
            grade=Grade(input('std_id:'),input('crc_id:'),input('score:')  )
            g=[]
            g.append(grade.student_id)
            g.append(grade.course_code)
            g.append(grade.score)
            file = open(self.address, 'a')
            write=writer(file)
            write.writerow(g)
            file.close()
            text=int(input('do you want to continue(yes=1/no=2):'))
            if text==2:
                break




address=input('enter filename:')
G=CourseUtil(address)
G.set_file()
G.save()
line=int(input('enter line number to show details:'))
print(G.load(line))
s=int(input('enter the student id to calculate the average:'))
G.calc_student_average(s)
b=int(input('enter the course code to calc the average:'))
G.calc_course_average(b)
print(G.count())
