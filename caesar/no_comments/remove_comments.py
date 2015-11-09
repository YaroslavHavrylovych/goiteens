file_name = "../no_loop"
f_source = open(file_name + '.py', 'r')
f_dest = open("no_comments.py", 'w')
f_dest.truncate()
for line in f_source:
    if len(line) > 0 and line[0] == "#":
        continue
    if '#' in line :
        ind = line.find('#')
        line = line[:ind] + '\n'
    f_dest.write(line)
f_source.close()
f_dest.close()

