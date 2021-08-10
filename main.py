import xml.etree.ElementTree as ET


class ConfigParser:
    def __init__(self, file_name='conf/config.xml', config_tag='config', tag='file'):
        self.tree = ET.parse(file_name)
        if self.tree.getroot().tag == config_tag:
            self.config = self.tree
        else:
            self.config = self.tree.find(config_tag)

        self.elements = self.config.findall(tag)

    def get_elements(self):
        return self.elements


class CopyFile:
    def __init__(self):
        pass

    def copy_files(self, files):
        for file in files:
            self.copy_file(file)

    def copy_file(self, file):
        try:
            settings = self.get_settings(file)
            with open(settings['source_path'] + '\\' + settings['file_name'], 'rb') as file_from:
                with open(settings['destination_path'] + '\\' + settings['file_name'], 'wb') as file_to:
                    file_to.write(file_from.read())

        except KeyError as ke:
            print('Error to find necessary file attribute: ' + str(ke))
        except FileNotFoundError:
            print('No such file ' + settings['source_path'] + '\\' + settings['file_name'])
        except Exception:
            print('Fatal error')


    def get_settings(self, file):
        items = file.items()
        settings = {}
        for item in zip(items):
            item = item[0]
            settings[item[0]] = item[1]
        return settings


if __name__ == '__main__':
    parser = ConfigParser()
    cp = CopyFile()
    cp.copy_files(parser.get_elements())
