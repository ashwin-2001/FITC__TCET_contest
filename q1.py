no_of_lines = int(input())
lst = []
for i in range(no_of_lines):
    c = int(input())
    lst.append(str(c))

output_list = [no_of_lines]
for x in lst:
    occurances = 0
    for t in x:
        if t=="5":occurances+=1
    output_list.append(occurances)
for p in output_list:
    print(p)


