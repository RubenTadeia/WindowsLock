cls
$Path = "C:\Program Files (x86)\Google\Chrome\Application\"
Start-Process -WorkingDirectory $Path chrome.exe -WindowStyle Maximized

py C:\Ruben\NOS\powershell\lock-PC\pythonKey.py

$y = Get-Content C:\Ruben\NOS\powershell\lock-PC\text.txt -First 1

write-host($y)

if($y -eq "1"){
   rundll32.exe user32.dll,LockWorkStation
}else {
   write-host("You hacked my computer...")
}