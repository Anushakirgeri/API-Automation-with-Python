*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}     https://gorest.co.in
${user}    2042

*** Test Cases ***
GetWeatherInfo
    Create Session  myssion    ${base_url}
    ${response}=    GET On Session        myssion  /public/v2/users/${user}
#VALIDATIONS
    ${status_code}=   Convert To String     ${response.status_code}
    Should Be Equal    ${status_code}       200
    Log To Console     ${response.content}

    ${body}=   Convert To String  ${response.content}
    Should Contain    ${body}   active

    ${contentType_Value}=   Get From Dictionary    ${response.headers}      Content-Type
    Should Be Equal    ${contentType_Value}     application/json; charset=utf-8