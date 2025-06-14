@echo off
echo Generating detailed file list...

REM Create timestamp for filename
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "timestamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"

REM Generate detailed file list as CSV
echo "Path","Name","Size_Bytes","Date_Modified","Time_Modified","Attributes" > "FileList_%timestamp%.csv"
for /f "tokens=*" %%i in ('dir /s /a /-c /q') do (
    echo Processing: %%i
)

REM Better approach - use forfiles for structured output
echo "Full_Path","Filename","Size_Bytes","Date_Modified","Time_Modified","Is_Directory" > "FileList_%timestamp%.csv"
forfiles /s /m *.* /c "cmd /c echo @path,@file,@fsize,@fdate,@ftime,@isdir" >> "FileList_%timestamp%.csv" 2>nul

REM Also create a detailed text report
echo File Listing Report - Generated on %date% at %time% > "FileList_%timestamp%.txt"
echo ================================================== >> "FileList_%timestamp%.txt"
echo. >> "FileList_%timestamp%.txt"
dir /s /a /q /t:w >> "FileList_%timestamp%.txt"

REM Create JSON format (requires PowerShell)
powershell -Command "Get-ChildItem -Recurse -Force | Select-Object FullName, Name, Length, LastWriteTime, CreationTime, Attributes | ConvertTo-Json" > "FileList_%timestamp%.json" 2>nul

echo.
echo File listing complete! Generated files:
echo - FileList_%timestamp%.csv (CSV format)
echo - FileList_%timestamp%.txt (Detailed text report) 
echo - FileList_%timestamp%.json (JSON format)
pause