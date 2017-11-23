@echo off
::@SET /P    _search_br=branche:
::@SET /P  _search_view=VIEW:
@SET     _search_br=%1
@SET     _search_view=%2
@SET     _outpath=%3
@SET     _output=%_search_label%_lb.txt

@echo view:      X:\%_search_view%
::@echo view:      X:\%_search_view%        1>%~dp0\%_output%
@echo condition: lbtype(%_search_label%)
::@echo condition: lbtype(%_search_label%) 1>>%~dp0\%_output%
::@echo ************************************************** 1>>%~dp0\%_output%
::@pause

@cd /d X:
@echo on
cleartool find X:\%_search_view%\blois_code_p_l -ver "lbtype(%_search_label%)" -print >%_outpath%\%_output%
cleartool find X:\%_search_view%\blois_soft_vob -ver "lbtype(%_search_label%)" -print >>%_outpath%\%_output%
cleartool find X:\%_search_view%\euro5_vob      -ver "lbtype(%_search_label%)" -print >>%_outpath%\%_output%
cleartool find X:\%_search_view%\gill_vob       -ver "lbtype(%_search_label%)" -print >>%_outpath%\%_output%
cleartool find X:\%_search_view%\hwi_vob        -ver "lbtype(%_search_label%)" -print >>%_outpath%\%_output%
cleartool find X:\%_search_view%\gill_dcm624_code  -ver "lbtype(%_search_label%)" -print >>%_outpath%\%_output%
cleartool find X:\%_search_view%\blois_hmc_code -ver "lbtype(%_search_label%)" -print >>%_outpath%\%_output%
cleartool find X:\%_search_view%\gwm_secure_vob -ver "lbtype(%_search_label%)" -print >>%_outpath%\%_output%

::cleartool find X:\%_search_view%\blois_code_p_l -ver "lbtype(%_search_label%)" -print >%~dp0\%_output%
::cleartool find X:\%_search_view%\blois_soft_vob -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
::cleartool find X:\%_search_view%\euro5_vob      -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
::cleartool find X:\%_search_view%\gill_vob       -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
::cleartool find X:\%_search_view%\hwi_vob        -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
::cleartool find X:\%_search_view%\gill_dcm624_code  -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
::cleartool find X:\%_search_view%\blois_hmc_code -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
::cleartool find X:\%_search_view%\gwm_secure_vob -ver "lbtype(%_search_label%)" -print >>%~dp0\%_output%
@cd /d %~dp0
@pause