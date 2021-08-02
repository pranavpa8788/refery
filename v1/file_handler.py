import os

class File_Handler :

    def __init__(self, image_directory) : 

        self.image_directory = image_directory

        self.image_extensions = [
        '.bmp', 
        '.dib', 
        '.gif', 
        '.jpg', 
        '.jpeg',
        '.jpe', 
        '.jif', 
        '.jfif',
        '.jfi', 
        '.png', 
        '.pbm', 
        '.pgm', 
        '.ppm', 
        '.xbm', 
        '.xpm' 
        ]

        self.extension_valid = False

        self.file_processor()

        # print(self.file_dictionary)

        self.clean_file_dictionary()

    def file_processor(self) : 

        self.file_dictionary = {}

        self.directory_list = list(os.walk(self.image_directory))

        for directory in range(1, len(self.directory_list)) : 

            # print(self.directory_list[directory])

            self.directory_name = self.directory_list[directory][0]

            self.file_dictionary[self.directory_name] = []
            
            for file_ in range(len(self.directory_list[directory][-1])) :

                self.extension_valid = False

                self.file_name = self.directory_list[directory][-1][file_]
                    
                for word in self.image_extensions : 

                    # print(f'File_name : {self.file_name}, {self.file_name.endswith(word)}')

                    if self.file_name.endswith(word) : 

                        self.extension_valid = True

                        break

                if self.extension_valid == True :

                    self.file_dictionary[self.directory_name].append(self.file_name)

    def clean_file_dictionary(self) :

        del_list_keys = []

        for key in self.file_dictionary.keys() :

            if self.file_dictionary[key] == [] :

                del_list_keys.append(key)

        for key in del_list_keys : 

            del self.file_dictionary[key]


if __name__ == '__main__' : 

    fh = File_Handler('Images/')
    
    print(fh.file_dictionary)
