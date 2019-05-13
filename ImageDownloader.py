# load library
import urllib
import os
import csv
import datetime
import codecs

# set real path parameters
class DirectoryPath:
    def __init__(self):
        self.current_directory = ''
        self.urls_csv_file = ''
        self.image_file = ''
        self.new_csv_file = ''
        self.log_file_path = ''

    # get current real path
    def getCurrentDirectory(self):
        try:
            self.current_directory = os.getcwd()
            if not os.path.isdir(self.current_directory):
                self.current_directory = input("Enter Current Filepath\n>>\t")
        except Exception as err:
            writeLog("ERROR: getCurrentDirectory: {}".format(err))

    # set paths in use
    def setFilePathes(self):
        self.getCurrentDirectory()
        self.urls_csv_file = self.current_directory + "\imageurls.csv"
        self.image_file = self.current_directory + "\images"
        self.new_csv_file = self.current_directory + "\downloaded.csv"
        self.log_file_path = self.current_directory + "\log.txt"    

   # get urls from csv file
   # if failed, get new file name and try again
    def getImageUrls(self): 
        try:
            with codecs.open(self.urls_csv_file,"rb", "utf-16") as f:
                writeLog("imageurls.csv file opened")
                for line in csv.reader(f):
                    url = line[0] #.replace('\0', '')
                    yield url
        except Exception as err:
            writeLog("ERROR: Failed to Read \'" + self.urls_csv_file + "\': {}".format(err))
            self.urls_csv_file = self.current_directory + input("Re-enter Image Urls File Name.\n>>\t")
            self.getImageUrls()       

    # if urls file not exist, alert
    def isUrlsExist(self):
        if not os.path.exists(self.urls_csv_file):
            writeLog("Error: No imageurls.csv")
            return False
        else:
            return True

path = DirectoryPath()
path.setFilePathes()

# download image from url
def download(image_url, out_path):
    try:
        # file path and file name to download
        url_splitter = image_url.split('/')
        out_file = url_splitter[-1]

        # verify filename extension - download image file only
        out_splitter = out_file.split('.')
        file_type = out_splitter[-1]
        filenames = ['jpg', 'img', 'png', 'JPG', 'IMG', 'PNG']
        if filenames.count(file_type)==0:
            return False

        # Create when directory does not exist
        if not os.path.isdir(out_path):
            os.makedirs(out_path)

        # download
        urllib.urlretrieve(image_url, out_path+"\\"+out_file)   
        return True

    except Exception as err:
        writeLog("ERROR: download: {}".format(err))
        return False

def writeLog(message):
    with open(path.log_file_path, 'a+') as f:
        f.write(str(datetime.datetime.now()) + "\t" + str(message) + "\n")
    
def main():
    if path.isUrlsExist():
        imageUrls = path.getImageUrls()
        f = codecs.open(path.new_csv_file, 'w', "utf-16")
        csv_writer = csv.writer(f)
        for url in imageUrls: 
            if download(url, path.image_file):
                csv_writer.writerow([url, 'Success'])
            else:
                csv_writer.writerow([url, 'Fail'])   
        f.close()
        writeLog("Proccess Success!")
    else:
        writeLog("Proccess Failed!")

if __name__=="__main__":
    main()
