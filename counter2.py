def duplicate_count(text):
    nlist = sorted(text.lower())
    dupicate = 0
    duplicates = []
    for i in range(len(nlist)-1):
        if nlist[i] == nlist[i + 1] and nlist[i] not in duplicates:
            dupicate += 1
            duplicates.append(nlist[i])
            i += 1
        elif nlist[i] != nlist[i + 1]:
            i += 1

    print(dupicate)


duplicate_count("Orange")
duplicate_count("aaabcde")
duplicate_count('aABbzz')
duplicate_count('21332aa1b44ccddeeffb66')
duplicate_count("0SqIJZ3Jdyn45ULjrs0oVkHEfREd64FiLuOssclmpPWkM")
