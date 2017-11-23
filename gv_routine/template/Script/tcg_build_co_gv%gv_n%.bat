:: ±àÒëcheckoutÎÄ¼ş.

FOR /F "delims=" %%I IN ('perl ..\Utility\get_src_file_name.pl gv%gv_n%_co.txt') DO set src_files=%%I

cd /d X:\%tcg_view_name%\gill_vob\6_coding
build GEN_QAC=NO %src_files%

@pause