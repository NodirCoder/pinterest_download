from requests_html import HTMLSession

ZORO_IMG = 'https://pin.it/4zLa0ig5l' # just for testing script
s = HTMLSession()

def get_pin(url: str):
    try:
        resp = s.get(url)
        
        el = resp.html.find('img.hCL.kVc.L4E.MIw')
        img_url = el[0].attrs['src']
        print(el[0].attrs['src']) # PRPRPRPRPRP
        
        resp = s.get(img_url)
        with open('image.jpg', 'wb+') as img:
            img.write(resp.content)
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    pin_url = str(input("[!]Enter a link: "))
    get_pin(pin_url)
