:: 用于生成review GV的checkout文件的脚本
:: 通过调用perl脚本tcg_gv_view.pl来实现
::   tcg_prepare_review_co.pl接收三个参数
::     前两个参数为view name和base label可事先固定, 
::     而第三个参数为需要view的文件列表的文件名, 在不同阶段他们不相同, 因此需要在运行该脚本前决定, 在这里为checkout文件列表

:: !!在调用该脚本前必须确保对应的checkout文件列表是最新的!
:: !!否则必须首先调用find_gvXXXXXXXX_co.bat重新生成checkout文件列表

ccperl ..\Utility\tcg_prepare_review_co.pl C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\  gv225086_co.txt review_co_gv225086.bat
