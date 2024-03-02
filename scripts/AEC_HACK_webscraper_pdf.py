import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime


def download_files_from_sites(site_urls, fileExtensions):
    parent_folder = '../data/scraper_pdf'
    
    # Create a parent folder for downloads if it doesn't exist
    if not os.path.exists(parent_folder):
        os.makedirs(parent_folder)
    
    for site_url in site_urls:
        # Send an HTTP request to the URL
        response = requests.get(site_url)
    
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
    
            # Get the site name for subfolder
            site_name = urlparse(site_url).hostname
            download_folder = os.path.join(parent_folder, site_name)
            
            # Create a subfolder for downloads if it doesn't exist
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)
            
            # Find all the elements with 'src' or 'href' attributes
            #file_elements = soup.find_all(['src', 'href'])
            # Find all the elements with 'src' or 'href' attributes
            file_elements = soup.find_all(
                    lambda
                    tag: tag.get(
                    'src'
                    )
                    or
                    tag.get(
                    'href'
                )
            )
    
            urlList=[]

            for file_element in file_elements:
                # Get the URL from the 'src' or 'href' attribute
                file_url = file_element.get('src') or file_element.get('href')
    
                # Join the URL with the base URL to get the absolute URL
                absolute_url = urljoin(site_url, file_url)
                
                if contains_any(absolute_url, fileExtensions):
                    # Parse the absolute URL
                    parsed_url = urlparse(absolute_url)
                    
                    # Extract the filename from the URL
                    filename = os.path.basename(parsed_url.path)
    
                    # Create the complete path to save the file
                    file_path = os.path.join(download_folder, filename)
                    if not os.path.exists(file_path):
                        # Download the file
                        try:
                            with open(file_path, 'wb') as file:
                                file.write(requests.get(absolute_url).content)
                            print(f"Downloaded: {filename} from {site_name}")
                            urlAndFile = absolute_url + ";" + filename
                            urlList.append(urlAndFile)
                            
                        except Exception as e:
                            print(f"Failed to download {filename} from {site_name}. Error: {e}")
    
            exportUrlList(urlList,site_name,parent_folder)
        else:
            print(f"Failed to retrieve the page from {site_url}. Status code: {response.status_code}")
            

def contains_any(text, values):
    # Using a loop
    for value in values:
        if value in text:
            return True
    return False

def exportUrlList(urlList,domain,rootfolder):
    # Specify the file path
    file_path =rootfolder+'/'+domain+'/'+'URLlist_'+get_custom_timestamp()+'.txt'

    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        # Write each value from the list to a new line in the file
        for value in urlList:
            file.write(f"{value}\n")

    print(f"The list has been exported to {file_path}.")


def get_custom_timestamp():
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Format the date and time as YYYY-MM-DDTHH-min
    formatted_timestamp = current_datetime.strftime('%Y-%m-%dT%H-%M')
    
    return formatted_timestamp



# Example usage with a list of site URLs
fileExtensions = ['.pdf']
#sites_to_scrape1 = ['https://example1.com', 'https://example2.com', 'https://example3.com']
sites_to_scrape1=['https://kaupunkiliikenne.fi/kaupunkiraidehankkeet-ja-kunnossapito/urakoitsijalle/tyot-metroradan-laheisyydessa/']
sites_to_scrape= [
    'https://www.finlex.fi/fi/laki/ajantasa/1999/19990132#L17P120 ',
    'https://ym.fi/rakentamismaaraykset',
    'https://www.espoo.fi/fi/liikenne-ja-kadut/yleis-katu-puisto-ja-rakennussuunnitelmat-ohjeistus#katu--puisto--ja-rakennussuunnitelmat-19233',
    'https://kaupunkitilaohje.hel.fi/haku/',
    'https://kaupunkitilaohje.vantaa.fi/fi/katutila/ohjeita-katujen-ja-vesihuollon-suunnittelijoille',
    'https://kaupunkitilaohje.vantaa.fi/fi',
    'https://tampereentilapalvelut.fi/materiaalipankki/suunnitteluohjeet/',
    'https://www.ouka.fi/rakennusvalvonta/maaraykset-ja-ohjeet?accordion=accordion-2575'
]
sites_to_scrape_all= [
    'https://kaupunkitilaohje.vantaa.fi/fi',
    'https://kaupunkitilaohje.vantaa.fi/fi/viheralueet-ja-kasvillisuus/viheralueet',
    'https://www.kuntaliitto.fi/julkaisut/2012/1481-hulevesiopas',
    'https://kaupunkitilaohje.vantaa.fi/fi/katutila/ohjeita-katujen-ja-vesihuollon-suunnittelijoille',
    'https://kaupunkitilaohje.vantaa.fi/fi/palveluhakemisto/palvelu/katujen-ja-puistojen-luvat',
    'https://kaupunkitilaohje.vantaa.fi/fi/ohjeita-ulkovalaistuksen-suunnittelijoille',
    'https://kaupunkitilaohje.hel.fi/kortti/luiska/',
    'https://kaupunkitilaohje.hel.fi/kortti/portaat-2/',
    'https://kaupunkitilaohje.hel.fi/kortti/sillat/',
    'https://kaupunkitilaohje.hel.fi/kortti/kansirakenteet/',
    'https://kaupunkitilaohje.hel.fi/kortti/asfaltoitu-kansi-rakenteen-tyyppiratkaisu/',
    'https://kaupunkitilaohje.hel.fi/kortti/hulevesien-hallintarakenteet/',
    'https://kaupunkitilaohje.hel.fi/kortti/luonnonkivikouru/',
    'https://kaupunkitilaohje.hel.fi/kortti/laiturit-kulkutasot-terassit/',
    'https://kaupunkitilaohje.hel.fi/kortti/mattolaiturit/',
    'https://kaupunkitilaohje.hel.fi/kortti/uimarannat/',
    'https://kaupunkitilaohje.hel.fi/kortti/veneiden-talvisailytys/',
    'https://kaupunkitilaohje.hel.fi/kortti/betoni/',
    'https://kaupunkitilaohje.hel.fi/kortti/kivikori/',
    'https://kaupunkitilaohje.hel.fi/kortti/luonnonkivi-massiivikivi-graniitti-liuskekivi/',
    'https://kaupunkitilaohje.hel.fi/kortti/puu/',
    'https://ym.fi/luonto-ja-vedet/lainsaadanto',
    'https://ym.fi/maankaytto-ja-rakennuslaki',
    'https://finlex.fi/fi/laki/ajantasa/1999/19990132',
    'https://www.finlex.fi/fi/laki/ajantasa/1999/19990895',
    'https://ym.fi/rakentamislaki',
    'https://ym.fi/alueidenkayton-lainsaadannon-uudistus',
    'https://ym.fi/documents/1410903/38439968/raportti-rakentamisen-ohjaus-mrln-ja-muun-lainsaadannon-rajapinnat-1DBAB625_10FF_45C5_9708_91AC6A838ED1-95788.pdf/0e569568-3aa6-727f-6c3f-923da092e06c/raportti-rakentamisen-ohjaus-mrln-ja-muun-lainsaadannon-rajapinnat-1DBAB625_10FF_45C5_9708_91AC6A838ED1-95788.pdf?t=1603260472103',
    'https://ym.fi/rakentamismaaraykset',
    'https://ym.fi/rakennusten-energiatehokkuus',
    'https://ym.fi/rakennus-ja-maisemansuojelu',
    'https://ym.fi/kansalliset-kaupunkipuistot',
    'https://ym.fi/rakennustuotteet',
    'https://ym.fi/rakennustuoteasetuksen-paivitys',
    'https://ym.fi/rakennusten-energiatehokkuusdirektiivin-uudistus',
    'https://ym.fi/green-deal-sopimukset',
    'https://kaupunkitilaohje.hel.fi/kortti/julkisen-kaupunkitilan-valaistus/',
    'https://kaupunkitilaohje.hel.fi/kortti/hairiovalo-ja-valosaaste/',
    'https://kaupunkitilaohje.hel.fi/kortti/julkisivu-ja-kohdevalaistus/',
    'https://kaupunkitilaohje.hel.fi/kortti/veistosten-valaistus/',
    'https://kaupunkitilaohje.hel.fi/kortti/asemaymparistojen-valaistus/',
    'https://kaupunkitilaohje.hel.fi/kortti/katu-puistovalaisimien-muotomaaritykset/',
    'https://kaupunkitilaohje.hel.fi/kortti/riippuvalaisimen-muotoilun-laatumaaritykset/',
    'https://kaupunkitilaohje.hel.fi/kortti/historialliset-y-kpv-valaisimet/',
    'https://kaupunkitilaohje.hel.fi/kortti/kausi-ja-jouluvalaistus/',
    'https://kaupunkitilaohje.hel.fi/kortti/valotapahtumat/',
    'https://kaupunkitilaohje.hel.fi/haku/',
    'https://kaupunkitilaohje.hel.fi/kortti/kaupunkitapahtumien-rakenteet/',
    'https://kaupunkitilaohje.hel.fi/kortti/terassit/',
    'https://kaupunkitilaohje.hel.fi/kortti/tyomaa-alueet-rajaaminen-aidat/',
    'https://kaupunkitilaohje.hel.fi/kortti/kaupunkikalusteiden-3d-mallit/',
    'https://kaupunkitilaohje.hel.fi/kortti/kivimateriaalit/',
    'https://kaupunkitilaohje.hel.fi/kortti/uusi-ohjekortti/',
    'https://kaupunkitilaohje.hel.fi/kortti/kokeilusta-ohjeeksi/',
    ' https://kaupunkitilaohje.hel.fi/kortti/katokset-teltat-valiaikaiset-2-viikkoa/',
    'https://wiki.buildingsmart.fi/fi/04_Julkaisut_ja_Standardit/maisema-bim',
    'https://julkaisut.valtioneuvosto.fi/handle/10024/161761'

]
download_files_from_sites(sites_to_scrape_all,fileExtensions)


