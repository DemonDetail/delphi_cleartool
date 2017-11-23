rem 用于从TCG项目文件config.py获取源文件列表
rem 通过调用perl脚本tcg_get_list_from_config.pl来实现

::set /P _view_name=                 view name:
::set /P _file_list=     output file list name:
::set /P _miss_list=output miss file list name:

set _file_list=config_list_gv225086.txt
set _miss_list=config_list_gv225086_miss.txt
set _view_name=C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\

@echo view:      X:\%_view_name%

ccperl ..\Utility\tcg_get_list_from_config.pl X:\%_view_name%\gill_vob\6_coding\config.py %_file_list% %_miss_list%

@copy %_file_list%    X:\%_view_name%\gill_vob\6_coding\%_file_list%
@copy %_file_list%    ..\_SI\%_file_list%
@copy %_miss_list%    X:\%_view_name%\gill_vob\6_coding\%_miss_list%
@copy %_miss_list%    ..\_SI\%_miss_list%