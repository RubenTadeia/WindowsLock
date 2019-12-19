cls
$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
$process = Start-Process -FilePath 'http://www.google.com' -PassThru
write-host($process)
$Path = "C:\Program Files (x86)\Google\Chrome\Application\"
Start-Process -WorkingDirectory $Path chrome.exe -WindowStyle Maximized

python $scriptPath\pythonKey.py $scriptPath

$y = Get-Content $scriptPath\doNotDeleteMe.txt -First 1

if($y -eq "1"){
   rundll32.exe user32.dll,LockWorkStation
}else {
   write-host("You hacked my computer...")
}