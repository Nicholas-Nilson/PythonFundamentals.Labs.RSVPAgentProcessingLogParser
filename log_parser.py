import re

# Sample Output:
# WARNINGS:
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.

f = open("./data/rsvp_agent_log.dat", "r")


# print(f.readline()*5)
# print(f.read())

# for line in f:
#     print(line.rstrip("\n"))

# gotta be a cleaner way to do this
def get_warning_lines(file):
    output = []
    pattern = re.compile("(WARNING)")
    for i, line in enumerate(file):
        for match in re.finditer(pattern, line):
            output.append(line.rstrip("\n"))
    return output
# print(get_warning_lines(f))


def remove_colon_dots(input):
    return re.sub("(WARNING)[:].*[:]",  "--", input)
# print(remove_colon_dots(
#     "03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available."))


def log_parser(file):
    warning_lines = get_warning_lines(file)
    for line in warning_lines:
        print(remove_colon_dots(line))


log_parser(f)



