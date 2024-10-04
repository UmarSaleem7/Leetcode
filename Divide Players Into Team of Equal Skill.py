def dividePlayers(skill):
    skill.sort()
    skillOfTeam = skill[0] + skill[-1]
    i = 0
    j = len(skill) - 1
    arrOfTuple = []
    while i < j:
        if (skill[i] + skill[j]) == skillOfTeam:
            arrOfTuple.append((skill[i], skill[j]))
        else:
            return -1
        i += 1
        j -= 1
    print(arrOfTuple)
    ans = 0
    for skill1, skill2 in arrOfTuple:
        productOfSkill = skill1 * skill2
        print(productOfSkill)
        ans += productOfSkill
    return ans
