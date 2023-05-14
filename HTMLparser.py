# in this ask, we take in an integer n, and n html scripts
# we are required to print out start tags, their attributes in a certain order, empty tags and end tags
# we can use the HTMLparser class from html.parser module to do this task
# if the tag has no attribute, we simply only print out the tag
# if the attribute of a tag has no value, we print the name of the attribute and "None" to represent its missing value
from html.parser import HTMLParser

"""
1
<meta http-equiv="refresh" content="5;url=http://example.com/" />
"""

"""
52
<article class="hentry">
  <!-- <header>
    <h1 class="entry-title">But Will It Make You Happy?</h1>
    <time class="updated" datetime="2010-08-07 11:11:03-0400">08-07-2010</time>
    <p class="byline author vcard">
        By <span class="fn">Stephanie Rosenbloom</span>
    </p>
  </header> -->

  <div class="entry-content">
      <p>...article text...</p>
      <p>...article text...</p>

      <figure>
        <img src="tammy-strobel.jpg" alt="Portrait of Tammy Strobel" />
        <figcaption>Tammy Strobel in her pared-down, 400sq-ft apt.</figcaption>
      </figure>

      <p>...article text...</p>
      <p>...article text...</p>

      <aside>
        <h2>Share this Article</h2>
        <ul>
          <li>Facebook</li>
          <li>Twitter</li>
          <li>Etc</li>
        </ul>
      </aside>

      <div class="entry-content-asset">
        <a href="photo-full.png">
          <img src="photo.png" alt="The objects Tammy removed from her life after moving" />
        </a>
      </div>

      <p>...article text...</p>
      <p>...article text...</p>

      <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>
  </div>

  <footer>
    <p>
      A version of this article appeared in print on August 8,
      2010, on page BU1 of the New York edition.
    </p>
    <div class="source-org vcard copyright">
        Copyright 2010 <span class="org fn">The New York Times Company</span>
    </div>
  </footer>
</article>
"""


class Kevin(HTMLParser):
    # def handle_comment(self, data):
    #     pass

    def handle_starttag(self, tag, attr):
        print("Start: ", tag)
        if attr is None:
            pass
        else:
            for item in attr:
                if item[1] is None:
                    print("->", item[0], "> None")
                else:
                    print("->", item[0], ">", item[1])

    def handle_startendtag(self, tag, attr):
        print("Empty: ", tag)
        if attr is None:
            pass
        else:
            for item in attr:
                if item[1] is None:
                    print("->", item[0], "> None")
                else:
                    print("->", item[0], ">", item[1])

    def handle_endtag(self, tag):
        print("End: ", tag)


f = ""
for i in range(int(input())):
    f += input()

file = Kevin()
file.feed(f)
