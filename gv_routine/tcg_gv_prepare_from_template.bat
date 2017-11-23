::@set /P  view_name= view name:
::@set /P BASE_LABEL=BASE_LABEL:
::@echo  view name: %view_name%
::@echo BASE_LABEL: %BASE_LABEL%
::ccperl tcg_gv_prepare_from_template.pl 1mqmcapp_a310d21_gv225086_zhaoy2  1MQMCAPP_A310D21  C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\
cd /d %~dp0
ccperl tcg_gv_prepare_from_template.pl  %1 %2 %3 
