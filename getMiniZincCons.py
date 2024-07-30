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

def getNXOR(n, mode=6):
    truth_table=generate_truth_table(n)
    from sboxanalyzer import SboxAnalyzer as sa
    input_variables=["b"]
    input_variables+=[f"a{i}" for i in range(n-2,-1,-1)]
    cnf, milp = sa.encode_boolean_function(truth_table=truth_table, input_variables=input_variables, mode=mode)
    print("Encoding")
    print(getMiniZincMilpCons(milp))
    print("\n\n\n")

def generate_truth_table(n):
    result = []
    for i in range(2**n):
        # Count the number of 1's in the binary representation of i
        num_ones = bin(i).count('1')
        # Determine if the count is even or odd
        if num_ones % 2 == 0:
            result.append(1)
        else:
            result.append(0)
    return result

