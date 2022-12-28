import unittest
import UploadFiles
#import filelocation
import pyodbc

server = 'HCL-02-18\SQLEXPRESS'
database = 'FileSearchResults'
username = 'vyshu'
password = 'Vyshu@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class test_capstone(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass
    def test_upload_file_results_todb(self):
        uploadObj = UploadFiles.UploadFilesToDB()
        #fileObj = filelocation.FindFileLocation()
        uploadObj.upload_file_results_todb("dummytestcasefile.txt","C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\dummy\\dummytestcasefile.txt",0)
        #uploadObj.upload_file_results_todb("test.txt","C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\test.txt", 0)

        values_1 = cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'dummytestcasefile.txt' ''')

        #values_2 = cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'test.txt' ''')
        for fileInfo in values_1:

            self.assertEqual(fileInfo.NameOfFile, "dummytestcasefile.txt")
            self.assertEqual(fileInfo.File_Location, "C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\dummy\\dummytestcasefile.txt")

    """def test_upload_file_results_todb(self):
        uploadObj = UploadFiles.UploadFilesToDB()
        #fileObj = filelocation.FindFileLocation()
        uploadObj.upload_file_results_todb("test.txt",
                                           "C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\test.txt", 0)


        values_2 = cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'test.txt' ''')

        for fileInfo1 in values_2:
            self.assertEqual(fileInfo1.NameOfFile, "test.txt")
            self.assertEqual(fileInfo1.File_Location, "C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\test.txt")

    def test_search_in_db_for_file(self):
        searchObj = UploadFiles.UploadFilesToDB()
        searchObj.search_in_db_for_file('demo.txt')
        value_1=cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'demo.txt' ''')
        for fileInfo in value_1:
            self.assertEqual(fileInfo.NameOfFile,'demo.txt')"""
""" def test_update_file_searchcount(self):
        searchCountObj = UploadFiles.UploadFilesToDB()
        searchCountObj.update_file_searchcount('demo.txt')
        values = cursor.execute(''' select * from FileSearchResults_table where NameOfFile ='demo.txt' ''')

        for fileInfo in values:
            fileSearchCount = fileInfo.SearchCount
            print(fileSearchCount)

            fileinfoQuery = cursor.execute('''
                    Update FileSearchResults_table SET SearchCount = {} WHERE NameOfFile = {} ''')
            updateQuery = fileinfoQuery.format(fileSearchCount + 1, 'demo.txt')
            cursor.execute(updateQuery)
            # commits data to DB

            self.assertEqual(fileInfo.SearchCount,1)"""


        
        
if __name__ == "__main__":
    unittest.main()