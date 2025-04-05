import os
import shutil


def githubify(data):
    split = data.split("$$")
    for i in range(len(split)):
        if i%2:
            split[i] = "```math" + split[i] + "```"

    data = "\n".join(split)
    split = data.split("$")
    for i in range(len(split)):
        if i%2:
            split[i] = "$`" + split[i] + "`$"
    data = " ".join(split)
    data = data.replace(r"\dag", r"\dagger")
    data = data.replace(r"\bm", "")
    return data

dst = "C:/Users/shara/OneDrive/Desktop/quantum-research"
for f in os.listdir('.'):
    of = dst + "/" + f
    if f.split(".")[-1] == "md":
        with open(f, "r") as obj:
            data = githubify(obj.read())
        with open(of, "w") as obj: 
            obj.write(data)
    elif len(f.split(".")) == 1:
        shutil.copytree(f, of) 
    else:
        shutil.copy(f, of)



