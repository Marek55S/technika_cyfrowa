import csv

states = ["R1", "R0", "ST","CN","CPR"]
change_states = ["R1'", "R0'", "ST'","CN'","CPR'"]
buttons = ["S", "P", "N", "PR"]


def calc_next(r1,r0):
    if r1 == 0 and r0 == 0:
        return 0,1
    elif r1 == 0 and r0 == 1:
        return 1,0
    elif r1 == 1 and r0 == 0:
        return 1,1
    else:
        return  0,0


def calc_prev(r1,r0):
    if r1 == 0 and r0 == 0:
        return 1,1
    elif r1 == 0 and r0 == 1:
        return 0,0
    elif r1 == 1 and r0 == 0:
        return 0,1
    else:
        return 1,0


def FP(r1,r0,st,cn,cpr,s,p,n,pr):
    r1_, r0_,st_,cn_,cpr_ = r1,r0,st,cn,cpr

    if s == 1:
        st_ = 1

    elif p == 1:
        st_ = 0

    if cn == 0 and n == 1:
        cn_ = 1

    elif cn == 1 and n == 0:
        r1_, r0_ = calc_next(r1, r0)
        cn_ = 0
        st_ = 1

    elif cpr == 0 and pr == 1:
        cpr_ = 1

    elif cpr == 1 and pr == 0:
        r1_, r0_ = calc_prev(r1, r0)
        cpr_ = 0
        st_ = 1

    return r1_, r0_,st_,cn_,cpr_


def create_truth_table():
    truth_table = [states + buttons + change_states]
    for r1 in range(2):
        for r0 in range(2):
            for st in range(2):
                for cn in range(2):
                    for cpr in range(2):
                        for s in range(2):
                            for p in range(2):
                                for n in range(2):
                                    for pr in range(2):
                                        r1_, r0_, st_, cn_, cpr_ = FP(r1,r0,st,cn,cpr,s,p,n,pr)
                                        truth_table.append([r1,r0,st,cn,cpr,s,p,n,pr,r1_, r0_, st_, cn_,cpr_])

    return truth_table


if __name__ == '__main__':

    tt_table = create_truth_table()
    with open("truth_table3.csv", mode="w", newline="", encoding="utf-8") as plik:
        writer = csv.writer(plik, delimiter=';')
        writer.writerows(tt_table)






