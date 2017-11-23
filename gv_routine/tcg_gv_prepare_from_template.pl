use strict;
use warnings;
use File::Copy;

my $view_name  = $ARGV[0];
my $BASE_LABEL = $ARGV[1];
my $targetpath = $ARGV[2];

my $gv_n = "";

if($view_name =~ /([0-9]{6})/)
{
    $gv_n = $1;
}
else
{
    print "!error: gv number not found!\n";
    exit 0;
}
my $gv_branche = '';
my $GV_LABEL   = '';
if($view_name =~ /\w+?_gv(\d{6})_(\w+)/)   # CTC RULE: 1myucapp_a200d01_gv149459_chenj
{ 
    my $owner = $2;
    $gv_branche = 'task_'.$owner.'_gv'.$gv_n;
    $GV_LABEL   = uc($gv_branche);
}
else    # TCG RULE: task_chenj_gv136010
{
    $gv_branche = $view_name;
    $GV_LABEL   = uc($view_name);
}


#在这里使用'/'代替'\', 否则在替换root时会出现问题, ccperl会把'/gv_routine'中的'/g'当做命令.
my $gv_template_root = './template';
my $gv_working_root  = $targetpath.'./GV'.$gv_n;

my %keywords = ();
$keywords{'%gv_n%'}                     = $gv_n;
$keywords{'%BASE_APP_LABEL%'}           = $BASE_LABEL;
$keywords{'%tcg_view_name%'}            = $view_name;
$keywords{'%gv_branche%'}               = $gv_branche;
$keywords{'%gv_label%'}                 = $GV_LABEL;
$keywords{'%BASE_CHECK_RESULT_PATH%'}   = "C:\\Users\\fzslqx\\Documents\\Projects\\BASE_CHECK_RESULT";
$keywords{'%cmd_BeyondCompare%'}        = "\"C:\\Program Files (x86)\\Beyond Compare 3\\BCompare.exe\"";
$keywords{'%cmd_NotePadpp%'}            = "\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\"";

my @dirs = ();
my @files = ();

# Step  1:  Analyse template directory structure
#   get all dirs and files list.
(my $ref_dirs, my $ref_files) = get_element_under_dir_recur($gv_template_root);

if( !(-e $gv_working_root) )
{
    print "---mkdir $gv_working_root\n";
    mkdir $gv_working_root;
}

print "\ndirs:\n";
foreach my $tmp_dir (sort @$ref_dirs)    
{ 
    print "    $tmp_dir\n"; 
    my $new_dir = $tmp_dir;
    
    print "$gv_template_root\n";
    $new_dir =~ s/$gv_template_root/$gv_working_root/g;
    foreach my $m_key (keys %keywords)
    {
        $new_dir =~ s/$m_key/$keywords{$m_key}/g;
    } 
    
    if( !(-e $new_dir) )
    {
        print "---mkdir $new_dir\n";
        mkdir $new_dir;
    }

    push @dirs, $new_dir;
    print " -> $new_dir\n\n";
}

print "\nfiles:\n";
foreach my $tmp_file (@$ref_files)  
{ 
    print "    $tmp_file\n";
    my $new_file = $tmp_file;
    
    $new_file =~ s/$gv_template_root/$gv_working_root/g;
    foreach my $m_key (keys %keywords)
    {
        $new_file     =~ s/$m_key/$keywords{$m_key}/g;
    } 

    copy($tmp_file, $new_file) or die "Copy failed: $!";
    
    print " -> $new_file\n";
    if($new_file =~ /\.(bat|txt|cfg)$/)
    {
        print ">>>>>>relpace, $new_file\n";
        my $file_context = read_file($new_file);
        foreach my $m_key (keys %keywords)
        {
            $file_context =~ s/$m_key/$keywords{$m_key}/g;
        } 
        write_file($new_file, $file_context);
    }

    push @files, $new_file;
    
}

# 递归分析一个目录, 分类找出其中的"文件夹"和"文件".
sub get_element_under_dir_recur
{
    my $top_dir = $_[0];
    my @all_dirs  = ();
    my @all_files = ();
    my @serach_dirs = ();   # 待搜索的子目录
    my $ref_dirs  = 0;
    my $ref_files = 0;
    
    push @serach_dirs, $top_dir;
    while( scalar @serach_dirs != 0 )
    {
        my $dir = pop @serach_dirs;
        ($ref_dirs, $ref_files) = get_element_under_dir($dir);
        push @all_dirs,    @$ref_dirs;
        push @serach_dirs, @$ref_dirs;
        push @all_files,  @$ref_files;
        
        @$ref_dirs  = 0;
        @$ref_files = 0;
        
        #print "got :\n";
        #print "    dirs:   @all_dirs \n";
        #print "    files:  @all_files \n"; 
        #print "    search: @serach_dirs \n"; 
    }
    
    return (\@all_dirs, \@all_files);
}

# 分析一个目录, 分类找出其中的"文件夹"和"文件", 不递归分析子目录.
sub get_element_under_dir
{
    my $dir = $_[0];
    
    #print "call :\t\t$dir \n";
    my @dirs  = ();
    my @files = ();
    
    opendir(f_dir, $dir) or die $!;
    while (my $element = readdir(f_dir)) 
    {
        # Use a regular expression to ignore files beginning with a period
        next if ($element =~ m/^\./);
        
        my $element_full_path = $dir.'\\'.$element;
        
        if(-d $element_full_path)
        {
            #print "    find a dir:   $element\n";
            push @dirs, $element_full_path;
        }
        elsif(-f $element_full_path)
        {
            #print "    find a file:  $element\n";
            push @files, $element_full_path;
        }
        else
        {
        }
    }
    close f_dir;  
   
    return (\@dirs, \@files);
}

sub read_file {
    my ($filename) = @_;
 
    open(f_in, '<', $filename) or die "Could not open '$filename' for reading $!";
    local $/ = undef;   #将分割符 '$/' 由默认的换行符改成undef这样才能一次性读出所有文本.
    my $all = <f_in>;
    close f_in;
 
    return $all;
}
 
sub write_file {
    my ($filename, $content) = @_;
 
    open( f_out, '>', $filename) or die "Could not open '$filename' for writing $!";
    print f_out $content;
    close f_out;
 
    return;
}