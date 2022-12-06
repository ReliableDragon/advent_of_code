from operator import methodcaller

print(
    sum(
        map(
            lambda p: p[1] + 1 + (3 if p[0] == p[1] else 6 * (p[1] == (p[0] + 1) % 3)), 
            [(
                ord(pair[0]) - ord('A'), ord(pair[1]) - ord('X')
            ) for pair in map(
                methodcaller("split", " "), 
                open('day_2.input').read().split('\n')
            )]
        )
    )
)