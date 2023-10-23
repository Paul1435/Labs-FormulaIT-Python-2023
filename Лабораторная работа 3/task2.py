def find_common_participants(first_group, second_group, sep_=","):
    participants_list1 = set(first_group.split(sep_))
    participants_list2 = set(second_group.split(sep_))
    common_participants = list(participants_list1.intersection(participants_list2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

