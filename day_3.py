print(
    sum(
        map(
            lambda c: (ord(c) - ord('a') + 1) if c.islower() else (ord(c) - ord('A') + 27),
            map(
                lambda l: next(iter(set(l[:len(l)//2]) & set(l[len(l)//2:]))), 
                open('day_3.input').read().split('\n')
            )
        )
    )
)