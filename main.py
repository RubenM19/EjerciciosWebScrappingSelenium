import selenium
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service  # Import the Service class
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.imdb.com/chart/top/'

driver_path = r'C:\Users\ruben\Desktop\SELENIUM\msedgedriver.exe'  # Adjust path as needed
service = Service(driver_path)
driver = webdriver.Edge(service=service)  # Use the Service object

driver.get(url)

title_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[1]/a/h3'))
)
ranking_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[1]/a/h3'))
)
link_movie_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[1]/a'))
)
link_picture_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[1]/div/div[2]/img'))
)
year_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[1]'))
)
views_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/span/div/span/span'))
)
stars_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/span/div/span'))
)
title = title_element.text[2:]
ranking = ranking_element.text[:1]
href_movie = link_movie_element.get_attribute("href")
href_picture = link_picture_element.get_attribute("src")
year = year_element.text
views = views_element.text
stars = stars_element.text
desired_stars = stars.split(" ")[0]
driver.quit()
print("El título de la película es: "+title)
print("El puesto del ranking que ocupa es: "+ranking) 
print("El link del detalle de la película es: "+href_movie) 
print("El link de la imagen de la película es: "+href_picture) 
print("El anio es: "+year) 
print("Cantidad de vistas: "+views) 
print("Estrellas: "+desired_stars) 