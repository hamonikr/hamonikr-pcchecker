import subprocess
from datetime import date

def count_score():
    cnt = 0
    total_cnt = 0

    pw_date = subprocess.check_output("sudo passwd -S $PCCHECKER_USER | awk '{print $3}'", shell=True).decode().split(
        '/')
    total_cnt += 2
    if date.today() == date(int(pw_date[2]), int(pw_date[0]), int(pw_date[1])):
        pw_date = 0
    else:
        pw_date = int(str(date.today() - date(int(pw_date[2]), int(pw_date[0]), int(pw_date[1]))).split(' day')[0])
    if 30 >= pw_date:
        cnt += 2
    elif 90 >= pw_date:
        cnt += 1

    update_list = subprocess.check_output("apt list --upgradable | wc -l", shell=True).decode().strip()
    total_cnt += 2
    if 5 >= int(str(update_list)):
        cnt += 2

    ufw_val = subprocess.check_output("sudo ufw status | awk '{print $2}' | head -1", shell=True).decode().strip()
    total_cnt += 2
    if ufw_val == "활성" or ufw_val == "active":
        cnt += 2

    ts_path = "/timeshift/snapshots"
    backup_list = subprocess.check_output("ls " + ts_path, shell=True).decode().strip().split('\n')
    backup_list_len = int(len(backup_list))
    backup_list = sorted(backup_list, reverse=True)
    bk_date_list = backup_list[0].split('_')[0].split('-')
    bk_date = date(int(bk_date_list[0]), int(bk_date_list[1]), int(bk_date_list[2]))
    diff_day = str(date.today() - bk_date)
    if "0:00:00" == diff_day:
        diff_day = 0
    else:
        diff_day = int(str(date.today() - bk_date).split(' day')[0])
    total_cnt += 2
    if 30 > diff_day:
        cnt += 2
    elif 60 > diff_day:
        cnt += 1
    return (cnt,total_cnt)

# status n info
def set_score():
    (cnt,total_cnt) = count_score()
    total_score_val = round(cnt / total_cnt * 100)
    if 100 == total_score_val:
        total_score_text = "<span color='green' font='40'><b>" + str(total_score_val) + "</b></span><span><b>/100</b></span>"
        total_status_text = "<span color='green' font='80'><b>안전</b></span>"
        total_info_text = "<span>시스템이 안전합니다.</span>"
    elif 70 < total_score_val:
        total_score_text = "<span color='orange' font='40'><b>" + str(total_score_val) + "</b></span><span><b>/100</b></span>"
        total_status_text = "<span color='orange' font='80'><b>주의</b></span>"
        total_info_text = "<span>시스템 관리에 주의가 필요합니다.</span>"
    else:
        total_score_text = "<span color='red' font='40'><b>" + str(total_score_val) + "</b></span><span><b>/100</b></span>"
        total_status_text = "<span color='red' font='80'><b>위험</b></span>"
        total_info_text = "<span>시스템을 관리해 주시기 바랍니다.</span>"
    return (total_score_text, total_status_text, total_info_text)
