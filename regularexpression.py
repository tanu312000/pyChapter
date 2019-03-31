# import re
# regex=r"ab*c"
# matches=re.findall(regex,"ab,abc,abbbc,abbbbbc")
# print(matches)

# import re
# regex=r"ab+c"
# matches=re.findall(regex,"abc,ac,abbbc,abbc")
# print(matches)
#
import re
regex=r"ab?c"
matches=re.findall(regex,"abc,ac,abbc")
print(matches)

# import re
# regex=r"a.c"
# matches=re.findall(regex,"abc,agc,axc,amc,apc,a12,a&c,abcd")
# print(matches)
#
# import re
# regex=r"b[aeiou]d"
# matches=re.findall(regex,"aaabad,bad,bed,bod,bid,bedd,baddy")
# print(matches)
#
# import re
# regex=r"b[^aeiou]d"
# matches=re.findall(regex,"aaabad,bad,bed,bod,bid,bedd,baddy,bnf,brd")
# print(matches)
#
# import re
# regex=r"ab{3}c"
# matches=re.findall(regex,"abbbc,abbbbc,abbc,abc,bed,baed,bead,bxd,brd")
# print(matches)
#
#
# import re
# regex=r"ab{3,5}c"
# matches=re.findall(regex,"abbbc,abbbbbc,abbc,abc,bed,baed,bead,bxd,brd")
# print(matches)
#
# import re
# regex=r"ab{,5}c"
# matches=re.findall(regex,"abbbc,abbbc,abc,abbc,abc,abbc,abbbc,abbbbbc,ac")
# print(matches)
#
# import re
# regex=r'suresh'
# s='''vidhatri is a good girl\n
# vidhatri is cute\n
# suresh is aweeeeeesome\n
# suresh is charming\n
# suresh is almighty'''
#
# matches=re.findall(regex,s)
# print(matches)


# import re
# regex=r'perl$'
# s1='perl is a language'
# s2='perl'
# s3='is a scripting perl'
#
# matches=re.findall(regex,s1)
# print(matches)

import re
regex=r""

