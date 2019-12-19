cls
$Path = "C:\Program Files (x86)\Google\Chrome\Application\"
Start-Process -WorkingDirectory $Path chrome.exe -WindowStyle Maximized

python C:\Ruben\NOS\WindowsLock\pythonKey.py

$y = Get-Content C:\Ruben\NOS\WindowsLock\doNotDeleteMe.txt -First 1

write-host($y)

if($y -eq "1"){
   rundll32.exe user32.dll,LockWorkStation
}else {
   write-host("You hacked my computer...")
}