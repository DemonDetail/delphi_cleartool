@echo off
::@SET /P  _search_view=VIEW(C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\):
::@IF "%_search_view%" == ""   set _search_view=C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\
::@FOR /F "delims=" %%I IN ('perl ..\Utility\get_gv_name.pl %_search_view%') DO set _output=%%I_co.txt

@set  _search_view=C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\
@set       _output=gv225086_co.txt

@echo view:      X:\%_search_view%
@echo view:      X:\%_search_view%      1>%~dp0\%_output%
@echo ************************************************** 1>>%~dp0\%_output%
cd /d X:\%_search_view%
cleartool lscheckout -avobs -cview 1>%~dp0\_temp\%_output%
cd /d %~dp0
ccperl ..\Utility\get_list_from_lscheckout.pl %~dp0\_temp\%_output% %~dp0\%_output%
