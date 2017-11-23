
@echo off
::@SET /P    _search_br=LABEL(task_zhaoy2_gv225086):
::@SET /P  _search_view=VIEW(C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\):
::@IF "%_search_br%" == "" set _search_br=task_zhaoy2_gv225086
::@IF "%_search_view%" == ""   set _search_view=C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\
::@FOR /F "delims=" %%I IN ('perl ..\Utility\get_gv_name.pl %_search_view%') DO set _output=%%I_br.txt

@set  _search_view=C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\
@set    _search_br=task_zhaoy2_gv225086
@set       _output=gv225086_br.txt

@echo view:      X:\%_search_view%
@echo view:      X:\%_search_view%                 1>%~dp0\%_output%
@echo condition: version(.../%_search_br%/LATEST)
@echo condition: version(.../%_search_br%/LATEST) 1>>%~dp0\%_output%
@echo ************************************************** 1>>%~dp0\%_output%
::@pause

@cd /d X:
@echo on
cleartool find X:\%_search_view%\blois_code_p_l   -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\blois_soft_vob   -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\euro5_vob        -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_vob         -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\hwi_vob          -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_wch_code    -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_dcm624_code -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\blois_hmc_code   -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gwm_secure_vob   -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
@cd /d %~dp0
