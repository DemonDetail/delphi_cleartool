:: 用于生成review GV的label文件的脚本
:: 通过调用perl脚本tcg_gv_view.pl来实现
::   tcg_prepare_review_lb.pl接收三个参数
::     前两个参数为view name和base label可事先固定, 
::     而第三个参数为需要view的文件列表的文件名, 在不同阶段他们不相同, 因此需要在运行该脚本前决定, 在这里为label文件列表

:: !!在调用该脚本前必须确保对应的label文件列表是最新的!
:: !!否则必须首先调用find_gvXXXXXXXX_lb.bat重新生成label文件列表

ccperl ..\Utility\tcg_prepare_review_lb.pl C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\  gv225086_lb.txt review_lb_gv225086.bat