import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    def __init__(self, filename):
        """
        Initializes a filename and a directory name that will be used.
        :param filename: str
        """
        self.filename = filename
        self.temp_directory = Path("unzipped-{}".format(filename[:-4]))

    def process_zip(self):
        """
        Main method for processing.
        :return: None
        """
        self.unzip_files()
        #self.process_files()
        self.zip_files()

    def unzip_files(self):
        """
        Unzips the archive, putting all of its files in a temporary directory.
        :return: None
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as archive:
            archive.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        Zips the archive back together from the temporary directory.
        :return: None
        """
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
