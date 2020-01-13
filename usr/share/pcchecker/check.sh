#!/bin/bash
V3LOG_PATH="/opt/AhnLab/v3desktopforlinux/log/event.log"

CHECK_DAY1=30
CHECK_DAY2=90

TODAY=`date +%m/%d/%Y | awk -F '/' '{print $3$1$2}'`
TODAY_SEC=`date -d "$TODAY" "+%s"`


fn_check-pw(){
	PW_LAST_DATE=`sudo passwd -S -a | awk -v user=$USER '{if(user == $1) {print $3}}' | awk -F '/' '{print $3$1$2}'`
	PW_LAST_DATE_SEC=`date -d "$PW_LAST_DATE" "+%s"`
	
	PW_DIFF_DAY=`echo "($TODAY_SEC - $PW_LAST_DATE_SEC) / 86400" | bc`
	
	if [ $CHECK_DAY2 -le $PW_DIFF_DAY ]
	then
		echo "90 over"
	elif [ $CHECK_DAY1 -le $PW_DIFF_DAY ]
	then
		echo "30 over"
	else
		echo "30 under"
	fi
}


fn_check-v3(){
	V_LAST_DATE=`sudo stat -c "%y" $V3LOG_PATH  | awk -F ' ' '{print $1}' | awk -F '-' '{print $1$2$2}'`
	V_LAST_DATE_SEC=`date -d "$V_LAST_DATE" "+%s"`
	V_DIFF_DAY=`echo "($TODAY_SEC - $V_LAST_DATE_SEC) / 86400" | bc`

	if [ $CHECK_DAY2 -le $V_DIFF_DAY ]
	then
		echo "90 over"
	elif [ $CHECK_DAY1 -le $V_DIFF_DAY ]
	then
		echo "30 over"
	else
		echo "30 under"
	fi

}

main(){
	fn_check-pw
	fn_check-v3
}

main
