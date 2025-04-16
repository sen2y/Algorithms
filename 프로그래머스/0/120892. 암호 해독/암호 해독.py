def solution(cipher, code):
    # print([i for i, idx in cipher if (idx+1)%code == 0])
    return ''.join([i for idx, i in enumerate(cipher) if (idx+1)%code == 0])