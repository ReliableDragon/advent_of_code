from operator import methodcaller

print(
    sum(
        map(
            lambda p: 3 * p[1] + (p[0] if p[1] == 1 else ((p[0] + (1 if p[1] == 2 else -1)) % 3)) + 1,
            [(
                ord(pair[0]) - ord('A'), ord(pair[1]) - ord('X')
            ) for pair in map(
                methodcaller("split", " "), 
                open('day_2.input').read().split('\n')
            )]
        )
    )
)