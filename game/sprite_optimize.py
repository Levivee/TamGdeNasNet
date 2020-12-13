data = """


"""

list_of = {"mon": "m", "sara": "s", "sai": "sa", "al": "a", "tch": "tch", "rbk": "rbk"}

three = [i for i in list_of.values() if len(i) == 3]



new_one = {}
for i in list_of.values():
    new_one[i] = ""

data = data.split("\n")
for i in data:
    if "//" in i:

        i = i[i.index("/") + 2:i.rindex("/") - 1]
        if len(i) > 8:
            print(i)
            continue
        for j in list_of.keys():
            i = i.replace(j, list_of[j])

        try:
            if i[:3] in three:
                if new_one[i[:3]]:
                    print("hide {}".format(new_one[i[:3]]))
            elif "sa" in i:
                if new_one["sa"]:
                    print("hide {}".format(new_one["sa"]))
            else:
                if new_one[i[0]]:
                    print("hide {}".format(new_one[i[0]]))
            print("show {}".format(i))
            if i[:3] in three:
                new_one[i[:3]] = i
            elif "sa" in i:
                new_one["sa"] = i
            else:
                new_one[i[0]] = i
        except Exception as ex:
            print(ex)
    else:
        pass
        print(i)