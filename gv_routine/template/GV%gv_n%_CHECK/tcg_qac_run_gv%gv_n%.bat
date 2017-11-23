cd /d X:\%tcg_view_name%\gill_vob\6_coding

@ECHO OFF

rem : Set the DOS title bar to show what GV we are building within.
for /F %%d in ('cleartool pwv -short') do title %%d - Command is: %*

echo Set Path...
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_cots_tool_vob\\python\\Python26/; $_ =~ s/\w{1}\://; print $_;"') do set PYTHON=%%d
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_misc_tool_vob\\tools\\python\\site-packages/; $_ =~ s/\w{1}\://; print $_;"') do set PYTHONPATH=%%d
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_misc_tool_vob\\tools\\build_scripts/; $_ =~ s/\w{1}\://; print $_;"') do set PYTHONPATH=%PYTHONPATH%;%%d
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_misc_tool_vob\\tools\\python\\site-packages\\scons-2.2.0\\Scripts/; $_ =~ s/\w{1}\://; print $_;"') do set PYTHONSCRIPTS=%%d
for /F %%d in ('perl -e "$_ =`cd`; chomp $_; $_ =~ s/\w{1}\://; print $_;"') do set PYTHONPATH=%PYTHONPATH%;%%d
set PATH=%PYTHONSCRIPTS%;%PYTHON%;%PATH%
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_cots_tool_vob\\gnu/; $_ =~ s/\w{1}\://; print $_;"') do set CTAGSPATH=%%d
set PATH=%CTAGSPATH%;%PATH%
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_misc_tool_vob\\tools\\autocode/; $_ =~ s/\w{1}\://; print $_;"') do set AUTOCODEPATH=%%d
set PATH=%AUTOCODEPATH%;%PATH%
set PYTHONPATH=%PYTHONPATH%;%AUTOCODEPATH%
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_cots_tool_vob\\perl\\perl\\bin\\/; $_ =~ s/\w{1}\://; print $_;"') do set PERLPATH=%%d
set PATH=%PERLPATH%;%PATH%
for /F %%d in ('perl -e "$_ =`cd`; $_ =~ s/\\gill_vob\\\d_coding/\\tcg_misc_tool_vob\\tools\\python\\site-packages\\scons-2.2.0/; $_ =~ s/\w{1}\://; print $_;"') do set SCONS_LIB_DIR=%%d
echo Path Set Done.

echo Run Quick QAC...
python ..\..\tcg_misc_tool_vob\sw_team_leader_tools\qa.py > gv%gv_n%_quick_qac_result.txt
echo Quick Qac Done.

copy gv%gv_n%_quick_qac_result.txt %~dp0\_temp\gv%gv_n%_quick_qac_result.txt