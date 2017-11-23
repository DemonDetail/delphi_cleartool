# 从ClearCase指令lscheckout的结果中提取被checkout的文件的路径
# 输入
#   1. lscheckout命令的结果文件的路径
#   2. 输出文件的路径
# 输出
#   1. 被checkout的文件的路径

my $co_raw_file = $ARGV[0];
my $co_out_file = $ARGV[1];

open(f_co_raw_file,"<",$co_raw_file) || die"cannot open the file: $co_raw_file!\n";
open(f_co_out_file,">",$co_out_file) || die"cannot open the file: $co_out_file!\n";

while (<f_co_raw_file>)
{
    #   16-Dec.15:47   fzslqx     checkout version "\blois_code_p_l\p_l\p_l_ecu\NVM\src\P_L_Nvm_Data.t55" from \main\sg7505_ctc\BR_1EWCH_A_CTC\3 (reserved)
    if(/checkout\s+version\s+"(.*)?"\s+from/)
    {
        print f_co_out_file "$1\n";
    }
    #   16-Dec.15:45   fzslqx     checkout directory version "\blois_soft_vob\Software\S_S\s_s_fault_manager\src" from \main\sg7505_ctc\BR_1EWCH_A_CTC\0 (reserved)
    elsif(/checkout\s+directory\s+version\s+"(.*)?"\s+from/)
    {
        print f_co_out_file "$1\n";
    }
    else
    {
    }
}

close f_co_raw_file;
close f_co_out_file;



