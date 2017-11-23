# 生成复审GV的脚本 #
# 输入:
# 1. gv的view的名字
# 2. gv的base的LABEL
#       即GV是基于那个base开发的.
# 3. 需要被review的文件的checkout文件列表
# 4. 输出文件名
# 输出:
#       用于复审GV的bat文件.


use strict;
use warnings;

my $view_name    = $ARGV[0];
my $base_lb      = $ARGV[1];
my $gv_file_list = $ARGV[2];
my $output       = $ARGV[3];

my $file_num = 0;
my %Files = ();

my $gv_num_from_file = "file";
my $gv_num_from_view = "view";
if($gv_file_list =~ /gv([0-9]{6})/) {   $gv_num_from_file = $1; }
if($view_name    =~ /gv([0-9]{6})/) {   $gv_num_from_view = $1; }

if($gv_num_from_file eq $gv_num_from_view)
{
    print "view name    = $view_name\n";
    print "label        = $base_lb\n";
    print "output name  = $output\n";
}
else
{   
    print "$gv_num_from_file\n";
    print "$gv_num_from_view\n";
    print "error!    gv number diff between view name and gv_file_list\n";
}

open(f_gv_file_list,"<",$gv_file_list) || die"cannot open the file: $gv_file_list!\n";
open(f_output,">",$output) || die"cannot open the file: $output!\n";
while (<f_gv_file_list>)
{
#   \gill_vob\6_coding\config_wch_etc27.py@@\main\sg7505_ctc\BR_1EWCH_A_CTC\task_zhouj_gv140370\1
#   匹配第一个'\'或'/', 以适应不同的路径: 'Z:\' 'Y:\' 'X:\task_chenj_gvXXXXXX\'
    if(/\s*?(.+)/)
    {
        my $path = $1;
        
        #将不同形式的路径统一替换为"X:\view_name\"类型的路径.
        $path =~ s/^[\\\/]/X:\\$view_name\\/;           #   \gill_vob\...   -> X:\task_chenj_gvXXXXXX\gill_vob
        $path =~ s/^\.[\\\/]/X:\\$view_name\\/;         #  .\gill_vob\...   -> X:\task_chenj_gvXXXXXX\gill_vob
        $path =~ s/^[A-WYZ]:[\\\/]/X:\\$view_name\\/;   # Y:\gill_vob\...   -> X:\task_chenj_gvXXXXXX\gill_vob
        
        $file_num = $file_num + 1;
        
        print "$path\n";
        print f_output "cleartool diff -g $path\@\@\\$base_lb  $path\n";
        print f_output"pause\n";
    }
}
print "total: $file_num\n";

close f_gv_file_list;
close f_output;