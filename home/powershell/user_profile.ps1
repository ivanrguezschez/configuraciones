#oh-my-posh init pwsh | Invoke-Expression

# Set-PoshPrompt -Theme gruvbox
#oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH/gruvbox.omp.json" | Invoke-Expression
oh-my-posh init pwsh --config "$env:USERPROFILE/.config/powershell/irs.omp.json" | Invoke-Expression

# Terminal Icons
Import-Module -Name Terminal-Icons