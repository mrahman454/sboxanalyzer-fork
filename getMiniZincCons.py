from sboxanalyzer import *
def getMiniZincMilpCons(inequalities):
    result = '\n /\\\n'.join(inequalities)
    return result

#pass sbox object
#generate diff, deterministic diff, *-DDT, inverse LAT, *-LAT and determinitic LAT constraints for Minizinc
def generateConsFromSbox(sb, ddt=1, starddt=1,detddt=1, lat=1, starlat=1,detlat=1):
    sa=SboxAnalyzer(sb)

    if(ddt==1):
        cnf, milp=sa.minimized_diff_constraints()
        print("DDT")
        print(getMiniZincMilpCons(milp))
        print("\n\n\n")

    if(starddt==1):
        cnfstar, milpstar=sa.minimized_linear_constraints(subtable="star")
        print("*-DDT")
        print(getMiniZincMilpCons(milpstar))
        print("\n\n\n")

    if(detddt==1):
        detdiff=sa.encode_deterministic_differential_behavior()
        print("Deterministic DDT")
        cpdetdiff = sa.generate_cp_constraints(detdiff)
        print(cpdetdiff)
        print("\n\n\n")

    if(lat==1):
        sainv = SboxAnalyzer(sa.inverse())
        print("LAT-inverse")
        cnf1, milp1 = sainv.minimized_linear_constraints()
        print(getMiniZincMilpCons(milp1))
        print("\n\n\n")

    if(starlat==1):
        print("*-LAT-inverse")
        cnf1star, milp1star = sainv.minimized_linear_constraints(subtable='star')
        print(getMiniZincMilpCons(milp1star))
        print("\n\n\n")

    if(detlat==1):
        print("Deterministic LAT inverse")
        detlin = sainv.encode_deterministic_linear_behavior()
        cpdetlin = sainv.generate_cp_constraints(detlin)
        print(cpdetlin)

