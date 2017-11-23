my $report_in  = $ARGV[0];
my $report_out = $ARGV[1];
my $fatal_out  = $ARGV[2];

my $txt_head  = '';
my $txt_out   = '';
my $txt_fatal = '';

open(CW_IN,"<",$report_in) || die"cannot open the file: $report_in\n";
open(CW_OUT,">",$report_out) || die"cannot open the file: $report_out\n";
open(CW_FATAL,">",$fatal_out) || die"cannot open the file: $fatal_out\n";

my $line_cnt    = 0;
my $err_cnt     = 0;
my $fatal_cnt   = 0;

while(<CW_IN>)
{
    if(/^\*/)
    {
        if($err_cnt != 0)
        {
            print CW_OUT $txt_head;
            print CW_OUT $txt_out;
            print CW_OUT "\n";
            
            if($fatal_cnt != 0)
            {
                print CW_FATAL $txt_head;
                print CW_FATAL $txt_fatal;
                print CW_FATAL "\n";
            }
            
            $txt_head  = '';
            $txt_out   = '';
            $txt_fatal = '';
        }
        elsif($line_cnt != 0)   # $err_cnt == 0 && $line_cnt != 0
        {
            $txt_head  = '';
        }
        
        $line_cnt = 0;
        $err_cnt = 0;
        $fatal_cnt = 0;

        my $txt = sprintf("$_");
        $txt_head = $txt_head.$txt;
    }
    else
    {
        $line_cnt++;
    
        if(/((WARNING)|(ERROR))\s+with\s+.*?;\s+(.*?);\s+Resolution;\s+(.*?);\s+(.*?);/)
        {
            my $var  = $4;
            my $res1 = $5;
            my $res2 = $6;
            
            $res1 = calc_res($res1);
            $res2 = calc_res($res2);
            
            if($res1 != $res2)
            {
                $err_cnt++;
                my $txt = sprintf("$_");
                $txt_out = $txt_out.$txt;
            }
        }
        elsif(/((WARNING)|(ERROR))\s+with\s+.*?;\s+(.*?);\s+Data Type;\s+(.*?);\s+(.*?);/)
        {        
            my $var  = $4;
            my $typ1 = $5;
            my $typ2 = $6;
            
            my $typ_len1 = 0;
            my $typ_len2 = 0;
            
            if( ($typ1 eq $typ2) || $var =~/_CPV$/)
            {
                # do nothing
            }
            else
            {
                $err_cnt++;
                my $txt = sprintf("$_");
                $txt_out = $txt_out.$txt;
                
                if( ($typ1 eq 'N/A') || ($typ2 eq 'N/A') )
                {
                    # do nothing
                }
                else
                {
                    $typ1 = clac_type($typ1);
                    $typ2 = clac_type($typ2);
                    $typ_len1 = clac_type_len($typ1);
                    $typ_len2 = clac_type_len($typ2);
                    
                    if($typ1 eq $typ2)
                    {
                        # do nothing.
                    }
                    elsif($typ_len1 eq $typ_len2)
                    {
                        # do nothing.
                    }
                    else
                    {
                        $fatal_cnt++;
                        my $txt = sprintf("$_");
                        $txt_fatal = $txt_fatal.$txt;
                    }
                }
                
            }
        }
    }
}

sub calc_res
{
    my ($express) = @_;
    my $res = $express;
    my $res_15 = '';
    
    if( $express =~ /^(\d+)\/(\d+)$/ )
    {
        $res = $1 / $2;
        #print "$res = $1 / $2\n";
    }
    elsif( $express =~ /^(\d+)\/(\d+)\^(\d+)$/ )
    {
        $res = ( $1 / ($2 ** $3) );
        #print "$res = ( $1 / ($2 ** $3) )\n"
    }
    elsif( $express =~ /^N\/A$/ )
    {
        $res = 1;
    }
    
    $res_15 = sprintf("%.15d", $res);
    
    return $res_15;
}

sub clac_type
{
    my ($express) = @_;
    my $typ = $express;
    
    if( $express =~ /^BOOL_TYPE$/ )
    {
        $typ = 'eq_U8';
    }
    elsif( $express =~ /^DTI_SUBM_TYPE$/ )
    {
        $typ = 'eq_U8';
    }
    elsif( $express =~ /(.*?)_CAL$/ )
    {
        $typ = $1;
    }
    return $typ;
}

sub clac_type_len
{
    my ($typ) = @_;
    my $len = $typ;
    
    if( $typ eq 'eq_U8')    {   $len = '1';   }
    elsif( $typ eq 'U8')    {   $len = '1';   }
    elsif( $typ eq 'S8')    {   $len = '1';   }
    elsif( $typ eq 'U16')   {   $len = '2';   }
    elsif( $typ eq 'S16')   {   $len = '2';   }
    elsif( $typ eq 'S32')   {   $len = '4';   }
    elsif( $typ eq 'U32')   {   $len = '4';   }
    elsif( $typ eq 'U8 PTR')    {   $len = 'ptr 1';   }
    elsif( $typ eq 'S8 PTR')    {   $len = 'ptr 1';   }
    elsif( $typ eq 'U16 PTR')   {   $len = 'ptr 2';   }
    elsif( $typ eq 'S16 PTR')   {   $len = 'ptr 2';   }
    elsif( $typ eq 'U32 PTR')   {   $len = 'ptr 4';   }
    elsif( $typ eq 'S32 PTR')   {   $len = 'ptr 4';   }

    return $len;
}

close(CW_IN);
close(CW_OUT);
close(CW_FATAL);