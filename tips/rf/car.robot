*** Settings ***
Library           Selenium2Library    implicit_wait=5
Library           DatabaseLibrary
Library           MyLibrary

*** Test Cases ***
SalesWhole
    open browser    http://car.waysdata.com/    CHROME
    maximize browser window
    input text    css=.el-form-item:nth-child(1) .el-input__inner    test
    input text    css=.el-form-item:nth-child(2) .el-input__inner    ways123
    click button    css=#app > div > div.main > div > div > div.achieves > form > div.el-form-item.button > div > button
    click element    css=#modules > table > tbody > tr:nth-child(1) > td:nth-child(1) > a
    title should be    销量分析-整体市场
    click element    css=#source > a
    click element    link=批发量
    sleep    3
    ${websale}    get text    css=#summary > tbody > tr > td:nth-child(1) > p
    log many    页面显示：    ${websale}
    Connect To Database Using Custom Params    cx_Oracle    'STRIDE','stride#96','172.16.1.37:1521/DBFM'
    ${datasale}    query    select to_char(sum(t.bq_sales),'fm999,999,999,999') from fdm_state_sales_sub_model t where t.data_type_id=2 and t.ym=(select max(ym) from fdm_state_sales_sub_model where data_type_id=2)
    log many    数据库查询：    ${datasale}[0][0]
    Should Be Equal    ${websale}    ${datasale}[0][0]
    close browser

SalesManf
    open browser    http://car.waysdata.com    CHROME
    maximize browser window
    input text    css=.el-form-item:nth-child(1) .el-input__inner    test
    input text    css=.el-form-item:nth-child(2) .el-input__inner    ways123
    click button    css=#app > div > div.main > div > div > div.achieves > form > div.el-form-item.button > div > button    #提交表单
    click element    css=#modules > table > tbody > tr:nth-child(1) > td:nth-child(1) > a    #点击销量模块
    click element    link=厂商市场    #点击厂商市场
    title should be    销量分析-厂商市场
    click element    css=#source > a
    click element    link=KP-终端销量
    click element    css=#selectManf > a
    click element    link=东风日产
    sleep    3
    ${websale}    get text    css=#summary > tbody > tr > td:nth-child(1) > p
    log many    页面显示：    ${websale}
    Connect To Database Using Custom Params    cx_Oracle    'STRIDE','stride#96','172.16.1.37:1521/DBFM'
    ${datasale}    query    select to_char(sum(t.bq_sales), 'fm999,999,999,999') sale from fdm_state_sales_sub_model t left join dm_sub_model m on m.sub_model_id = t.sub_model_id left join dm_manf f on f.manf_id = m.manf_id where t.data_type_id = 6 and t.ym =(select max(ym) from fdm_state_sales_sub_model where data_type_id = 6) and f.manf_name = '东风日产'
    log many    数据库查询：    ${datasale}[0][0]
    Should Be Equal    ${websale}    ${datasale}[0][0]
    close browser

Myemil
    ${emailist}    create list    yuejing@way-s.cn    cmssystem@way-s.cn
    ${subject}    Set Variable    RF主题
    ${contents}    create list    Dear all    RF正文
    ${attachment}    create list    C://Users//yuejing//Desktop//AutoTest//InterfaceRun.py    C://Users//yuejing//Desktop//AutoTest//UiRun.py
    sendeml    ${emailist}    ${subject}    ${contents}    ${attachment}
