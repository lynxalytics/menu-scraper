package main

import (
	// "strconv"
	"time"
	"fmt"
	"strings"
	"io/ioutil"
	"encoding/json"
 
 	"github.com/tidwall/gjson"
	"github.com/gocolly/colly"
)

// create a struct to store all relevant menu data
type Menu struct {
	
	ChainName   string `json:"chain_name"`
	District    string `json:"district"`
	VendorMenu  string `json:"vendor_menu"`

}

func main() {

	// define base URL
	base_url := "https://hungerstation.com/sa-en/regions/al-khobar/"

	// initialize collector to make HTTP requests
	c := colly.NewCollector(
		colly.AllowedDomains("hungerstation.com", "www.hungerstation.com"),
		c.CacheDir("C:/Users/Aljawad/Desktop/scraper/cache"),
	)

	// print the web page being visited
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	// get meal type, meal names, calories, descriptions and images
	c.OnHTML("#__NEXT_DATA__", func(e *colly.HTMLElement) {
		
		text := e.Text

		district   := gjson.Get(text, "props.pageProps.district").String()
		chainName  := gjson.Get(text, "props.pageProps.vendor.chain_name").String()
		vendorMenu := gjson.Get(text, "props.pageProps.vendorMenu").String()

		m := Menu{ChainName: chainName, District: district, VendorMenu: vendorMenu}

		// save to JSON file
		menuJson, _ := json.MarshalIndent(m, "", " ")
    	_ = ioutil.WriteFile("./data/out-" + chainName + ".json", menuJson, 0644)

	})

	c.OnHTML("a[href]", func(e *colly.HTMLElement) {

		link := e.Attr("href")

		if strings.Index(link, "al-khobar") == -1 || strings.Index(link, "?") > -1 {
			return
		}

		// set sleeping time for this iteration to avoid Cloudfare problems
		time.Sleep(30 * time.Second)

		// start scaping the page under the link found
		e.Request.Visit(link)
	})

	c.Visit(base_url)

}
