Rocket league co-op is locked to the max resolution of one monitor by default.

Using this script you can extend the resolution & make changes to other settings that permit Rocket league to span the X resolution of however many monitors you require.

You must change your rocket league settings to display co-op mode split vertically.

# TO setup -- 
**Powershell**

1. Change the variable values to match your filesystem layout accordingly;\
$MY_CONFIG_FILE - This is your TASystemSettings.ini file.\
$MY_RL_SHORTCUT - This is a desktop shortcut file.

2. Create a new desktop shortcut and browse to the location of the script.
3. Give your shortcut a friendly name.
4. Right click the shortcut, hit properties.
5. In the 'Target:' field, insert the following BEFORE the existing filepath;\
powershell.exe -ExecutionPolicy Bypass -File

6. Hit OK

## Use the desktop shortcut to run



# TO RUN -- 
**Python**

1. Change the variable value to match your filesystem layout accordingly;\
myrocketleaguefile - This is your TASystemSettings.ini file.

You also must have python interpreter installed to run this file.
