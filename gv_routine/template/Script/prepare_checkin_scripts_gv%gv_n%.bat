:: 用于生成checkin所有checkout的文件, 文件夹的脚本, 所有脚本放入一个统一的文件夹内.
:: 通过调用perl脚本checkin_from_list.pl来实现
::   checkin_from_list.pl.pl接收两个参数
::     1. checkout文件列表, 所有路径以X:\开头 
::     2. checkin的comment, 所有文件都使用这个comment.

:: !!在调用该脚本前必须确保对应的co文件列表是最新的!
:: !!否则必须首先调用find_gvXXXXXXXX_co.bat重新生成checkout文件列表

ccperl ..\Utility\checkin_from_list.pl gv%gv_n%_co.txt GV%gv_n%