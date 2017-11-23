#print "hello word\n";
#$String = "SourceFile('blois_code_p_l/p_l/p_l_com/MSG/src/P_L_Cc_Bus_Fault.c',CC_TYPE = 'spec' , OWNER = 'tcbl' , CCFLAGS = ['INTROM','INTRAM','SHARE_COMMON_CODE'])";
#$String =~ /SourceFile\s*\(\s*'(.*?\/(\w*?.c))'/;
#print "file path:\t\t'$1'\n";
#print "file name:\t\t'$2'\n";

#my $cfg_file = "X:\\1EWCHAPP_A410D01\\gill_vob\\6_coding\\config_wch_etc27.py";
my $cfg_file      = $ARGV[0];
my $file_path_sorted_txt = $ARGV[1];
my $miss_file_list       = $ARGV[2];

open(config_file,"<",$cfg_file) || die"cannot open the file: $!\n";

my %Files = ();
my @all_list_not_sort = ();
my @proj_list = ();
my @c_list =();
my @s_list =();
my @h_list =();
my @t55_list =();
my @oth_lit = ();
my $file_found = 0;

while (<config_file>){
    $file_found = "NULL";
    if(/^SourceFile\s*\(\s*'(.*?\/(\w*?.c))'/)
    {
        $file_found = "c";
    }
    elsif (/AsmFile\s*\(\s*'(.*?\/(\w*?.s))'/)
    {
        $file_found = "s";
    }
    elsif (/HeaderFile\s*\(\s*'(.*?\/(\w*?.h))'/)
    {
        $file_found = "h";
    }
    elsif (/T55File\s*\(\s*'(.*?\/(\w*?.t55))'/)
    {
        $file_found = "t55";
    }
    elsif (/ProjectFile\s*\(\s*'(.*?\/(\w*?.(asc|dld|h|t55|txt|)))'/)
    {
        $file_found = "proj";
    }

    if($file_found ne "NULL")
    {
        my $file_path = $1;
        my $file = lc($2);
        
        if(exists $Files{$file})
        {
            print "!file found more than once. please check config.py:\n";
            print "    $file    $Files{$file}\n";
            print "    $file    $file_path\n";
        }
        $Files{$file} = $file_path;
        
        #replace '/' with '\' for windows.    
        my $file_path_win = $file_path;
        $file_path_win =~ s/\//\\/g;

        push @all_list_not_sort, $file_path_win;
        
        if   ($file_found eq "c")   {   push @c_list,   $file_path_win; }
        elsif($file_found eq "s")   {   push @s_list,   $file_path_win; }
        elsif($file_found eq "h")   {   push @h_list,   $file_path_win; }
        elsif($file_found eq "t55") {   push @t55_list, $file_path_win; }
        elsif($file_found eq "proj"){   push @proj_list,$file_path_win; }   
        else                        {   push @oth_list, $file_path_win; }
    }
}
close config_file;

#open(path_list,">",$file_path_txt) || die"cannot open the file: $!\n";
#foreach $path (@all_list_not_sort)  { print path_list "$path\n";}
#close path_list;

open(path_sorted_list,">",$file_path_sorted_txt) || die"cannot open the file: $!\n";
# 排序不区分大小写.
@proj_list = sort { lc($a) cmp lc($b) } @proj_list;   foreach $path (@proj_list)  {print path_sorted_list "$path\n";}
@c_list   = sort { lc($a) cmp lc($b) } @c_list;       foreach $path (@c_list)     {print path_sorted_list "$path\n";}
@s_list   = sort { lc($a) cmp lc($b) } @s_list;       foreach $path (@s_list)     {print path_sorted_list "$path\n";}
@h_list   = sort { lc($a) cmp lc($b) } @h_list;       foreach $path (@h_list)     {print path_sorted_list "$path\n";}
@t55_list = sort { lc($a) cmp lc($b) } @t55_list;     foreach $path (@t55_list)   {print path_sorted_list "$path\n";}
@oth_list = sort { lc($a) cmp lc($b) } @oth_list;     foreach $path (@oth_list)   {print path_sorted_list "$path\n";}
close path_sorted_list;

open(miss_list,">",$miss_file_list) || die"cannot open the file:$miss_file_list $!\n";

my $config_dir = "";
if($cfg_file =~ /(.*)?[\\\/][a-zA-Z0-9_]+\.py/)
{
    $config_dir = $1;
}

STDOUT->autoflush(1);
my $cnt;
foreach $path (@all_list_not_sort)  
{
    $cnt = $cnt + 1;
    if($cnt >= 888)         {   print "\>\n"; $cnt = 0; }
    elsif($cnt % 10 == 0)   {   print "\>";             }

    if(-e $config_dir."\\".$path)
    {
    }
    else
    {
         print miss_list "$path\n";
    }
}
close miss_list;


#open(file_list,">",$file_name_txt) || die"cannot open the file: $!\n";
#close file_list;