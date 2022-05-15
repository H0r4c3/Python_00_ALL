from bs4 import BeautifulSoup

# create an html document
html_doc = '''
<td class="section_header_column" valign="top" width="300">
<div class="forum_thread_header">
<a href="/calendar/" title="TV Series Calendar" style="color: #FFFFFF;"><b>Aired today on EZTV:</b> Saturday</a>
</div>
<div style="overflow: auto; width: 300px; height: 132px; padding-left: 0px;" class="section_header_column">
<table border="0" align="center" width="100%" cellspacing="0" cellpadding="0" style="text-align: left;">
<tbody><tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/8241/a-black-lady-sketch-show/" class="thread_link" title="A Black Lady Sketch Show Torrent"><b><font size="1">A Black Lady Sketch Show</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2795/all-in-with-chris-hayes/" class="thread_link" title="All In with Chris Hayes Torrent"><b><font size="1">All In with Chris Hayes</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2213/american-justice/" class="thread_link" title="American Justice Torrent"><b><font size="1">American Justice</font></b></a>
</td>
</tr>
 <tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1891/atlanta/" class="thread_link" title="Atlanta Torrent"><b><font size="1">Atlanta</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/248725/backroad-truckers/" class="thread_link" title="Backroad Truckers Torrent"><b><font size="1">Backroad Truckers</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3141/beat-bobby-flay/" class="thread_link" title="Beat Bobby Flay Torrent"><b><font size="1">Beat Bobby Flay</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/419828/becoming-a-popstar/" class="thread_link" title="Becoming A Popstar Torrent"><b><font size="1">Becoming A Popstar</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/424853/black-files-declassified/" class="thread_link" title="Black Files Declassified Torrent"><b><font size="1">Black Files Declassified</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/887/the-blacklist/" class="thread_link" title="Blacklist, The Torrent"><b><font size="1">Blacklist, The</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1910/bull/" class="thread_link" title="Bull Torrent"><b><font size="1">Bull</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/260875/chef-boot-camp/" class="thread_link" title="Chef Boot Camp Torrent"><b><font size="1">Chef Boot Camp</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425871/chivalry/" class="thread_link" title="Chivalry Torrent"><b><font size="1">Chivalry</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425203/conversations-with-a-killer-the-john-wayne-gacy-tapes/" class="thread_link" title="Conversations with a Killer: The John Wayne Gacy Tapes Torrent"><b><font size="1">Conversations with a Killer: The John Wayne Gacy Tapes</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/34830/diners-drive-ins-and-dives-triple-d-nation-cultural-cookin/" class="thread_link" title="Diners, Drive-ins and Dives Triple D Nation: Cultural Cookin' Torrent"><b><font size="1">Diners, Drive-ins and Dives Triple D Nation: Cultural Cookin'</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/4266/earth-odyssey-with-dylan-dreyer/" class="thread_link" title="Earth Odyssey with Dylan Dreyer Torrent"><b><font size="1">Earth Odyssey with Dylan Dreyer</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/14657/elite/" class="thread_link" title="Elite Torrent"><b><font size="1">Elite</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/227758/fast-foodies/" class="thread_link" title="Fast Foodies Torrent"><b><font size="1">Fast Foodies</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3889/fatal-attraction/" class="thread_link" title="Fatal Attraction Torrent"><b><font size="1">Fatal Attraction</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1596/full-frontal-with-samantha-bee/" class="thread_link" title="Full Frontal with Samantha Bee Torrent"><b><font size="1">Full Frontal with Samantha Bee</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3303/gardening-australia/" class="thread_link" title="Gardening Australia Torrent"><b><font size="1">Gardening Australia</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3143/gogglebox/" class="thread_link" title="Gogglebox Torrent"><b><font size="1">Gogglebox</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/211365/gold-rush-freddy-dodges-mine-rescue/" class="thread_link" title="Gold Rush: Freddy Dodge's Mine Rescue Torrent"><b><font size="1">Gold Rush: Freddy Dodge's Mine Rescue</font></b></a>
</td>
</tr>
 <tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/239559/graysons-art-club/" class="thread_link" title="Grayson's Art Club Torrent"><b><font size="1">Grayson's Art Club</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425905/heartstopper/" class="thread_link" title="Heartstopper Torrent"><b><font size="1">Heartstopper</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425906/hold-tight/" class="thread_link" title="Hold Tight Torrent"><b><font size="1">Hold Tight</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/297739/icarly/" class="thread_link" title="iCarly Torrent"><b><font size="1">iCarly</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1210/the-late-late-show-with-james-corden/" class="thread_link" title="James Corden, The Late Late Show with Torrent"><b><font size="1">James Corden, The Late Late Show with</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/983/the-tonight-show-starring-jimmy-fallon/" class="thread_link" title="Jimmy Fallon, The Tonight Show Starring Torrent"><b><font size="1">Jimmy Fallon, The Tonight Show Starring</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/247112/kate-humbles-coastal-britain/" class="thread_link" title="Kate Humble's Coastal Britain Torrent"><b><font size="1">Kate Humble's Coastal Britain</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/210602/kindred-spirits/" class="thread_link" title="Kindred Spirits Torrent"><b><font size="1">Kindred Spirits</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/67906/lego-masters-australia/" class="thread_link" title="Lego Masters Australia Torrent"><b><font size="1">Lego Masters Australia</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/186797/lets-make-a-deal/" class="thread_link" title="Lets Make a Deal Torrent"><b><font size="1">Lets Make a Deal</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425418/life-after-life/" class="thread_link" title="Life After Life Torrent"><b><font size="1">Life After Life</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/418919/love-all-play/" class="thread_link" title="Love All Play Torrent"><b><font size="1">Love All Play</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/4535/masterchef/" class="thread_link" title="MasterChef Torrent"><b><font size="1">MasterChef</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1248/masterchef-australia/" class="thread_link" title="MasterChef Australia Torrent"><b><font size="1">MasterChef Australia</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/417593/moon-knight/" class="thread_link" title="Moon Knight Torrent"><b><font size="1">Moon Knight</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/187/mv-group-documentaries/" class="thread_link" title="MV Group Documentaries Torrent"><b><font size="1">MV Group Documentaries</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2717/mysteries-of-the-abandoned/" class="thread_link" title="Mysteries of the Abandoned Torrent"><b><font size="1">Mysteries of the Abandoned</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/123141/newsroom-tokyo/" class="thread_link" title="Newsroom Tokyo Torrent"><b><font size="1">Newsroom Tokyo</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/249669/nightwatch/" class="thread_link" title="Nightwatch Torrent"><b><font size="1">Nightwatch</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2428/not-going-out/" class="thread_link" title="Not Going Out Torrent"><b><font size="1">Not Going Out</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1911/other-tv-shows/" class="thread_link" title="Other TV Shows Torrent"><b><font size="1">Other TV Shows</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/242245/pacific-rim-the-black/" class="thread_link" title="Pacific Rim: The Black Torrent"><b><font size="1">Pacific Rim: The Black</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/140214/paranormal-caught-on-camera/" class="thread_link" title="Paranormal Caught on Camera Torrent"><b><font size="1">Paranormal Caught on Camera</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/4904/pilgrimage/" class="thread_link" title="Pilgrimage Torrent"><b><font size="1">Pilgrimage</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/419070/rat-in-the-kitchen/" class="thread_link" title="Rat in the Kitchen Torrent"><b><font size="1">Rat in the Kitchen</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/225/real-time-with-bill-maher/" class="thread_link" title="Real Time with Bill Maher Torrent"><b><font size="1">Real Time with Bill Maher</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/392568/rupauls-drag-race-uk-vs-the-world/" class="thread_link" title="RuPaul's Drag Race UK vs the World Torrent"><b><font size="1">RuPaul's Drag Race UK vs the World</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/4350/russian-doll/" class="thread_link" title="Russian Doll Torrent"><b><font size="1">Russian Doll</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/4725/selling-sunset/" class="thread_link" title="Selling Sunset Torrent"><b><font size="1">Selling Sunset</font></b></a>
 </td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/991/seth-meyers-late-night-with/" class="thread_link" title="Seth Meyers, Late Night With Torrent"><b><font size="1">Seth Meyers, Late Night With</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/419101/shadowverse/" class="thread_link" title="Shadowverse Torrent"><b><font size="1">Shadowverse</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2149/siesta-key/" class="thread_link" title="Siesta Key Torrent"><b><font size="1">Siesta Key</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425571/so-dumb-its-criminal-hosted-by-snoop-dogg/" class="thread_link" title="So Dumb it's Criminal Hosted by Snoop Dogg Torrent"><b><font size="1">So Dumb it's Criminal Hosted by Snoop Dogg</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3666/sports/" class="thread_link" title="Sports Torrent"><b><font size="1">Sports</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/16418/sun-sea-and-selling-houses/" class="thread_link" title="Sun, Sea and Selling Houses Torrent"><b><font size="1">Sun, Sea and Selling Houses</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1259/swamp-people/" class="thread_link" title="Swamp People Torrent"><b><font size="1">Swamp People</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/165822/taskmaster/" class="thread_link" title="Taskmaster Torrent"><b><font size="1">Taskmaster</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/410520/that-dirty-black-bag/" class="thread_link" title="That Dirty Black Bag Torrent"><b><font size="1">That Dirty Black Bag</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/155980/the-amber-ruffin-show/" class="thread_link" title="The Amber Ruffin Show Torrent"><b><font size="1">The Amber Ruffin Show</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1862/the-bold-and-the-beautiful/" class="thread_link" title="The Bold and the Beautiful Torrent"><b><font size="1">The Bold and the Beautiful</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/145798/the-daily-show-james-corden/" class="thread_link" title="The Daily Show James Corden Torrent"><b><font size="1">The Daily Show James Corden</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/15459/the-kelly-clarkson-show/" class="thread_link" title="The Kelly Clarkson Show Torrent"><b><font size="1">The Kelly Clarkson Show</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2793/the-last-word-with-lawrence-odonnell/" class="thread_link" title="The Last Word with Lawrence O'Donnell Torrent"><b><font size="1">The Last Word with Lawrence O'Donnell</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/426020/the-long-game-bigger-than-basketball/" class="thread_link" title="The Long Game: Bigger Than Basketball Torrent"><b><font size="1">The Long Game: Bigger Than Basketball</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425232/the-marked-heart/" class="thread_link" title="The Marked Heart Torrent"><b><font size="1">The Marked Heart</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2172/the-pioneer-woman/" class="thread_link" title="The Pioneer Woman Torrent"><b><font size="1">The Pioneer Woman</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3094/the-price-is-right/" class="thread_link" title="The Price Is Right Torrent"><b><font size="1">The Price Is Right</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/2749/the-rachel-maddow-show/" class="thread_link" title="The Rachel Maddow Show Torrent"><b><font size="1">The Rachel Maddow Show</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/426059/the-rising/" class="thread_link" title="The Rising Torrent"><b><font size="1">The Rising</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1867/the-talk/" class="thread_link" title="The Talk Torrent"><b><font size="1">The Talk</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/140213/the-unxplained/" class="thread_link" title="The UnXplained Torrent"><b><font size="1">The UnXplained</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/1863/the-young-and-the-restless/" class="thread_link" title="The Young and the Restless Torrent"><b><font size="1">The Young and the Restless</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3607/tomorrow-tonight/" class="thread_link" title="Tomorrow Tonight Torrent"><b><font size="1">Tomorrow Tonight</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/274/top-chef/" class="thread_link" title="Top Chef Torrent"><b><font size="1">Top Chef</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/406965/troppo/" class="thread_link" title="Troppo Torrent"><b><font size="1">Troppo</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/3018/vice-news-tonight/" class="thread_link" title="Vice News Tonight Torrent"><b><font size="1">Vice News Tonight</font></b></a>
</td>
</tr>
<tr name="hover">
<td class="forum_thread_post_end">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/shows/425263/yakamoz-s-245/" class="thread_link" title="Yakamoz S-245 Torrent"><b><font size="1">Yakamoz S-245</font></b></a>
</td>
</tr>
</tbody></table>
</div>
</td>
'''

# path for the offline html file
path_html = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Scraping_eztv\eztv.html'

# import the offline html file
with open(path_html, 'r') as eztv_file:
    soup = BeautifulSoup(eztv_file, "html.parser")
    
# view the content of the soup object
#print(soup.contents)
    
# search using find methods for a tag
tag_td = soup.find('td')

# print tag_td
print(tag_td)

# search using find for an ID
find_id = soup.find(id='???')

# print find_id
print(find_id)

# print the text value
print(tag_td.text)

# search based of css class name (present as attribute)
#css_class_search = soup.find(attrs={"class" : "forum_thread_post_end"})
css_class_search = soup.find_all("a", attrs={"class" : "thread_link"})

# print
print(css_class_search)
print(css_class_search.text)



