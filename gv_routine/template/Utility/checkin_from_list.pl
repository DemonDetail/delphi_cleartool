# 通过文件列表, 生成用于并行checkin源文件到ClearCase的脚本.
# 每个待checkin的文件首先对于一个独立的脚本.
# 另有一个总的脚本用于以并行方式调用各个checkin脚本.
# 输入
#   1. 待checkin的文件的列表, 实际就是VIEW的checkout的文件列表, 
#      所有路径为"绝对路径", 必须以"X:\"开头.

my $file_list   = $ARGV[0];
my $comment_cus = $ARGV[1];

my $view_name   = "";
my $child_bat   = "";
my $root_dir  = "";
my $merge_log_txt = "";
my $log_file_list = "";

# start cleartool checkin -keep -c "Int 1EWCHAPP_A500P02 150109 15:28" X:\1EWCHAPP_A500P02\gill_vob\6_coding\src\appli\rtw\src\mul_u32_u32_u32_sr26.c
my $child_bat_tmp1 = "cleartool checkin -keep -c %comment% %file_path% > %log_name% 2>&1\n";
my $child_bat_tmp2 = "exit 0\n";


open(f_file_list,"<",$file_list) || die"cannot open the file: $file_list!\n";

my $file_num = 0;

while (<f_file_list>)
{
    my $file_path = "";
    my $file_name = "";
    
    
    if($_ =~ /(X:\\([a-zA-Z_0-9]+)\\.*\\([a-zA-Z_0-9\.]+))\s*$/)
    {
        $file_num += 1;
        $file_path = $1;
        $file_name = $3;
    
        # 从文件列表的内容获取VIEW的名字, 从而生成checkin脚本根目录的名字.
        if($view_name eq "")
        {
            $view_name   = $2;
            my $dir_name = $view_name."_checkin";
            if( !(-e $dir_name) )
            {
                mkdir $dir_name or die;
            }
               $root_dir       = ".\\".$dir_name."\\";
            my $parent_bat     = $view_name."_checkin_all.bat";
            my $parent_txt     = $view_name."_checkin_all.txt";
            my $merge_log_bat  = $view_name."_checkin_merge_log.bat";
               $merge_log_txt  = $view_name."_checkin_all_error.log";
               $log_file_list  = $view_name."_checkin_err_files.list";
            open(f_parent_bat,">",$root_dir.$parent_bat) || die"cannot open the file: $root_dir.$parent_bat!\n";
            open(f_parent_txt,">",$root_dir.$parent_txt) || die"cannot open the file: $root_dir.$parent_txt!\n";
            open(f_merge_log_bat,">",$root_dir.$merge_log_bat) || die"cannot open the file: $root_dir.$merge_log_bat!\n";
            open(f_log_file_list,">",$root_dir.$log_file_list) || die"cannot open the file: $root_dir.$log_file_list!\n";
        }
        elsif($view_name eq $2)
        {
            # view name is right, all equal.
        }
        else
        {
            print "!err: view name not equal\n";
            print " former view: $view_name\n";
            print " new    view: $1\n";
            exit;
        }
    }
    
    # X:\1EWCHAPP_A500P02\gill_vob\6_coding\src\appli\rtw\src\mul_u32_u32_u32_sr26.c
    my $tmp = $file_path;
    $tmp =~ s/:\\/--/g;
    $tmp =~ s/\\/-/g;
    my $log_name        = "__".$file_num."_checkin_".$file_name.".log";
    my $child_bat_name  =  "_".$file_num."_checkin_".$file_name.".bat";
    $child_bat = $root_dir.$child_bat_name;
    open(f_child_bat,">",$child_bat) || die"cannot open the file: $child_bat!\n";
    
    my $child_bat_context = $child_bat_tmp1;
    my $comment   = "\"".$comment_cus." "."checkin $file_path"."\"";
    $child_bat_context =~ s/%comment%/$comment/g;
    $child_bat_context =~ s/%file_path%/$file_path/g;
    $child_bat_context =~ s/%log_name%/$log_name/g;
    
    print f_child_bat  "$child_bat_context";
    print f_child_bat  "$child_bat_tmp2";
    close f_child_bat;
    
    print f_parent_txt      "$child_bat_context";
    print f_parent_bat      "start /i /min $child_bat_name\n";
    print f_log_file_list   "$log_name\n";
}

print f_merge_log_bat "ccperl ..\\..\\Utility\\merge_file_context.pl $merge_log_txt $log_file_list\n";

close f_file_list;
close f_parent_bat;
close f_log_file_list;
close f_merge_log_bat;


















