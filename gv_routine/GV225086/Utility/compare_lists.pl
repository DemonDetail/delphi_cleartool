my $list_1  = $ARGV[0];
my $list_2  = $ARGV[1];
my $str_1   = $ARGV[2];
my $str_2   = $ARGV[3];

my %cmp_dic = ();

use constant {
    IN_LIST_1   => 0,
    IN_LIST_2   => 1,
    IN_BOTH     => 2,
};

if($str_1 eq "")
{
    $str_1 = $list_1;
}

if($str_2 eq "")
{
    $str_2 = $list_2;
}

open(f_list_1, "<", $list_1) || die"cannot open the file: $list_1!\n";
while(<f_list_1>)
{
    if(/^X:\\.*/)
    {
        $cmp_dic{$_} = IN_LIST_1;
    }
}
close f_list_1;

open(f_list_2, "<", $list_2) || die"cannot open the file: $list_2!\n";
while(<f_list_2>)
{
    if(/^X:\\.*/)
    {
        if(exists $cmp_dic{$_})
        {
            $cmp_dic{$_} = IN_BOTH;
        }
        else
        {
            $cmp_dic{$_} = IN_LIST_2;
        }
    }
}
close f_list_2;

foreach $files (keys %cmp_dic)
{
    print "  $key costs $value\n";
}

