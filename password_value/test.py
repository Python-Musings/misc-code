sequence = ["qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop",
    "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "zxc", "xcv",
    "cvb", "vbn", "bnm"]
#pass1 = 1
#if pass1 == 1:
#    print("Please enter your password")
#    userpassword = str(input(":"))
#    if len(userpassword) in range(8, 24):  # minimum password length
#        print("Processing, stage {1} completed, please wait")
#        lenpoint = point + len(userpassword)  # length of the password
#        print(lenpoint)
#        chars = userpassword
#        for sq in sequence:
#            for sq in sequence:
#                if sq in chars:
#                    print('Found sequence: ', sq)
#                if sq.lower() in userpassword.lower():
#                    point -= 5 * userpassword.lower().count(sq.lower())
#                    print(point)

sequence = ["qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop",
    "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "zxc", "xcv",
    "cvb", "vbn", "bnm"]

for three_chars_in_list in sequence:
    print (three_chars_in_list)
    for letter in range(len(three_chars_in_list)):
        print (three_chars_in_list[letter])

