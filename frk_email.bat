@Echo Off

chcp 1251
type fkr_email.ini | find /I "work_dir" > tmp.txt

Set file=tmp.txt

For /F "usebackq tokens=* delims=" %%i In ("%file%") Do Set var=%%i
del tmp.txt

Setlocal EnableDelayedExpansion
FOR %%a IN (%var%) DO Set d=%%a

echo %d%

start C:\Work\python\Fkr_email\fkr_email.exe 
timeout 1
start powershell.exe Get-Content %d%\email-sender.log -Wait 
