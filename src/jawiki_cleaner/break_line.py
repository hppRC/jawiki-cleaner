from .clean_text import clean_text


def break_line(text):
    res = []
    tmp = ""
    # 「　『 ( 【
    aligns = [0, 0, 0, 0]
    for ch in text:
        if ch == "「":
            aligns[0] += 1
        elif ch == "」":
            aligns[0] -= 1
        elif ch == "『":
            aligns[1] += 1
        elif ch == "』":
            aligns[1] -= 1
        elif ch == "(":
            aligns[2] += 1
        elif ch == ")":
            aligns[2] -= 1
        elif ch == "【":
            aligns[3] += 1
        elif ch == "】":
            aligns[3] -= 1

        if ch == "。" and sum(abs(x) for x in aligns) == 0:
            res.append(tmp + "。")
            tmp = ""
        else:
            tmp += ch
    else:
        res.append(tmp.strip())

    if not sum(abs(x) for x in aligns) == 0:
        tmp = ""
        for ch in text:
            if ch == "「" and aligns[0] > 0:
                aligns[0] -= 1
            elif ch == "」" and aligns[0] < 0:
                aligns[0] += 1
            elif ch == "『" and aligns[1] > 0:
                aligns[1] -= 1
            elif ch == "』" and aligns[1] < 0:
                aligns[1] += 1
            elif ch == "(" and aligns[2] > 0:
                aligns[2] -= 1
            elif ch == ")" and aligns[2] < 0:
                aligns[2] += 1
            elif ch == "【" and aligns[3] > 0:
                aligns[3] -= 1
            elif ch == "】" and aligns[3] < 0:
                aligns[3] += 1
            else:
                tmp += ch
        return break_line(tmp).strip()

    res = [clean_text(x).strip() for x in res]
    return "\n".join(x for x in res if len(x) > 10)
