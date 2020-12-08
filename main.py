import xml.etree.ElementTree as ET
import os
import json

file_path_1 = os.path.join(os.getcwd(), 'newsafr.xml')
file_path_2 = os.path.join(os.getcwd(), 'newsafr.json')


def find_10_most_common_words(file):
    list_of_descr = []

    def xml_find_every_description():
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(file_path_1, parser)
        root = tree.getroot()
        news_xml = root.findall("channel/item")
        for news in news_xml:
            descr = news.find("description")
            list_of_descr.append(descr.text)
        return(list_of_descr)

    def json_find_every_description():
        with open(file, encoding="utf-8") as f:
            json_data = json.load(f)
        for every_descr in json_data["rss"]["channel"]["items"]:
            list_of_descr.append(every_descr["description"])
        return(list_of_descr)

    def transformation_file():
        list_of_words_in_descr = []
        set_of_descr = set()
        dict_frequency_of_occurrences = {}
        dict_top_of_frequency_of_occurrences = {}
        dict_with_deleted_top_of_frequency_of_occurrences = {}
        list_numerated_top_of_frequency_of_occurrences = []

        for one_descr in list_of_descr:
            one_split_decr = one_descr.split()
            for every_word in one_split_decr:
                list_of_words_in_descr.append(every_word)

        for one_word in list_of_words_in_descr:
            if len(one_word) > 6:
                set_of_descr.add(one_word)

        for one_elem in set_of_descr:
            entry = list_of_words_in_descr.count(one_elem)
            dict_frequency_of_occurrences.setdefault(one_elem, entry)

        dict_with_deleted_top_of_frequency_of_occurrences = dict_frequency_of_occurrences.copy()

        for top in range(10):
            most_common_word = max(dict_with_deleted_top_of_frequency_of_occurrences, key=dict_with_deleted_top_of_frequency_of_occurrences.get)
            for word, frequency in dict_frequency_of_occurrences.items():
                if word == most_common_word:
                    list_numerated_top_of_frequency_of_occurrences.append(f'{word}:{frequency}')
                    del dict_with_deleted_top_of_frequency_of_occurrences[most_common_word]

        print(list_numerated_top_of_frequency_of_occurrences)

    if 'xml' in file:
        xml_find_every_description()
    elif 'json' in file:
        json_find_every_description()
    transformation_file()


find_10_most_common_words(file_path_1)
# find_10_most_common_words(file_path_2)
