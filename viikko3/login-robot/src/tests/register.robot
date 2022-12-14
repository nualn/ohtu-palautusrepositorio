*** Settings ***
Resource  resource.robot
Test Setup  Input  new
*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Invalid username
    
Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Invalid password


