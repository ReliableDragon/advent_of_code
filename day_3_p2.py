print(
    sum(
        map(
            lambda c: (ord(c) - ord('a') + 1) if c.islower() else (ord(c) - ord('A') + 27),
            map(
                lambda l: next(iter(set(l[0]) & set(l[1]) & set(l[2]))), 
                zip(
                    *(
                        (iter(open('day_3.input').read().split('\n')),) * 3
                    )
                )
            )
        )
    )
)