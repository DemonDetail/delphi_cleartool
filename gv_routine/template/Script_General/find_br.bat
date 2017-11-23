
@echo off
@SET /P    _search_br=branche:
@SET /P  _search_view=VIEW:
@SET     _output=%_search_br%_br.txt

@echo view:      X:\%_search_view%
@echo view:      X:\%_search_view%                 1>%~dp0\%_output%
@echo condition: version(.../%_search_br%/LATEST)
@echo condition: version(.../%_search_br%/LATEST) 1>>%~dp0\%_output%
@echo ************************************************** 1>>%~dp0\%_output%
::@pause

@cd /d X:
@echo on
cleartool find X:\%_search_view%\blois_code_p_l -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\blois_soft_vob -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_vob       -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\hwi_vob        -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_wch_code  -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gill_dcm624_code  -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\blois_hmc_code -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%
cleartool find X:\%_search_view%\gwm_secure_vob -ver "version(.../%_search_br%/LATEST)" -print >>%~dp0\%_output%

@cd /d %~dp0
