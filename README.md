<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Mini-Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites-and-installation">Prerequisites and Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The goal of this project is to enable menu scraping for a client on ``hungerstation.com``. The required data to scrape includes restaurant name and location (district & coordinates), meal types and individual meal names, their prices, calories, descriptions and images.

Specifically, the following procedure must be performed to scrape a website:
- Define a Golang struct with necessary data components.
- Use Colly & GJSON to index into scraped data's HTML structure and map it against the defined struct.
- Write the obtained result into a JSON file.
- Combine all the resultant JSON files into a tabular CSV format for easier client usage.

### Built With

The following main Golang libraries were used to build this project:
- <a href="https://github.com/tidwall/gjson">GJSON</a>
- <a href="https://github.com/gocolly/colly">Colly</a>

<!-- GETTING STARTED -->
## Getting Started

This is a list of instructions on how anyone can get started with this code.

### Prerequisites & Installation

1. Clone the repo
```sh
    git clone https://github.com/lynxalytics/menu-scraper.git
```
2. Install Golang, if not installed
- <a href="https://go.dev/dl/">Golang</a>

<!-- USAGE EXAMPLES -->
## Usage

To run this code, use the following command on your terminal:

``` sh
    go run scraper-sa.go
```
The processed files will be saved under ``./data`` folder in your current working directory.
