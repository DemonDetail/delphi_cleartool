:: ±àÒëcheckoutÎÄ¼þ.

FOR /F "delims=" %%I IN ('perl ..\Utility\get_src_file_name.pl gv225086_co.txt') DO set src_files=%%I

cd /d X:\C:\D\Project\tool_proj\1mqmcapp_a310d21_gv225086_zhaoy2\\gill_vob\6_coding
build GEN_QAC=NO %src_files%

@pause