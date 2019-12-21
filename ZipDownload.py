from __future__ import print_function
import os
from urllib2 import urlopen, URLError, HTTPError
from zipfile import ZipFile


__author__ = "Ashutosh Narayan Jha"
__copyright__ = "Copyright 2019, IgnitedPeople"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ashutosh Narayan Jha"
__status__ = "Development"

class ZipDownload(object):
    def __init__(self, sourceUrl, target):
        self.sourceUrl = sourceUrl;
        self.target = target;

    def download(self) :
        #print("Given source url is {0} and local target directory is {1}".format(self.sourceUrl, self.target));
        outputFilePath = os.path.join(self.target, os.path.basename(self.sourceUrl));
        try:
            fObj = urlopen(self.sourceUrl); # Refer https://docs.python.org/2/library/urllib2.html#urllib2.urlopen

            print ("downloading " + self.sourceUrl)

            # Open our local file for writing
            with open(outputFilePath, "wb") as local_file:
                local_file.write(fObj.read())

       #handle errors
        except HTTPError, e:
            print ("HTTP Error:", e.code, self.sourceUrl);
        except URLError, e:
            print ("URL Error:", e.reason, self.sourceUrl);
        
       # Call zipExtractor.
        ZipDownload.extractZip(outputFilePath, os.path.join(self.target, ''));

    @staticmethod
    def extractZip(fullFilePath, targetDir):
        print (targetDir);
        with ZipFile(fullFilePath, 'r') as zip: 
            zip.printdir(); # printing all the contents of the zip file 

            print('Extracting files at: ' + targetDir) 
            zip.extractall(targetDir);
            print('Extracted!');

# If this file is called directly.
if __name__ == "__main__":
    from optparse import OptionParser
    # Get source and destination parameters.
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="sourceUrl", help="Source URL to download ", metavar="string")
    parser.add_option("-t", "--target", dest="target", help="Local system path", metavar="string")
    (opt, args) = parser.parse_args();
    if opt.sourceUrl is None :
        print ('Source URL is required. Pass it along with -s or --source option.')
        exit (1);

    if opt.target is None :
        print ('Please provid target where file is to be saved. Pass it along with -t or --target.')
        exit (1);

    downloader = ZipDownload(opt.sourceUrl, opt.target);
    downloader.download();




