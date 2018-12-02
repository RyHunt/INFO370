def pdfConvert():
    from pdf2image import convert_from_path
    import os, linecache, time
    
    pdfpath = './uploads/sales.pdf'
    output = './images'
    format = 'png'
    timestr = time.strftime("%Y%m%d%-H%M")
    
    images_from_path = convert_from_path(pdfpath, output_folder=output, fmt=format)

