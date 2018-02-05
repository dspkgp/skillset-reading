import os
import xlrd

EXCEL_FILE_NAME = 'MyBookExcel.xlsx'
EXCEL_FILE_PATH = os.path.join(os.getcwd(), EXCEL_FILE_NAME)
SPACE_COUNTER = 10


def get_sheet(sheet_number):
    wb = xlrd.open_workbook(EXCEL_FILE_PATH)

    return wb.sheet_by_index(sheet_number)


def parse_excel_to_dictionary(sheet):
    mapping = {}

    for i in range(1,sheet.nrows):
        main_key = sheet.cell_value(i,0)
        mapping.update({main_key : {}})

        for j in range(1,sheet.ncols):
            key = sheet.cell_value(0, j)
            value = sheet.cell_value(i, j)

            mapping[main_key].update({key : value})

    return mapping


def parse_role_and_skillset_sheet(sheet):
    role_to_skillset_mapping = {}
    ROLE_ROW_INDEX_TO_ROLE_MAPPING = {}

    for j in range(sheet.ncols):
        if j == 0:
            for i in range(0, sheet.nrows, SPACE_COUNTER):
                ROLE_NAME = sheet.cell_value(i, j)
                role_to_skillset_mapping.update({ROLE_NAME : {}})
                ROLE_ROW_INDEX_TO_ROLE_MAPPING.update({i : ROLE_NAME})

        if j != 0:
            for i in range(0, sheet.nrows, SPACE_COUNTER):
                SKILL_NAME = sheet.cell_value(i, j)
                role_name = ROLE_ROW_INDEX_TO_ROLE_MAPPING[i]
                if SKILL_NAME:
                    role_to_skillset_mapping[role_name].update({SKILL_NAME : []})
                for number in range(i+1,i+SPACE_COUNTER):
                    try:
                        output1 = sheet.cell_value(number,j)
                    except:
                        output1 = ''

                    if output1:
                        role_to_skillset_mapping[role_name][SKILL_NAME].append(output1)

    return role_to_skillset_mapping


def get_role_data():
    sheet = get_sheet(1)

    return parse_excel_to_dictionary(sheet)


def get_skillset_data():
    sheet = get_sheet(2)

    return parse_excel_to_dictionary(sheet)


def get_skill_data():
    sheet = get_sheet(3)

    return parse_excel_to_dictionary(sheet)


def get_role_to_skillset_mapping():
    sheet = get_sheet(0)

    return parse_role_and_skillset_sheet(sheet)
