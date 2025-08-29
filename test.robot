*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    BuiltIn
*** Variables ***
${url}    https://www.iplt20.com/points-table/men
${table}    //table[@class="ih-td-tab"]
${table_row}    //tbody[@id='pointsdata']/tr
${table_data}    //tbody[@id='pointsdata']/tr/td
${Accept_button}    //button[contains(text(),'Accept cookies')]
*** Test Cases ***
IPL_table
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Sleep    10
    ${is_visible}=    Run Keyword And Return Status    Element Should Be Visible    ${Accept_button}
    Run Keyword If    ${is_visible}    Click Button    ${Accept_button}
    Sleep    20
    Wait Until Element Is Visible    ${table_row}    timeout=25s
    
    ${table_data}=    Create List    
    ${rows_count}    Get Element Count    //tbody[@id='pointsdata']/tr
    FOR    ${i}    IN RANGE    1    ${rows_count}+1
        ${column_count}    Get Element Count    //tbody[@id='pointsdata']/tr[${i}]/td
        ${rows_list}=    Create List    
        FOR    ${j}    IN RANGE    1    ${column_count}+1
            ${column_val}    Get Text    //tbody[@id='pointsdata']/tr[${i}]/td[${j}]
            Append To List    ${rows_list}    ${column_val}
        END
        Append To List    ${table_data}    ${rows_list}
    END


    ${won_dict}=    Create Dictionary    
    ${count_list}    Get Length    ${table_data}
    FOR    ${l1}    IN RANGE    0    ${count_list}
        ${rows}=    Get From List    ${table_data}    ${l1}
        ${team}=    Get From List    ${rows}    2
        ${num_won}=    Get From List    ${rows}    -1
        ${split_text}=    Evaluate    '''${num_won}'''.split('\\n')
        ${count_w}=    Evaluate    ${split_text}.count('W')
        Set To Dictionary    ${won_dict}    ${team}=${count_w}
    END

    Log To Console    ${won_dict}
    
    ${Dict_val}=    Evaluate    max(${won_dict}.values())

    ${max_teams}=    Create Dictionary
    FOR    ${k}    ${v}    IN    &{won_dict}
        Run Keyword If    ${v} == ${Dict_val}    Set To Dictionary    ${max_teams}    ${k}=${v}
    END

    Log To Console    ${max_teams}
