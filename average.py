print("Student Grade")
Pre=float(input("PRELIMS: "))
Mid=float(input("MIDTERMS: "))
Semi=int(input("SEMI'S: "))
Fin=int(input("FINALS: "))

Ave = (Pre + Mid+ Semi + Fin)/4

if(Ave >= 75):
    print("Passed!")
else:
    print("Failed!")
