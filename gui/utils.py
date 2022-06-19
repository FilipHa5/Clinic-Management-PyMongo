from PyQt5 import QtCore
from PyQt5.QtWidgets import QComboBox


def block_parrent_window(self):
    """
    object need to have field named `ui` of type QWidget
    """
    self.ui.setWindowModality(QtCore.Qt.ApplicationModal)
    self.ui.show()


def populate_combo_box(combo_box, items):
    
    for item in items:
        combo_box.addItem(str(item))

def make_str_from_appoinment(docs, db_manager):
    docs_str = ''

    for doc in docs:
        docs_str += make_str_from_type_appointment(doc, db_manager) + '\n'
    return docs_str

def make_str_from_type_appointment(document, db_manager):
    document_str = ''
    #document_str += 'Appointment: ' + document['_id'] + '\n'
    document_str += 'PESEL: ' + str(document['pesel']) + ' '
    '''[document_str + i + ' ' for i in list(db_manager.Patient.find_one(
                                                {'pesel': document['pesel']}, 
                                                {'name':1, 'surname':1, '_id':0}
                                            ).values())]'''
    document_str += 'Time: ' + str(document['time']) + '\n'
    print (document_str)
    return document_str



def make_str_from_documents(docs, db_manager):
    docs_str = ''
    
    for doc in docs:
        docs_str += make_str_from_type(doc, db_manager) + '\n'
    
    return docs_str


def make_str_from_type(document, db_manager):
    document_str = ''
    
    document_str += 'Title: ' + document['title'] + '\n'
    document_str += 'PWZ: ' + str(int(document['pwz'])) + ' '
    document_str += ' '.join([ i for i in list(db_manager.Medician.find_one(
                                                {'pwz': int(document['pwz'])}, 
                                                {'name':1, 'last_name':1, '_id':0}
                                            ).values())]) + '\n'
    document_str += 'PESEL: ' + str(int(document['pesel'])) + ' '
    document_str += ' '.join([ i for i in list(db_manager.Patient.find_one(
                                                {'pesel': int(document['pesel'])}, 
                                                {'name':1, 'last_name':1, '_id':0}
                                            ).values())]) + '\n'
    document_str += 'Creation date: ' + str(document['creation_date']) + '\n'
    document_str += parse_from_type(document)
    
    return document_str


def parse_from_type(document):
    
    if document['type'] == 'description':
        output_str = parse_description(document)
    if document['type'] == 'prescription':
        output_str = parse_prescription(document)
    if document['type'] == 'referral':
        output_str = parse_referral(document)
    
    return output_str


def parse_description(doc):
    output = ''
    output += 'Subjective examination: ' + doc['subjective_examination'] + '\n'
    output += 'Physical examination: ' + doc['physical_examination'] + '\n'
    output += 'Recomendations: ' + doc['recomendations'] + '\n'
    return output


def parse_prescription(doc):
    output = 'Number: '
    output += str(int(doc['number'])) + '\n'
    output += 'Drugs list:\n'
    for drug in doc['drugs_list']:
        output += '\t' + drug + '\n'
    return output


def parse_referral(doc):
    output = 'Number: '
    output += str(int(doc['number'])) + '\n'
    output += 'Destination specialization: ' + doc['destination_specialization'] + '\n'
    output += 'Purpose: ' + doc['purpose'] + '\n'
    return output


