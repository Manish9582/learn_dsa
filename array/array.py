from array import *

class StudentManage:
    def __init__(self):
        self.studentName=None;
        self.marks=array('i',[])
       


class Student:
    mng=StudentManage();
    def AddStudent(self,Name):
        storeName=Student.mng.studentName=Name
        print(storeName)
        print(Name)
    
    
    def AddMarks(self):
        inputSize=input('Enter the total subjcet  : ')
        if(type(int(inputSize))!=int):
            print('Enter the number only')
            return;
        count=1;
        while int(inputSize) >=count:
            marks=input("Enter the marks : ")
            Student.mng.marks.append(int(marks));
            count+=1;
     
    def showAllMarks(self):
       return list(Student.mng.marks);
                
    def TotalMarks(self):
       data=self.showAllMarks();
       total=0;
       for d in data:
           total+=d;
       return total;   
   
    def Average(self):
        length=len(self.showAllMarks());
        total=self.TotalMarks()
        return total/length;
   
    def Percantage(self):
        length=len(self.showAllMarks());
        total=self.TotalMarks()
        return (total*100)/(length*100);
          
    def GradeNumber(self):
        percantage=int(self.Percantage());
        if percantage>85:
            return "S"
        elif percantage>75:
            return "A"
        elif percantage>65:
            return "B"
        elif percantage>55 and percantage >=40:
            return "C"
        else:
            return "F"
       
     
    def getHightestNumber(self):
        allmarks=self.showAllMarks();
        bigNumber=0;
        for marks in allmarks:
            if marks>bigNumber:
                bigNumber=marks;
        return bigNumber; 
    
    
    def getSamllNumber(self):
        allmarks=self.showAllMarks();
        samllNumber=allmarks[0];
        for marks in allmarks:
            if marks<samllNumber:
                samllNumber=marks;
        return samllNumber;           
    
std=Student();
std.AddStudent('Manish')
std.AddMarks();

AllSubject=std.showAllMarks();
print(AllSubject)

total=std.TotalMarks();
print(total)

average=std.Average()
print(average)

percangae=std.Percantage()
print(percangae)
grade=std.GradeNumber()
print(grade)

bigNumber=std.getHightestNumber();
print(bigNumber)

smallNumber=std.getSamllNumber();
print(smallNumber)