import re
employee_id = [  "AB1 0AA",
                 "AZ1A 1AA",
                 "SW1A 2BA",
                 "BX3 2BB",
                 "DH98 1BT",
                 "N1 9UU",
                 "EEZ3 1TT",
                 "TIM E52",
                 "A B1 A22",
                 "AB34 2DD",
                 "SE9 2HG",
                 "N1 11H",
                 "AC1V 8DS",
                 "WCC1 9DD",
                 "B4C 1LK",
                 "B28 9AD",
                 "WE12 7RJ",
                 "AABB 007",
                ]
patt = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}"
for Eid in employee_id:
    r = re.search(patt, Eid)
    if r:
        print(Eid + " is employee of XYZ")
    else:
        print(Eid + " is not an employee of XYZ")

