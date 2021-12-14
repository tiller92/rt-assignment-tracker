# central python dict will cont all RT's and then keep points based of where
# they are at in the excel sheet. Use boolean for there core teams, floors,
# and other. To get the assignemnt the charge could paste the file location
# intp an inpit and then click submit. On submit use python to read the exel
# and then place the points accoringly. Decide with team wether it should be
# monthly or per schedule period.

import openpyxl 

# list of RT's and there units recent counts however often carlee or jenn decides 
RTS = {
        "ryan":{"MICU":0,
            "NICU":0,
            "10ICU":0,
            "other":0,
            "floors":0,
            },
        "nick c":{"MICU":0,
        "other":0,
        "floors":0,
        },
        "scott":{
            "MICU":0,
            "other":0,
            "floors":0,
        },
        "mona":{
            "SICU":0,
            "other":0,
            "floors":0,
        },
        "sammie":{
            "floors":0,
        },
        "christina":{
            "floors":0,
        },
        "laura":{
            "floors":0,
        },
        "sara":{
            "floors":0,
        },
}

def excel_break(file):
    """this functon shoule take the assignment and break down who is here and where they where assigned. File will come from a folder that the charge places the current assignment list in"""
    # path = f"/Users/ryantiller/Desktop/rt-assignment-project/current-assignment/{file}"
    path = file

    #To open the workbook
    # workbook object is created
    wb_obj = openpyxl.load_workbook(path)
    
    # Get workbook active sheet object
    # from the active attribute
    sheet_obj = wb_obj.active
    
    # Cell objects also have a row, column,
    # and coordinate attributes that provide
    # location information for the cell.

    # Note: The first row or
    # column integer is 1, not 0.

    # Cell object is created by using
    # sheet object's cell() method.
    cell_obj = sheet_obj.cell(row = 2, column = 2)

    # Print value of cell object
    # using the value attribute
    print(cell_obj.value)
    print('*****')
    print(sheet_obj.max_column, 'columns')
    print('*****')
    print(sheet_obj.max_row, 'rows')
    print('******')
    
    MICU = [sheet_obj.cell(row= 3, column=5),sheet_obj.cell(row= 4, column=5),sheet_obj.cell(row= 5, column=5)]
    
    FLOORS = [sheet_obj.cell(row= 15, column=12),sheet_obj.cell(row= 16, column=12),sheet_obj.cell(row= 17, column=12),sheet_obj.cell(row= 18, column=12),sheet_obj.cell(row= 19, column=12),sheet_obj.cell(row= 20, column=12),sheet_obj.cell(row= 21, column=12),sheet_obj.cell(row= 22, column=12),]

    #make a filtered list that is just strings
    floors = []
    for i in FLOORS:
        if str(i.value) and i.value != None:
            floors.append(i.value)
    
    for x in floors:
        name_lower = x.lower()
        if RTS[name_lower]:
            RTS[name_lower]["floors"] +=1
            print(x, "was on the floors")

    for x,y in RTS.items():
        print(x,y)
    
    
    ## maybe just start with floor assignemtns
    return RTS

def floor_shifts(rt_dict=RTS):
    """creat a list if tuples with name and number of floor shifts"""
    floors_percent = []
    for x,y in RTS.items():
        print((RTS[x]['floors'],x))

    
def createRT(rts_dict, name, list_of_core_teams):
    """add an rt to the RTS dict"""
    return None

