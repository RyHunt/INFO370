def ocr(filename):
    import time
    
    timestr = time.strftime("%Y%m%d%-H%M")
    
    try:
    	from PIL import Image
    except ImportError:
    	import Image
    import pytesseract
    
    tesseract_cmd = r'/usr/bin/tesseract'
    
    f = open("./temp/{}.txt".format(timestr), 'w')
    f.write(pytesseract.image_to_string(filename).encode('utf-8').strip())
    f.close()
