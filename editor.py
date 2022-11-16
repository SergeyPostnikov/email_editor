def persons(data_lists):
    persons = []
    for iter in data_lists:
        if iter[0].istitle() and iter[1].istitle() and len(iter[2]) == 7 and iter[3]:
            persons.append([iter[0],iter[1], iter[2], iter[3]])
    persons[3][1] = "Abramov" #  специально изменил, имя и фамилию, чтобы проверить работо-
    persons[3][0] = "Ivan" #  способность условного цикла в функции email_get(persons)
    return persons


def email_get(persons):
    emails = []
    letter = 1
    for iter in persons:
        mail =  iter[1] + '.' + iter[0][0:letter] + '@company.io'
        if mail in emails:
            letter += 1
            mail = iter[1] + '.' + iter[0][0:letter] + '@company.io'
            emails.append(mail)
        else:
            emails.append(mail)
    return emails


if __name__ == '__main__':
    with open("task_file.txt", "r" ) as f:
        data_lists = []
        for iter in f.readlines():
            iter = iter.strip(', ').lstrip(" ").rstrip("\n")
            data_lists.append(iter.split(", "))
        name_of_titles= data_lists.pop(0) # список сохранил, как название ключей(NAME, SURNAME etc.)
        persons = persons(data_lists)
        emails = email_get(persons)

     with open("task_file.txt", "w") as f:
        f.write(", ".join(name_of_titles) + "\n")
        for i, value in enumerate(persons):
            value.insert(0, emails[i])
            value = ", ".join(value) + "\n"
            f.write(value)
