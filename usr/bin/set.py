import subprocess
from gi.repository import Gtk
from datetime import date
import os

##알람기능##
def set_alarm():
    lbl_alarm_info = Gtk.Label()
    switch_alarm = Gtk.Switch()
    switch_alarm.set_tooltip_text("PC의 보안 상태를 체크하여 '위험' 상태일 경우 주기적으로 알림을 표시합니다.")
    try:
        subprocess.check_output("systemctl status pcchecker_alarm.timer | grep inactive", shell=True, stderr=subprocess.STDOUT).decode().strip()
        alarm_info=("알람이 <span color='red'><b>꺼져</b></span> 있습니다.")
        lbl_alarm_info.set_markup(alarm_info)
        switch_alarm.set_active(0)
    except subprocess.CalledProcessError as e:
        alarm_info = ("알람이 <span color='green'><b>켜져</b></span> 있습니다.")
        lbl_alarm_info.set_markup(alarm_info)
        switch_alarm.set_active(1)
    return (lbl_alarm_info, switch_alarm, alarm_info)

##비밀번호##
def set_password():
    pw_date = subprocess.check_output("sudo passwd -S $PCCHECKER_USER | awk '{print $3}'", shell=True).decode().split(
        '/')
    if date.today() == date(int(pw_date[2]), int(pw_date[0]), int(pw_date[1])):
        pw_date = 0
    else:
        pw_date = int(str(date.today() - date(int(pw_date[2]), int(pw_date[0]), int(pw_date[1]))).split(' day')[0])

    if 30 >= pw_date:
        pw_status = "<span background='green' font='15' color='white'><b> 안   전 </b></span>"
        pw_past = "비밀번호 변경 후 <span color='green'><b> " + str(pw_date) + "</b></span> 일 지났습니다."
    elif 90 >= pw_date:
        pw_status = "<span background='orange' font='15' color='white'><b> 주   의 </b></span>"
        pw_past = "비밀번호 변경 후 <span color='orange'><b> " + str(pw_date) + "</b></span> 일 지났습니다."
    else:
        pw_status = "<span background='red' font='15' color='white'><b> 위   험 </b></span>"
        pw_past = "비밀번호 변경 후 <span color='red'><b> " + str(pw_date) + "</b></span> 일 지났습니다."
    return (pw_status, pw_past)

##업데이트##
def set_update():
    update_list = subprocess.check_output("apt list --upgradable | wc -l", shell=True).decode().strip()
    if 5 >= int(str(update_list)):
        update_status = "<span background='green' font='15' color='white'><b> 최   신 </b></span>"
        update_info = "업그레이드 가능한 패키지가 <span color='green'><b>" + str(update_list) + "</b></span> 개 있습니다."
    else:
        update_status = "<span background='orange' font='15' color='white'><b> 주   의 </b></span>"
        update_info = "업그레이드 가능한 패키지가 <span color='orange'><b>" + str(update_list) + "</b></span> 개 있습니다."
    return (update_status,update_info)

def set_ufw():
    lbl_ufw_info = Gtk.Label()
    lbl_ufw_status = Gtk.Label()
    switch_ufw = Gtk.Switch()
    # 방화벽에 접근하기위한 ufw 패키지가 없을 경우 설치해준다.
    try:
        ufw_install = subprocess.check_output("dpkg --get-selections | grep ^ufw | awk '{print $2}'",
                                              shell=True).decode().strip()
        if ufw_install != 'install':
            subprocess.call("sudo apt-get --yes --force-yes install ufw", shell=True)
        else:
            print("ufw 이미 설치됨")
    except subprocess.CalledProcessError as e:
        subprocess.call("sudo apt-get --yes --force-yes install ufw", shell=True)
        print("ufw 미설치 -> 설치")

    # 방화벽에 접근하기위한 gufw 패키지가 없을 경우 설치해준다.
    try:
        gufw_install = subprocess.check_output("dpkg --get-selections | grep gufw | awk '{print $2}'",
                                               shell=True).decode().strip()
        if gufw_install != 'install':
            subprocess.call("sudo apt-get --yes --force-yes install gufw", shell=True)
            print("gufw 미설치 -> 설치")
        else:
            print("gufw 이미 설치됨")
    except subprocess.CalledProcessError as e:
        subprocess.call("sudo apt-get --yes --force-yes install gufw", shell=True)
        print("gufw 미설치 -> 설치")

    ufw_val = subprocess.check_output("sudo ufw status | awk '{print $2}' | head -1", shell=True).decode().strip()
    if ufw_val == "비활성" or ufw_val == "inactive":
        ufw_status = "<span background='red' font='15' color='white'><b> 비활성 </b></span>"
        ufw_info=("방화벽이 <span color='red'><b>비활성화</b></span> 되었습니다.")
        lbl_ufw_info.set_markup(ufw_info)
        switch_ufw.set_active(0)
    elif ufw_val == "활성" or ufw_val == "active":
        ufw_status = "<span background='green' font='15' color='white'><b> 활   성 </b></span>"
        ufw_info=("방화벽이 <span color='green'><b>활성화</b></span> 되었습니다.")
        lbl_ufw_info.set_markup(ufw_info)
        switch_ufw.set_active(1)
    else:
        ufw_status = "<span background='orange' font='15' color='white'><b> 오   류 </b></span>"
        ufw_info=("방화벽 상태를 확인 할 수 없습니다.")
        lbl_ufw_info.set_markup(ufw_info)
        switch_ufw.set_active(0)
    lbl_ufw_status.set_markup(ufw_status)
    return (lbl_ufw_status,lbl_ufw_info, switch_ufw, ufw_status, ufw_info)

def set_backup():
    lbl_ts_status = Gtk.Label()
    lbl_ts_info = Gtk.Label()
    # 백업에 접근하기위한 timeshift 패키지가 없을 경우 설치해준다.
    try:
        ts_install = subprocess.check_output("dpkg --get-selections | grep timeshift | awk '{print $2}'",
                                             shell=True).decode().strip()
        if ts_install != 'install':
            subprocess.call("sudo apt-get --yes --force-yes install timeshift", shell=True)
            print("timeshift 미설치 -> 설치")
        else:
            print("timeshift 이미 설치됨")
    except subprocess.CalledProcessError as e:
        subprocess.call("sudo apt-get --yes --force-yes install timeshift", shell=True)
        print("timeshift 미설치 -> 설치")

    ts_path = "/timeshift/snapshots"
    backup_list = ""

    if os.path.isdir(ts_path):
        backup_list = subprocess.check_output("ls " + ts_path, shell=True).decode().strip().split('\n')
        backup_list_len = int(len(backup_list))
        if (backup_list_len == 1 and os.listdir(ts_path) == []):
            backup_ts_status = "<span background='red' font='15' color='white'><b> 위   험 </b></span>"
            backup_list_len = 0
        else:
            backup_list = sorted(backup_list, reverse=True)
            bk_date_list = backup_list[0].split('_')[0].split('-')
            bk_date = date(int(bk_date_list[0]), int(bk_date_list[1]), int(bk_date_list[2]))
            diff_day = str(date.today() - bk_date)
            if "0:00:00" == diff_day:
                diff_day = 0
            else:
                diff_day = int(str(date.today() - bk_date).split(' day')[0])

            if 30 > diff_day:
                ts_status = "<span background='green' font='15' color='white'><b> 안   전 </b></span>"
            elif 60 > diff_day:
                ts_status = "<span background='orange' font='15' color='white'><b> 주   의 </b></span>"
            else:
                ts_status = "<span background='red' font='15' color='white'><b> 위   험 </b></span>"
    else:
        ts_status = "<span background='red' font='15' color='white'><b> 위   험 </b></span>"
        backup_list_len = 0

    if (backup_list_len >= 1 and os.listdir(ts_path)):
        ts_info=(str(len(backup_list)) + " 개의 백업이 있습니다.\n마지막 백업은 <b>" + bk_date_list[0] + "년" + bk_date_list[1] + "월" +
            bk_date_list[2] + "일</b> 입니다.")
        lbl_ts_info.set_markup(ts_info)
    else:
        ts_info=("시스템 안전을 위해 백업을 진행하십시오.")
        lbl_ts_info.set_markup(ts_info)
    lbl_ts_status.set_markup(ts_status)
    return (lbl_ts_status, lbl_ts_info, ts_status, ts_info)