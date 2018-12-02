def rename_pdf():
    import os, linecache, time
    
    path = './uploads/'
    
    timestr = time.strftime("%Y%m%d%-H%M")
    
    filenames = os.listdir(path)
    
    for filename in filenames:
        if not filename.startswith('20'):
            src = path + filename
            dst = path + '{}.pdf'.format(timestr)
            os.rename(src,dst)
            return()

def rename_png():
    import os, linecache, time
    
    path = './images/'
    
    timestr = time.strftime("%Y%m%d%-H%M")
    
    filenames = os.listdir(path)
    
    for filename in filenames:
        if not filename.startswith('20'):
            src = path + filename
            dst = path + '{}.png'.format(timestr)
            os.rename(src,dst)
            return(dst)