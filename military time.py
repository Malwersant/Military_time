def time_convert():
    user_time = input().split()
    user_time = user_time[0].split(':') + list(user_time[1])
    pm_list = list(range(13, 25))
    pm_list_1 = list(range(1, 13))
    # pm_dict = dict(list(enumerate(pm_list, 1)))
    pm_dict = dict(zip(pm_list_1, pm_list))

    if user_time[2] == 'P':
        return f"{pm_dict[int(user_time[0])]}:{user_time[1]}"
    else:
        return f"{user_time[0]}:{user_time[1]}"


print(time_convert())

