# in this task, we are given html links and are supposed to print out the links and their value
import re
"""
Test case
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
"""
"""
13
<div class="portal" role="navigation" id='p-navigation'>
<h3>Navigation</h3>
<div class="body">
<ul>
 <li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
 <li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li>
 <li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content  the best of Wikipedia">Featured content</a></li>
<li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li>
<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li>
<li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en" title="Support us">Donate to Wikipedia</a></li>
</ul>
</div>
</div>
"""
"""
7
<ul>
<li style="-moz-float-edge: content-box">Former Italian Prime Minister <a href="/wiki/Silvio_Berlusconi" title="Silvio Berlusconi">Silvio Berlusconi</a> <i>(pictured)</i> is <b><a href="/wiki/Silvio_Berlusconi_underage_prostitution_charges" title="Silvio Berlusconi underage prostitution charges">found guilty</a></b> of paying for sex with an underage prostitute.</li>
<li style="-moz-float-edge: content-box">In sports car racing, the <b><a href="/wiki/2013_24_Hours_of_Le_Mans" title="2013 24 Hours of Le Mans">24 Hours of Le Mans</a></b>, won by <a href="/wiki/Tom_Kristensen" title="Tom Kristensen">Tom Kristensen</a>, <a href="/wiki/Allan_McNish" title="Allan McNish">Allan McNish</a> and <a href="/wiki/Lo%C3%AFc_Duval" title="Loc Duval">Loc Duval</a>, is marred by the death of <b><a href="/wiki/Allan_Simonsen_(racing_driver)" title="Allan Simonsen (racing driver)">Allan Simonsen</a></b>.</li>
<li style="-moz-float-edge: content-box"><b><a href="/wiki/2013_Alberta_floods" title="2013 Alberta floods">Flooding</a></b> in <a href="/wiki/Alberta" title="Alberta">Alberta</a>, Canada, results in at least three deaths and the evacuation of thousands.</li>
<li style="-moz-float-edge: content-box"><b><a href="/wiki/2013_North_India_floods" title="2013 North India floods">Flash floods and landslides</a></b> in <a href="/wiki/Uttarakhand" title="Uttarakhand">Uttarakhand</a> and <a href="/wiki/Himachal_Pradesh" title="Himachal Pradesh">Himachal Pradesh</a> in India kill more than <span class="nowrap">1,000 people</span> and trap more than 20,000.</li>
<li style="-moz-float-edge: content-box">In <a href="/wiki/Basketball" title="Basketball">basketball</a>, the <a href="/wiki/Miami_Heat" title="Miami Heat">Miami Heat</a> defeat the <a href="/wiki/San_Antonio_Spurs" title="San Antonio Spurs">San Antonio Spurs</a> to win the <b><a href="/wiki/2013_NBA_Finals" title="2013 NBA Finals">NBA Finals</a></b>.</li>
</ul>
"""
"""
7
<center>
<div class="noresize" style="height: 242px; width: 600px; "><map name="ImageMap_1_971996215" id="ImageMap_1_971996215">
<area href="/wiki/File:Pardalotus_punctatus_female_with_nesting_material_-_Risdon_Brook.jpg" shape="rect" coords="3,3,297,238" alt="Female" title="Female" />
<area href="/wiki/File:Pardalotus_punctatus_male_with_nesting_material_-_Risdon_Brook.jpg" shape="rect" coords="302,2,597,238" alt="Male" title="Male" /></map><img alt="Pair of Spotted Pardalotes" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/600px-Female_and_male_Pardalotus_punctatus.jpg" width="600" height="242" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/900px-Female_and_male_Pardalotus_punctatus.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/1200px-Female_and_male_Pardalotus_punctatus.jpg 2x" usemap="#ImageMap_1_971996215" />
<div style="margin-left: 0px; margin-top: -20px; text-align: left;"><a href="/wiki/File:Female_and_male_Pardalotus_punctatus.jpg" title="About this image"><img alt="About this image" src="//bits.wikimedia.org/static-1.22wmf7/extensions/ImageMap/desc-20.png" style="border: none;" /></a></div>
</div>
</center>
"""

pattern = r"(?<=href=\")(.*?)(?=\")(.*?)(?<=>)(.*?)(?=</a>)"
f = [input() for _ in range(int(input()))]
for item in f:
    if re.search(pattern, item):
        print(re.search(pattern, item).group(1) + "," + re.search(pattern, item).group(2))


