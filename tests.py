# 6
# shashank <shashank@9mail.com>
# shashank <shashank@gmail.9om>
# shashank <shashank@gma_il.com>
# shashank <shashank@mail.moc>
# shashank <shashank@company-mail.com>
# shashank <shashank@companymail.c_o>

# 9
# vin <vineet@>
# vineet <vineet@gmail.com>
# vineet <vineet@gma.il.co.m>
# vineet <vineet@gma-il.co-m>
# vineet <vineet@gma,il.co@m>
# vineet <vineet@gmail,com>
# vineet <.vin@gmail.com>
# vineet <vin-nii@gmail.com>
# vineet <v__i_n-n_ii@gmail.com>

import re
p = re.compile("^[A-Za-z]{1}[A-Za-z-_\.]+@{1}[A-Za-z]+.{1}[A-Za-z]{1,3}$")
print(p.findall("kramzy-v.i_ne@gmail.com"))