import sys


def read_file():
    global data
    data = []
    with open(sys.argv[1]) as f:
        for line in f:
            res = [int(i) for i in line.strip().split() if i.isdigit()]
            data.append(res)
    f.close()


def calc_Probability_Values():
    global PBt, PGt_given_Bt, PGt_given_Bf, PCt, PFt_given_GtCt, PFt_given_GtCf, PFt_given_GfCt, PFt_given_GfCf
    PBt = sum(row[0] == 1 for row in data)/len(data)
    PGt_given_Bt = (sum(row[0] == 1 and row[1] ==
                    1 for row in data)/len(data))/PBt
    PGt_given_Bf = (sum(row[0] == 0 and row[1] ==
                    1 for row in data)/len(data))/(1-PBt)
    PCt = sum(row[2] == 1 for row in data)/len(data)
    PFt_given_GtCt = (sum(row[1] == 1 and row[2] == 1 and row[3] == 1 for row in data)/len(
        data))/(sum(row[1] == 1 and row[2] == 1 for row in data)/len(data))
    PFt_given_GtCf = (sum(row[1] == 1 and row[2] == 0 and row[3] == 1 for row in data)/len(
        data))/(sum(row[1] == 1 and row[2] == 0 for row in data)/len(data))
    PFt_given_GfCt = (sum(row[1] == 0 and row[2] == 1 and row[3] == 1 for row in data)/len(
        data))/(sum(row[1] == 0 and row[2] == 1 for row in data)/len(data))
    PFt_given_GfCf = (sum(row[1] == 0 and row[2] == 0 and row[3] == 1 for row in data)/len(
        data))/(sum(row[1] == 0 and row[2] == 0 for row in data)/len(data))
    print("P(Bt) =", PBt)
    print("P(Gt_given_Bt) =", PGt_given_Bt)
    print("(PGt_given_Bf) =", PGt_given_Bf)
    print("P(Ct) =", PCt)
    print("P(Ft_given_GtCt) =", PFt_given_GtCt)
    print("P(Ft_given_GtCf) =", PFt_given_GtCf)
    print("P(Ft_given_GfCt) =", PFt_given_GfCt)
    print("P(Ft_given_GfCf) =", PFt_given_GfCf)


def calc_Probability(B=None, G=None, C=None, F=None):

    ans = 1
    if B == 't':
        ans = ans*PBt
    else:
        ans = ans*(1-PBt)
    if G == 't':
        if B == 't':
            ans = ans*PGt_given_Bt
        else:
            ans = ans*PGt_given_Bf
    else:
        if B == 't':
            ans = ans*(1-PGt_given_Bt)
        else:
            ans = ans*(1-PGt_given_Bf)
    if C == 't':
        ans = ans*PCt
    else:
        ans = ans*(1-PCt)
    if F == 't':
        if G == 't' and C == 't':
            ans = ans*PFt_given_GtCt
        elif G == 't' and C == 'f':
            ans = ans*PFt_given_GtCf
        elif G == 'f' and C == 't':
            ans = ans*PFt_given_GfCt
        else:
            ans = ans*PFt_given_GfCf
    else:
        if G == 't' and C == 't':
            ans = ans*(1-PFt_given_GtCt)
        elif G == 't' and C == 'f':
            ans = ans*(1-PFt_given_GtCf)
        elif G == 'f' and C == 't':
            ans = ans*(1-PFt_given_GfCt)
        else:
            ans = ans*(1-PFt_given_GfCf)
    return ans


def inf_by_enum(B, G, C, F):
    tf = ['t', 'f']
    ans = 0
    for b in tf:
        if B != None:
            b = B
        for g in tf:
            if G != None:
                g = G
            for c in tf:
                if C != None:
                    c = C
                for f in tf:
                    if F != None:
                        f = F
                    ans = ans+calc_Probability(b, g, c, f)
                    if F != None:
                        break
                if C != None:
                    break
            if G != None:
                break
        if B != None:
            break
    return ans


if __name__ == "__main__":

    read_file()
    calc_Probability_Values()
    B, G, C, F, gB, gG, gC, gF = None, None, None, None, None, None, None, None
    given = False
    for i in range(2, len(sys.argv)):
        if sys.argv[i][0] == 'B':
            if given == True:
                gB = sys.argv[i][1]
                B = sys.argv[i][1]
            B = sys.argv[i][1]
        elif sys.argv[i][0] == 'G':
            if given == True:
                gG = sys.argv[i][1]
                G = sys.argv[i][1]
            G = sys.argv[i][1]
        elif sys.argv[i][0] == 'C':
            if given == True:
                gC = sys.argv[i][1]
                C = sys.argv[i][1]
            C = sys.argv[i][1]
        elif sys.argv[i][0] == 'F':
            if given == True:
                gF = sys.argv[i][1]
                F = sys.argv[i][1]
            F = sys.argv[i][1]
        elif sys.argv[i] == 'given':
            given = True

    if len(sys.argv) > 2:
        print("Output:")
        if given == True:
            print('P(', ' '.join(map(str, sys.argv[2:])), ') = ', inf_by_enum(
                B, G, C, F)/inf_by_enum(gB, gG, gC, gF))
        else:
            print(
                'P(', ' '.join(map(str, sys.argv[2:])), ') = ', inf_by_enum(B, G, C, F))
