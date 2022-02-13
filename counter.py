def duplicate_count(text):
    duplicate = 0
    counted = []
    givenlist = sorted(text.lower())
    for i in givenlist:
        if i not in counted:
            if givenlist.count(i) >= 2:
                duplicate += 1
                counted.append(i)

    return(duplicate)


duplicate_count("Orange")
duplicate_count("abcdeaa")
duplicate_count('aABb')
duplicate_count('21332aa1b44ccddeeffb66')
# x = "0SqIJZ3Jdyn45ULjrs0oVkHEfREd64FiLuOssclmpPWkM"
# x = x.lower()
# x = sorted(x)
# print(x)
