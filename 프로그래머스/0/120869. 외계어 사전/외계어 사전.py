def solution(spell, dic): 
    sorted_spell = sorted(spell)
    sorted_dic = [sorted(i) for i in dic]
    print(sorted_spell, sorted_dic)
    return 1 if sorted_spell in sorted_dic else 2