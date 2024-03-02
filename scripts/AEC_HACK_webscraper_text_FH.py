from selenium import webdriver
import pdfkit

def save_webpage_as_pdf(url, output_path='output.pdf'):
    # Set up the WebDriver (Make sure to replace 'path/to/chromedriver' with the path to your chromedriver executable)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for some time to allow dynamic content to load (you may need to adjust this based on the webpage)
        driver.implicitly_wait(10)

        # Save the webpage as a PDF using pdfkit
        pdfkit.from_file('temp.html', output_path)

    finally:
        # Close the WebDriver
        driver.quit()

# Example usage
save_webpage_as_pdf('https://www.finlex.fi/fi/laki/ajantasa/1973/19730606', 'test.pdf')
