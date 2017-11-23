::cleartool mkview -tag   myviewv   \\CNSHGCTC-AP07\views\ASIA\bjq5dl\myview.vws
::cleartool lsview 
::cleartool startview
cleartool lsview > %2
@echo cleartool mkview -tag   %1   %3%1.vws
cleartool mkview -tag   %1   %3%1.vws
::@pause