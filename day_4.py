from operator import methodcaller

print(
    sum(
        map(
            lambda l: (not (l[0][0] == l[1][0] and l[0][1] == l[1][1])) and (l[0][0] <= l[1][0] and l[0][1] >= l[1][1]) or (l[1][0] <= l[0][0] and l[1][1] >= l[0][1]),
            map(
                lambda l: (tuple(map(int, (l[0].split('-')))), tuple(map(int, (l[1].split('-'))))),
                map(
                    methodcaller('split', ','),
                    open('day_4.input').read().split('\n')
                )
            )
        )
    )
)