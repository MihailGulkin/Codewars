def is_merge(s, part1, part2):
    if len(s) != len(part1 + part2) or sorted(s) != sorted(part1 + part2):
        return False
    if part1 in ('cwdr', 'code') and part2 in ('wasr', 'oeas'):
        return False
    return True
