users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
count_all_users = len(users)
count_uniq_users = len(set(users))

statistics["Общее количество"] = count_all_users
statistics["Уникальные посещения"] = count_uniq_users

print(statistics)
