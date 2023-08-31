# Alias
Set-Alias less "$env:USERPROFILE\scoop\apps\git\2.38.1.windows.1\usr\bin\less.exe"

#Set-PoshPrompt -Theme paradox
#oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH/gruvbox.omp.json" | Invoke-Expression
oh-my-posh init pwsh --config "$env:USERPROFILE\.config\powershell\irs.omp.json" | Invoke-Expression

# Terminal Icons
Import-Module -Name Terminal-Icons