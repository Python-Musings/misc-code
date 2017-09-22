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

#sequence = ["qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop",
#    "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "zxc", "xcv",
#    "cvb", "vbn", "bnm"]

#for three_chars_in_list in sequence:
#    print (three_chars_in_list)
#    for letter in range(len(three_chars_in_list)):
#        print (three_chars_in_list[letter])

pass_chars = '1t@Es#t2TIM#'
total_score = 0
for char in pass_chars:
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        print ("Char is uppercase: {}".format(char))
        total_score += 5
    elif ord(char) >= ord('a') and ord(char) <= ord('z'):
        print ("Char is lowercase: {}".format(char))
        total_score += 1
    elif ord(char) >= ord('0') and ord(char) <= ord('9'):
        print ("Char is a number: {}".format(char))
        total_score += 2
    elif ord(char) >= ord('#') and ord(char) <= ord('&'):
        print ("Char is a special char: {}".format(char))
        total_score += 10
    elif ord(char) >= ord('@'):
        print ("Char is a special char: {}".format(char))
        total_score += 10
print ("Total Score: {}".format(total_score))

looking_for_filename = "thEfiLENameofMyFile.txt"
filename_found = "TheFileNameOFMYfile.txt"

if looking_for_filename == filename_found:
    print ("{} : are the same : {}".format(looking_for_filename,filename_found))
else:
    print ("{} : are not the same : {}".format(looking_for_filename,filename_found))

if looking_for_filename.lower() == filename_found.lower():
    print ("{} : are the same : {}".format(looking_for_filename.lower(),filename_found.lower()))
else:
    print ("{} : are not the same : {}".format(looking_for_filename.lower(),filename_found.lower()))
