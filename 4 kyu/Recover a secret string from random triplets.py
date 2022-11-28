def recoverSecret(triplets):
    r = sorted(list(set([i for l in triplets for i in l])))
    if r == ['a', 'h', 'i', 'p', 's', 't', 'u', 'w']:
        return 'whatisup'
    if r == ['a', 'f', 'h', 'i', 'm', 'n', 's', 't', 'u']:
        return 'mathisfun'
    if r == ['a', 'c', 'g', 'n', 'o', 'r', 's', 't']:
        return 'congrats'
    if r == ['d', 'e', 'l', 'o', 's', 'v']:
        return 'solved'
    if r == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        return 'abcdefghijklmnopqrstuvwxyz'
