###
##
## Jake Hardy 


## File input
function file_input{

$SEL = Select-String -Path $MY_CONFIG_FILE -Pattern "ResX=3840"  # Find the string

if ($SEL -ne $null)
{
$current = '3840'
}
else{
$current = '1920'
}
return $current
}
## End File input


## User input
function user_input{
$acceptable_inputs = 'y', 'n', 'q'

$user_input = 'x'

while ($acceptable_inputs -NotContains $user_input){  # Enforce validity of inputs

Write-Host "*****************************"

if ($current -eq '3840'){ 
Write-Host "Resolution is set to 2 player"
}
else{
Write-Host "Resolution is set to single player"
}

Write-Host "Would you like to alter resolution?"
$user_input = Read-Host -Prompt "Y, N, Q".ToLower()

if($acceptable_inputs -NotContains $user_input){
Write-Host "Does not compute"
Write-Host "Enter 'q'  to quit"
continue
}
} 
return $user_input
}
## End User input


## Resolution change
function resolution_change{

if ($current -eq '1920'){
$newconfig = $config -replace 'Fullscreen=True', 'Fullscreen=False' -replace 'Borderless=False', 'Borderless=True' -replace $current, '3840'
}
else{
$newconfig = $config -replace 'Fullscreen=False', 'Fullscreen=True' -replace 'Borderless=True', 'Borderless=False' -replace $current, '1920'
}

Out-File -FilePath $MY_CONFIG_FILE -InputObject  $newconfig 
}
## End Resolution change


## Launch game
function launch_game{
Write-Host "Launching game!"
Start-Process -FilePath $MY_RL_SHORTCUT
}
## End Launch game


#CONSTANTS
$MY_CONFIG_FILE = 'C:\Users\Jake\Documents\My Games\Rocket League\TAGame\Config\TASystemSettings.ini'
$MY_RL_SHORTCUT = 'C:\Users\Jake\Desktop\Rocket League.url'

# MAIN
$current = file_input
$user_input = user_input
  
if ($user_input -eq "q"){  #Quit
exit
}

elseif($user_input -eq "n"){  #No resolution_change
Write-Host "Settings were not changed"
launch_game
exit
}

elseif($user_input -eq "y"){
$config = Get-Content $MY_CONFIG_FILE -Raw 
resolution_change
Write-Host "Settings have been changed!"
launch_game
exit
}
