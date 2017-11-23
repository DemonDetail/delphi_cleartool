@echo off
::@SET /P _search_label=LABEL(%gv_label%):
::@SET /P  _search_view=VIEW(%tcg_view_name%):
::@IF "%_search_label%" == "" set _search_label=%gv_label%
::@IF "%_search_view%" == ""   set _search_view=%tcg_view_name%
::@FOR /F "delims=" %%I IN ('perl ..\Utility\get_gv_name.pl %_search_view%') DO set _output=%%I_lb.txt

@set  _search_view=%tcg_view_name%
@set _search_label=%gv_label%
@set       _output=gv%gv_n%_lb.txt

@echo view:      X:\%_search_view%
@echo view:      X:\%_search_view%        1>%~dp0\%_output%
@echo condition: lbtype(%_search_label%)
@echo condition: lbtype(%_search_label%) 1>>%~dp0\%_output%
@echo ************************************************** 1>>%~dp0\%_output%
::@pause

@cd /d X:
@echo on
cleartool find X:\%_search_view%\blois_code_p_l    -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\blois_soft_vob    -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\euro5_vob         -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_vob          -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\hwi_vob           -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_wch_code     -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_dcm624_code  -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%                                                                                     
cleartool find X:\%_search_view%\blois_hmc_code    -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gwm_secure_vob    -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
@cd /d %~dp0