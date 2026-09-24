@echo off
set /A Leerzeichen = 0
set /A count = 0
:Leerzeichen
if %Leerzeichen% LEQ 30 (
	set /A Leerzeichen = %Leerzeichen% + 1
	set /A count = %Leerzeichen%
	:count
	if %count% LEQ 0 (
		echo 1
		set /A count = %count% - 1
		goto :count
	)
	echo 0
	goto :Leerzeichen
)
pause