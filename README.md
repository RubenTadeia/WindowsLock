# WindowsLock

Shortcut for powershell in windows WIN + X then I or A (for elevated privileges)

Considering python 3.8+

Install python open cv

Install pylint
    - C:/Python38/python.exe -m pip install -U pylint --user

Set an alias to the powershell
    - New-Alias lockme C:\Ruben\GitHub\WindowsLock\doNotStealMe.ps1

To allow scripts to be run from powershell
    -  Set-ExecutionPolicy RemoteSigned 