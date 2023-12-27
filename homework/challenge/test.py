def edit_distance_with_steps(str1, str2):
    if not str1:
        return len(str2), ['插入 ' + str2[i] for i in range(len(str2))]

    if not str2:
        return len(str1), ['刪除 ' + str1[i] for i in range(len(str1))]

    if str1[-1] == str2[-1]:
        distance, steps = edit_distance_with_steps(str1[:-1], str2[:-1])
        return distance, steps

    insert_cost, insert_steps = edit_distance_with_steps(str1, str2[:-1])
    delete_cost, delete_steps = edit_distance_with_steps(str1[:-1], str2)
    replace_cost, replace_steps = edit_distance_with_steps(str1[:-1], str2[:-1])

    if insert_cost <= delete_cost and insert_cost <= replace_cost:
        return 1 + insert_cost, insert_steps + ['插入 ' + str2[-1]]
    elif delete_cost <= insert_cost and delete_cost <= replace_cost:
        return 1 + delete_cost, delete_steps + ['刪除 ' + str1[-1]]
    else:
        return 1 + replace_cost, replace_steps + ['替換 ' + str1[-1] + ' 為 ' + str2[-1]]

if __name__ == "__main__":
    str1 = "kitten"
    str2 = "sitting"
    
    distance, steps = edit_distance_with_steps(str1, str2)
    
    print(f"編輯距離為: {distance}")
    print("編輯步驟:")
    for step in steps[::-1]:
        print(step)
