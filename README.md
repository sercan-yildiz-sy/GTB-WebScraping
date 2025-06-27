# Newspaper Name Extractor

This project provides Python scripts to extract newspaper names, available dates, and related links for newspaper volumes from the Istanbul University Newspaper Archive using web scraping techniques.
There are two scripts available: 

•	`GTB-Data.py`: Uses manual string parsing to extract data from the HTML content.

•	`GTB-Data-BeautifulSoup.py`: Utilizes the requests library and BeautifulSoup for robust HTML parsing.

## Features

- Fetches the main archive page.
- Extracts all newspaper names listed on the page.
- Extracts links and dates to individual newspaper volumes.
- Outputs the extracted data for further processing.

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies with:

pip install requests beautifulsoup4
## Usage

1. Clone or download this repository.
2. Run the script:

python GTB-Data-BeautifulSoup.py

## Example Output
The extracted data is saved as JSON files.  
You can find the outputs in `newspapers.json` for `GTB-Data.py` and `newspapers-bs4.json` for `GTB-Data-BeautifulSoup.py`.

Example structure:
{
"Anadolu": [
    [
      "10 mart  1935",
      "https://nek.istanbul.edu.tr/ekos/GAZETE/anadolu/anadolu_1935/anadolu_1935_mart_/anadolu_1935__mart_10_.pdf"
    ],
    [
      "11 mart  1935",
      "https://nek.istanbul.edu.tr/ekos/GAZETE/anadolu/anadolu_1935/anadolu_1935_mart_/anadolu_1935__mart_11_.pdf"
    ],
    ...
  ],
  "Vatan": [
    [
      "04 Ağustos 1940",
      "https://nek.istanbul.edu.tr/ekos/GAZETE/vatan/vatan_1940/vatan_1940_agustos_/vatan_1940_agustos_4_.pdf"
    ],
    [
      "19 Ağustos 1940",
      "https://nek.istanbul.edu.tr/ekos/GAZETE/vatan/vatan_1940/vatan_1940_agustos_/vatan_1940_agustos_19_.pdf"
    ],
    ...

}



## Amount of Newspapers

The following table lists the available newspapers and their issue counts:

| Newspaper Name                                              | Issue Count |
|-------------------------------------------------------------|-------------|
| Açık Söz                                                    | 219         |
| Akşam                                                       | 3018        |
| Anadolu                                                     | 1859        |
| Aravelk                                                     | 324         |
| Aydın                                                       | 659         |
| Beyoğlu                                                     | 3005        |
| Borsa                                                       | 2038        |
| Bugün (Siyasi, İktisadi, İçtimai, Gündelik Gazete)          | 588         |
| Cumhuriyet                                                  | 6141        |
| Doğu                                                        | 289         |
| En Son Dakika                                               | 689         |
| En Son Havadis                                              | 179         |
| Haber (Akşam Postası)                                       | 2987        |
| Hakikat                                                     | 162         |
| Hakimiyeti Milliye                                          | 149         |
| Hakkın Sesi (Bursa)                                         | 198         |
| Halkın Dili                                                 | 134         |
| Halkın Sesi                                                 | 2147        |
| İkdam (Halk Gazetesi)                                       | 210         |
| İkdam (Cumhuriyet için, Halk için)                          | 328         |
| İkdam (Sabah Postası)                                       | 1062        |
| İzmir Postası                                               | 156         |
| Jamanak                                                     | 339         |
| Kurun                                                       | 1485        |
| Milliyet                                                    | 2237        |
| Munakaşa                                                    | 1641        |
| Piyasa Cetveli                                              | 150         |
| Savaş                                                       | 226         |
| Son Dakika                                                  | 330         |
| Son Posta                                                   | 4108        |
| Son Telgraf                                                 | 2068        |
| Son Saat                                                    | 309         |
| Tan                                                         | 2573        |
| Tasviri Efkar                                               | 578         |
| Türk Sözü                                                   | 2554        |
| Türk Dili                                                   | 1329        |
| Türkische Post                                              | 814         |
| Ulus                                                        | 2505        |
| Ulus Sesi                                                   | 836         |
| Ulusal Birlik                                               | 873         |
| Vakit                                                       | 3364        |
| Vatan                                                       | 1135        |
| Yarın                                                       | 413         |
| Yeni Asır                                                   | 2715        |
| Yeni Mersin                                                 | 1592        |
| Yeni Sabah                                                  | 1647        |
| Yenigün                                                     | 980         |
| Yeniyol                                                     | 944         |