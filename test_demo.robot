*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}          https://www.iplt20.com/points-table/men
${table_row}    //tbody[@id='pointsdata']/tr

*** Test Cases ***
IPL_table
    Open Browser    ${url}    chrome
    Maximize Browser Window

    ${is_visible}=    Run Keyword And Return Status    Element Should Be Visible    //button[contains(text(),'Accept cookies')]
    Run Keyword If    ${is_visible}    Click Button    //button[contains(text(),'Accept cookies')]

    Wait Until Element Is Visible    ${table_row}    timeout=25s

    ${rows}=    Get WebElements    ${table_row}
    ${all_data}=    Create List

    FOR    ${index}    IN RANGE    1    ${len(${rows})+1}
        ${cells}=    Get WebElements    xpath=${table_row}[${index}]/td
        ${row_data}=    Create List
        FOR    ${cell}    IN    @{cells}
            ${text}=    Get Text    ${cell}
            Append To List    ${row_data}    ${text}
        END
        Append To List    ${all_data}    ${row_data}
    END

    Log To Console    ${all_data}
