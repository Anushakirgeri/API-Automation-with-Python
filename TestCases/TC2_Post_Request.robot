*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}=    https://gorest.co.in

*** Test Cases ***
Put_CustomerRegistration
        Create Session    myssion ${base_url}
        ${body}=    Create Dictionary    id=349074   name=Vinaya Jain  email=vinaya_jain@gusikowski.test  gender=female status=active
        ${header}=   Create Dictionary    Content-Type=application/json

        ${response}=  POST On Session      myssion  /public/v2/users  json=${body}  headers=${header}
        Log To Console    ${response.status_code}
        Log To Console    ${response.content}
