a="WLXOVYEX"
b="WXMNWX"

def edit_distance(str1,str2):
    if str1=="":return len(str2)
    if str2=="":return len(str1)

    if str1[0]==str2[0]: 
        return edit_distance(str1[1:],str2[1:])
    
    del_cost = edit_distance(str1[1:],str2) + 1
    ins_cost = edit_distance(str1,str2[1:]) + 1
    rep_cost = edit_distance(str1[1:],str2[1:]) + 1

    return min(del_cost,ins_cost,rep_cost)

print(f'edit distance = {edit_distance(a,b)}')
    