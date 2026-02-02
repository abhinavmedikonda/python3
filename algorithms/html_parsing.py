from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for k, v in attrs:
            print(f"-> {k} > {v}")
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
    def handle_data(self, data):
        if not data.isspace():
            print(f"Data  : {data}")
    def handle_comment(self, data):
        m = re.search(r'\n', data)
        if m:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

'''
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

      <!--[if IE 9]>IE9-specific content
      <![endif]-->
      <div> Welcome to HackerRank</div>
      <!--[if IE 9]>IE9-specific content<![endif]-->

      <p>...article...</p>
      <p>...text...</p>

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
          <img src="photo.png" alt="The objects Tammy removed" />
        </a>
      </div>

      <p>...article...</p>
      <p>...text...</p>

      <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>
  </div>

  <footer>
    <p>
      A version of this article appeared in print on August 8,
      2010, on page BU1 of the New York edition.
    </p>
    <div class="source-org vcard copyright">
        Copyright 2010 <span class="org fn">Times Company</span>
    </div>
  </footer>
</article>
'''
if __name__ == '__main__':
    parser = MyHTMLParser()
    n = int(input())
    inp = [input() for _ in range(n)]
    inp = '\n'.join(inp)
    parser.feed(inp)
