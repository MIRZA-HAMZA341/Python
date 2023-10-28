class Prs: 
 def __init__(info, firstname, lastname):
  info.fname = firstname
  info.lname = lastname

 def printname(info):
  print(info.fname, info.lname)
x=Prs("John", "Max")
x.printname()
class Student(Prs):
  def __init__(self, fname):
    super().__init__(fname)