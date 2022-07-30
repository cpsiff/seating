result = ""
missed = ""
with open("seats.txt") as f:
    for line in f:
        first_name = line.split(" ")[1]
        last_name = line.split(" ")[0]
        print(line)
        if len(line.split(" ")) == 4:
            table = line.split(" ")[2] + " " + line.split(" ")[3]
            item = f"<tr>\n\t<td>{first_name} {last_name}</td>\n\t<td>{table}</td>\n</tr>\n"
            result += item
        else:
            missed += line

print(result)
print("missed\n", missed)