# coding=utf8

import config, misc, crawler, parser

from collections import OrderedDict

def main():
	misc.mkdir_p("data/site/%s/%s/" % (config.wiki_lang, config.start_cat))
	misc.mkdir_p("data/pages/%s/%s/" % (config.wiki_lang, config.start_cat))
	misc.mkdir_p("data/speling/%s/%s/" % (config.wiki_lang, config.start_cat))

	config.init_config()

	# stage 1 - obtaining list of subcategories
	print("** Stage 1: Obtaining list of subcategories to crawl. **")
	subcats = crawler.crawl_subcats()

	# stage 2 - obtaining list of pages
	print("** Stage 2: Obtaining list of pages to crawl. **")
	pages = crawler.crawl_pages(subcats)

	# stage 3 - crawling all pages
	print("** Stage 3: Crawling all pages in list. **")
	crawler.crawl_all_pages(pages)

	# stage 4 - parsing (scraping) all pages
	print("** Stage 4: Parsing all pages in list. **")
	spelings = parser.parse(pages)

	# stage 5 - write to file
	print("** Stage 5: Writing final results to file. **")
	f = open("data/speling.txt", "w")
	for speling in spelings:
		f.write(speling + "\n")
	f.close()

	print("")
	print("")
	print("=== STATS ===")
	print("Crawled %d pages" % len(pages))
	print("Obtained %d spelings" % len(spelings))
	print("=============")

main()