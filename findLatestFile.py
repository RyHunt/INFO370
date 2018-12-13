def latestTxt():
    import glob
    import os

    list_of_files = glob.glob('./temp/*')
    latest_file_location = max(list_of_files, key=os.path.getctime)
    #latest_file = latest_file_location[1:]
    return(latest_file_location)

def latestImg():
    import glob
    import os

    list_of_files = glob.glob('./images/*')
    latest_file_location = max(list_of_files, key=os.path.getctime)
    latest_file = latest_file_location[1:]
    return(latest_file)
