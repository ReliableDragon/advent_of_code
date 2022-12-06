
print(sum(sorted([sum([int(line) for line in lines.split('\n')]) for lines in open('day_1_p1.input').read().split('\n\n')], reverse=True)[:3]))
