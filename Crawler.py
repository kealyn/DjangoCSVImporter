# =============================================================================
# Python Crawler
#
# Description: A python program that pulls data out of HTML and XML files. It
#              makes use of Beautiful Soup library, aiming to find out the
#              provost of the school by the given seed file. 
#
# Author     : Lin Qi
# Created on : Mar. 26th, 2013
# Updated on : Mar. 26th, 2013
# =============================================================================

import sys,os,re
import urllib2
import codecs
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str




class Crawler:
  
  def __init__(self, filename, threshold):
    self.seed = ""
    self.filename = filename
    self.visited_urls=[]
    self.domain=""
    self.threshold = threshold
    
  def fetch(self):
    response = urllib2.urlopen(self.seed)
    html = response.read()
    return html

  # Try to open the url, if it fails return empty array
  # Find all <a>-tags on the page
  # Skip links with 'nofollow'
  # Don't want to get stuck in an abyss of some forum, so strip querystrings from url
  # Screw the anchor links (#)
  #If the link is relative, try to piece together something that makes sense
  def run(self):
    base_address = self.seed
    link_list = self.crawl(base_address, self.domain)

    for l in link_list:
      new_page = True
      for visited_url in self.visited_urls:
        if l['url'] == visited_url['url']:
          new_page = False
      if new_page:
        print 'new page: ', l['url']
        self.visited_urls.append(l)
        link_list.extend(self.crawl(l['url'], self.domain))
        
      if int(self.threshold) > 0 and \
         int(len(self.visited_urls)) > int(self.threshold):
         print 'threshold: ',self.threshold
         break
              
    self._Crawler__write_to_csv(self.filename)

  # crawl() is the most important method here. It takes url and domain as
  # parameters. url is url that we want to parse and domain is used to check
  # the url points to the right domain.
  def crawl(self, url, domain):
    # return empty array if opening url fails
    try:
      response = urllib2.urlopen(url)
    except urllib2.HTTPError:
      return []

    # add '/' to the end of url
    if url[len(url)-1] != '/':
      url = url[:url.rindex('/')+1]
  
    # get all anchor-tags from the page
    html = response.read()
    soup = BeautifulSoup(html)
    links = soup.findAll('a')
    
    # search within the newpage to find provost information
        
    
        
        
    
        
        
        
    link_list = []
    for link in links:
      # skip links with rel = 'nofollow'
      if link.get('rel')=='nofollow':
        continue
      href = link.get('href','empty')
      # remove everything after '#'
      if href.find('#')!=-1:
        href=href[:href.index('#')]
      if href.find('?')!=-1:
        ref=href[:href.index('?')]

      if not href.startswith('http') and not href.startswith('www'):
        if href.startswith('/'):
          href = url + href[1:]
        elif href.startswith('..'):
          href = url[0:url[0:-1].rindex('/')] + href[2:]
        elif href.startswith('.'):
          href = url + href

      if href.startswith(domain):
        link_dictionary = {'title':link.text,
                           'url':href}
        link_list.append(link_dictionary)

    return link_list

  def __write_to_csv(self, filename):
    file = open(filename, 'wb')
    file.write('Title, URL\r\n')
    for url in self.visited_urls:
      file.write('{},{}\r\n'.format(url['title'].encode('utf-8'),url['url'].encode('utf-8')))
      #file.write('{},{}\r\n'.format(url['title'],url['url']))
    file.close
    


def main():
  base_url = "http://www.google.com"
  file_name = "result.txt"
  base_domain = "http://www"
  threshold = 100
  
  crawler = Crawler(file_name,threshold)
  
  
  crawler.seed = base_url
  crawler.domain = base_domain
  
  
  
  crawler.run()

if __name__ == "__main__":
  main()



  
