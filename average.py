print("Student Grade")
Pre=float(input("PRELIMS: "))
Mid=float(input("MIDTERMS: "))
Semi=int(input("SEMI'S: "))
Fin=int(input("FINALS: "))

Ave = (Pre + Mid+ Semi + Fin)/4

if Ave>=99 and Ave<=100:
    print("Your Average is {} " .format(Ave) + "you PASSED your grade is A")
elif Ave>=90 and Ave<98:
    print("Your Average is {} " .format(Ave) + "you PASSED your grade is B")
elif Ave>=80 and Ave<90:
    print("Your Average is {} " .format(Ave) + "you PASSED your grade is C")
elif Ave>=71 and Ave<80:
    print("Your Average is {} " .format(Ave) + "you PASSED your grade is D")
    elif Ave>=61 and Ave<70:
    print("Your Average is {} " .format(Ave) + "you FAILED and your grade is E")
elif Ave<=60:
    print("Your Average is {} " .format(Ave) + "you FAILED and your grade is F")
else:
    print("INVALID INPUT")
