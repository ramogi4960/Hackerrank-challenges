import re
"""
71
Adventure
Send a letter to the editor about the content of the Adventure website.
mpotts@ngs.org
Advertising
Why not sponsor an online feature?
jbmccorm@ngs.org
The Complete National Geographic
Use this help form to contact us with comments or support questions regarding The Complete National Geographic on DVD or hard drive.
CNG Help Form
Customer Service: Magazine Subscriptions
Send questions regarding your subscriptions. Check on delivery, expiration dates, or other concerns. Inquiries about National Geographic, National Geographic Kids, and Traveler can be sent to this email address. Customer service is also available online at ngsline@customersvc.com.
Digital Magazine Subscriptions
For questions about digital subscriptions to National Geographic magazine (iPad, Nook, Kindle, or Zinio) email us at ngsdigital@customersvc.com or call 1-800-895-2068. You can also read the digital FAQs online.
Donating to National Geographic
Please contact us at givinginfo@ngs.org or call +1 202 862 8638 with any questions regarding your donation, or how to make a donation in support of the Society's work in exploration, research, and education. Thank you for your support!
Frequently Asked Questions
Find answers to your questions here.
http://www.nationalgeographic.com/faq/
Games
For questions about downloadable games and Plan It Green Live, please write to:
askngs@nationalgeographic.com and put "Attn: Games" in the subject line.
Genographic Project
Send us your questions regarding the Genographic Project.
genographic@ngs.org
Genographic Project en espaï¿½ï¿½ol
Envienos en espaï¿½ï¿½ol sus preguntas sobre el Proyecto Genographic.
genographicespanol@ngs.org
Mobile Applications and More
Email us with comments or support questions regarding our content for iPhone, iPad, Android, Windows Mobile 7, and more: apps@ngs.org.
For magazine app and digital subscription queries email us at ngsdigital@customersvc.com or call 1-800-895-2068.
National Geographic Channel
Send comments or questions regarding our television programming.
feedback@natgeotv.com
National Geographic Expeditions
For more information or to reserve your space, call toll-free 1-888-966-8687, or reserve online at nationalgeographicexpeditions.com.
For email inquiries use this form.
National Geographic Magazine
Send a letter to the Editor about the content of National Geographic magazine. Letters will be considered for the monthly Forum column.
ngsforum@nationalgeographic.com
National Geographic Maps
Contact us with questions about our maps.
maps@ngs.org
Photography: Stock Photography
National Geographic Stock's photography collection offers the best in rights managed and royalty free wildlife, travel, landscape and lifestyle photographs available for professional editorial and commercial licensing.
stock@ngs.org
Photography: Commercial Assignments
National Geographic Assignment represents international commercial photographers specializing in lifestyle, adventure, travel, and landscape photography. Online portfolios are available.
ngassignment@ngs.org
Photography: Prints
You can order beautiful National Geographic prints for your home or as a great gift. Browse through our collection.
News
Send comments, questions or concerns regarding the National Geographic News site.
newsdesk@nationalgeographic.com
Public Relations
Send press inquiries here.
pressroom@ngs.org
Speakers Bureau
Send inquiries about having a National Geographic photographer, adventurer, explorer, or scientist speak at your next event.
speakers@ngs.org
TOPO! Digital Maps
Send us your product and technical support quesions.
topo@ngs.org
Traveler Magazine
Send a letter about Traveler magazine.
Traveler@ngs.org
Your Shot & Your Shot Puzzles
Help Form
Frequently Asked Questions
Miscellaneous
Not sure where to send your question? Weï¿½ï¿½ï¿½ll pass it to the proper department. Please keep in mind that the high volume of mail does not allow us to send everyone a personal answer.
askngs@nationalgeographic.com

Traveler@ngs.org;apps@ngs.org;askngs@nationalgeographic.com;feedback@natgeotv.com;genographic@ngs.org;genographicespanol@ngs.org;givinginfo@ngs.org;jbmccorm@ngs.org;maps@ngs.org;mpotts@ngs.org;newsdesk@nationalgeographic.com;ngassignment@ngs.org;ngsdigital@customersvc.com;ngsforum@nationalgeographic.com;ngsline@customersvc.com;pressroom@ngs.org;speakers@ngs.org;stock@ngs.org;topo@ngs.org
"""
pattern = r"\b[\w]+@[\w]+\.[\w]{1,3}\b"
addresses_list = []
for _ in range(int(input())):
    t = input()
    for item in sorted(re.findall(pattern, t)):
        addresses_list.append(item)
print(*addresses_list, sep=";")