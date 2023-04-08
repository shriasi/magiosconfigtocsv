

class NagiosConfigToCsv:
    def __init__(self, template):
        self.template = template

    def convert_one(self, config_file):
        try:
            return True
        except Exception as er:
            return "Error: Could not convert Nagios config to CSV " + config_file + " using template" \
                   + str(self.template) + "\n ERROR: " + str(er)

    def convert_many(self, config_path):
        try:
            return True
        except Exception as er:
            return "Error: Could not convert Nagios config to CSV in path " + config_path + " using template" \
                   + str(self.template) + "\n ERROR: " + str(er)