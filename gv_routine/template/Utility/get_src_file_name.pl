# tcg平台下, 从文件列表获取.c文件的文件名
# 输入:
# 1. 文件列表文件
#   X:\task_chenj_gv143293\gill_vob\6_coding\src\p_l\p_l_com\p_l_cc\p_l_cc_j1939\src\p_l_cc_j1939_rx_pdu255.c
#                                                                                    p_l_cc_j1939_rx_pdu255.c                 


use strict;
use warnings;

my $co_file_list = $ARGV[0];
my @src_files       = ();
my $src_files_str   = "";


open(f_co_file_list,"<",$co_file_list) || die"cannot open the file: $co_file_list!\n";

while (<f_co_file_list>)
{
    # X:\task_chenj_gv143293\gill_vob\6_coding\src\p_l\p_l_com\p_l_cc\p_l_cc_j1939\src\p_l_cc_j1939_rx_pdu255.c
    if(/\s*?X:[\\\/](\w+)[\\\/](\w+?[\\\/])+(\w+\.c)/)
    {
        my $src_file    = $3;
        push @src_files, $src_file;
        $src_files_str = $src_files_str." ".$src_file;
    }
}
close f_co_file_list;

print $src_files_str;

