import random
import pickle
import sys
import os


class Brain():
    def __init__(self) -> None:
        """
        This class is designed to facilitate the 
        creation of databases in SQL Server. It is 
        built on standard libraries, takes full 
        care of its file structure, does not require 
        configuration and preparation for work. To 
        work, it is enough to declare a class object 
        and select the desired function.
        
        Variables:
            - self.GeneratedTables:
                The variable in which all generated 
                tables are stored. Updated in a new 
                generation.
            - self.ProfessionalMode:
                When included in the generation, 
                infrequent table attributes will 
                be included.
            - self.TablesWeights:
                Data about tables that can be 
                generated.
            - self.ColumnWeights:
                Data about table attributes, including 
                data type and length.
            - self.FrequencySensitivity:
                ...
        Special thanks to NikitaE30.
        """
        # Paths
        self.PathDumps:    str = "./data/dumps/"
        self.PathTraining: str = "./data/training/"
        self.PathTablesWeights: str = self.PathDumps + "TablesWeights.pkl"
        self.PathColumnWeights: str = self.PathDumps + "ColumnWeights.pkl"
        # Variables
        self.GeneratedTables: list = []
        self.PlatformOS: str = sys.platform
        self.FrequencySensitivity: float = 0.30
        # Directories
        if not os.path.isdir(self.PathDumps):
            os.makedirs(self.PathDumps, exist_ok=True)
        if not os.path.isdir(self.PathTraining):
            os.makedirs(self.PathTraining, exist_ok=True)
        # Loading the scales
        self.ColumnWeights: dict = {}
        self.TablesWeights: dict = {}
        if os.path.isfile(self.PathTablesWeights):
            with open(self.PathTablesWeights, "rb") as ReadDump:
                self.TablesWeights: dict = pickle.load(ReadDump)
        if os.path.isfile(self.PathColumnWeights):
            with open(self.PathColumnWeights, "rb") as ReadDump:
                self.ColumnWeights: dict = pickle.load(ReadDump)
        # Clearing the console
        self._clearing_the_console()
        # Operating mode
        self.ProfessionalMode:  str = self.__user_input("Use professional mode (True/False): ")
        self.ProfessionalMode: bool = bool(self.ProfessionalMode)

    def ManualTrainingModel(self) -> bool:
        """
        The function provides an opportunity
        to train the model. It is enough for 
        the user to enter the data required 
        by the program.
        """
        print("The beginning of model training.")
        while 1:
            # Entering the table name
            TableName: str = self.__user_input("Table name (or Exit): ")
            # End of training
            if TableName == "Exit":
                print("Completion of training..")
                with open(self.PathTablesWeights, "wb") as WriteDump:
                    pickle.dump(self.TablesWeights, WriteDump)
                with open(self.PathColumnWeights, "wb") as WriteDump:
                    pickle.dump(self.ColumnWeights, WriteDump)
                print("Success!")
                return True
            # Entering table fields
            TableFields: str = self.__user_input("Table fields (separated by commas): ")
            ListFields: list = [table.capitalize() for table in TableFields.split(", ")]
            # Updating table data
            if TableName in self.TablesWeights:
                NestedDict: dict = self.TablesWeights[TableName]
                self.TablesWeights[TableName]["all"]: int = NestedDict["all"] + 1
                for field in ListFields:
                    NumberRepetitions: int = 1
                    if field in NestedDict:
                        NumberRepetitions += NestedDict[field]
                    self.TablesWeights[TableName][field]: int = NumberRepetitions
            # Adding table data
            else:
                self.TablesWeights[TableName]: dict = {"all": 1}
                for field in ListFields:
                    self.TablesWeights[TableName][field]: int = 1
            # Updating columns data     
            if TableName in self.ColumnWeights:
                NestedDict: dict = self.ColumnWeights[TableName]
                NestedDict["all"]: int = NestedDict["all"] + 1
                for field in ListFields:
                    DataType:     str = self.__user_input(f"Data type ({field}): ")
                    LengthColumn: str = self.__user_input(f"Column length ({field}): ")
                    if field not in NestedDict["columns"]:
                        NestedDict["columns"][field]: dict = {}
                    if DataType not in NestedDict["columns"][field]:
                        NestedDict["columns"][field][DataType]: dict = {}
                    if LengthColumn not in NestedDict["columns"][field][DataType]:
                        NestedDict["columns"][field][DataType][LengthColumn]: int = 1
                    else:
                        NumberLength: int = NestedDict["columns"][field][DataType][LengthColumn] + 1
                        NestedDict["columns"][field][DataType][LengthColumn]: int = NumberLength
                    self.ColumnWeights[TableName]: dict = NestedDict
            # Adding columns data
            else:
                self.ColumnWeights[TableName]: dict = {"all": 1, "columns": {}}
                for field in ListFields:
                    DataType:     str = self.__user_input(f"Data type ({field}): ")
                    LengthColumn: str = self.__user_input(f"Column length ({field}): ")
                    self.ColumnWeights[TableName]["columns"][field] = {DataType: {LengthColumn: 1}}
            print("Table values updated.")

    def CreatingTables(self) -> bool:
        """
        A function aimed at user interaction 
        with the model. Allows the user to 
        generate the desired tables.
        """
        # Entering table names
        DesiredTables: str = self.__user_input("Desired tables (separated by commas): ")
        TablesNames:  dict = {}
        for table in DesiredTables.split(")"):
            FlagNewUppend: bool = False
            for column in table.split(", "):
                if " (" in column:
                    TableName, column = column.split(" (")
                    TablesNames[TableName]: list = [column]
                    FlagNewUppend: bool = True
                elif not column:
                    continue
                elif not FlagNewUppend:
                    TablesNames[column]: list = []
                else:
                    TablesNames[TableName].append(column)
        # Previous generation cleaning
        self.GeneratedTables: list = []
        # Creating and displaying new tables
        for TableName in TablesNames.keys():
            if TableName in self.TablesWeights:
                self.__create_table(TableName, TablesNames[TableName])
            else:
                print(f"Unable to create table {TableName}.")
        # Displaying tables
        self.__output_tables()
        return True
                     
    def TrainedTables(self) -> bool:
        """
        The function assumes direct interaction. 
        It is used to demonstrate tables that have 
        been embedded in a neural network.
        """
        # Getting table names and checking their availability
        TableNames: set = set(self.TablesWeights.keys())
        if not TableNames:
            print("Unfortunately, there are no tables here.")
            return False
        # Displaying table names
        print("Tables that you may require:")
        LastName: int = len(TableNames)-1
        for tndex, TableName in enumerate(TableNames):
            if tndex == LastName:
                print(f"- {TableName}.")
            else:
                print(f"- {TableName};")
        return True
     
    def AutomaticTrainingModel(self) -> bool:
        """
        The function provides an opportunity 
        to train the model. All files must have 
        utf-8 encoding.
        Returns:
            bool: confirmation.
        """
        print("The beginning of model training.")
        # Checking for files
        if not os.listdir(self.PathTraining):
            print("There are no files for training, cancel.")
            return False
        # Reading files
        TablesProcessed: int = 0
        for file in os.scandir(self.PathTraining):
            with open(file.path, "r", encoding="utf-8") as OpenFile:
                ReadFile:    str = OpenFile.read()
                ReadTables: list = ReadFile.split("\n\n")
            for table in ReadTables:
                TablesProcessed += 1
                FlagUpdate: bool = False
                requisites: list = table.split("\n")
                TableName:   str = requisites[0]
                requisites: list = [requisite.split(" - ") for requisite in requisites[1:]]
                # Entering table fields
                if TableName in self.TablesWeights:
                    FlagUpdate: bool = True
                    NestedDict: dict = self.TablesWeights[TableName]
                    self.TablesWeights[TableName]["all"]: int = NestedDict["all"] + 1
                    for field, __, _ in requisites:
                        NumberRepetitions: int = 1
                        if field in NestedDict:
                            NumberRepetitions += NestedDict[field]
                        self.TablesWeights[TableName][field]: int = NumberRepetitions
                # Adding table data
                else:
                    self.TablesWeights[TableName]: dict = {"all": 1}
                    for field, __, _ in requisites:
                        self.TablesWeights[TableName][field]: int = 1
                # Updating columns data
                if TableName in self.ColumnWeights:
                    NestedDict: dict = self.ColumnWeights[TableName]
                    NestedDict["all"]: int = NestedDict["all"] + 1
                    for field, DataType, LengthColumn in requisites:
                        if field not in NestedDict["columns"]:
                            NestedDict["columns"][field]: dict = {}
                        if DataType not in NestedDict["columns"][field]:
                            NestedDict["columns"][field][DataType]: dict = {}
                        if LengthColumn not in NestedDict["columns"][field][DataType]:
                            NestedDict["columns"][field][DataType][LengthColumn]: int = 1
                        else:
                            NumberLength: int = NestedDict["columns"][field][DataType][LengthColumn] + 1
                            NestedDict["columns"][field][DataType][LengthColumn]: int = NumberLength
                        self.ColumnWeights[TableName]: dict = NestedDict      
                # Adding columns data
                else:
                    self.ColumnWeights[TableName]: dict = {"all": 1, "columns": {}}
                    for field, DataType, LengthColumn in requisites:
                        self.ColumnWeights[TableName]["columns"][field] = {DataType: {LengthColumn: 1}}
                if FlagUpdate:
                    print(f"Updated table {TableName}")
                else:
                    print(f"Added table {TableName}")
        # End of training
        print("Completion of training..")
        print(f"Total tables processed: {TablesProcessed}")
        with open(self.PathTablesWeights, "wb") as WriteDump:
            pickle.dump(self.TablesWeights, WriteDump)
        with open(self.PathColumnWeights, "wb") as WriteDump:
            pickle.dump(self.ColumnWeights, WriteDump)
        print("Success!")
        return True

    def __create_table(self, TableName: str, columns: list) -> bool:
        """
        A system function that is not intended 
        for direct interaction with the user. 
        Used to create the required table.
        Arguments:
            TableName (str): table name.
        """
        # Checking for duplicate table
        for table, _ in self.GeneratedTables:
            if table[0] == TableName:
                return False
        # Variables
        TableDict: dict = self.TablesWeights[TableName]
        TableStructure:  list = [TableName]
        ColumnStructure: list = []
        # Adding an attribute to the table, 
        # taking into account the frequency 
        # of its use.
        for field in TableDict.keys():
            if field == "all":
                continue
            elif field in columns:
                TableStructure.append(field)
            elif self.ProfessionalMode and TableDict[field]/TableDict["all"]<self.FrequencySensitivity:
                continue
            elif TableDict[field] == TableDict["all"]:
                TableStructure.append(field)
            elif random.choices([True, False], weights=[TableDict[field], TableDict["all"]])[0]:
                TableStructure.append(field)
        # Adding characteristics to attributes
        for cndex, column in enumerate(TableStructure):
            if not cndex:
                ColumnStructure.append(["Тип данных", "Длина"])
                continue
            TotalRepetitions:    int = self.ColumnWeights[TableName]["all"]
            AttributeDataTypes: list = []
            for DataType in self.ColumnWeights[TableName]["columns"][column].keys():
                AttributeDataTypes.append(DataType)
            DataType:     str = random.choice(AttributeDataTypes)
            DataLengths: list = []
            for length in self.ColumnWeights[TableName]["columns"][column][DataType].keys():
                DataLengths.append(length)
            WeightValues: list = []
            for length in DataLengths:
                value: float = self.ColumnWeights[TableName]["columns"][column][DataType][length]
                value /= TotalRepetitions
                WeightValues.append(value)
            weight: int = random.choices(DataLengths, weights=WeightValues)[0]
            ColumnStructure.append([DataType, weight])
        # Search for dependent tables
        for field in TableStructure[2:]:
            if "Код " not in field:
                continue
            for key in self.TablesWeights.keys():
                WeightField: str = list(self.TablesWeights[key].keys())[1]
                if WeightField == field:
                    for table, _ in self.GeneratedTables:
                        if table[0] == key:
                            break
                    else:
                        self.__create_table(key, [])
        # Adding a new table
        self.GeneratedTables.append([TableStructure, ColumnStructure])
        return True
                        
    def __output_tables(self) -> bool: 
        """
        This is a system function that does not 
        involve direct interaction. Used to display 
        generated tables.
        """
        # Checking generated tables
        if not self.GeneratedTables:
            return False
        # Variable sizes
        LenghtName:   int = 0
        LenghtType:   int = 0
        LenghtWeight: int = 0
        # Filling in dimensions for displayed tables
        for table, columns in self.GeneratedTables:
            # Name length
            for field in table:
                LenField: int = len(field) + 2
                if LenField > LenghtName:
                    LenghtName: int = LenField
            # Type/Length length
            for Type, Weight in columns:
                LenType:   int = len(Type) + 2
                LenWeight: int = len(Weight) + 2
                if LenType > LenghtType:
                    LenghtType: int = LenType
                if LenWeight > LenghtWeight:
                    LenghtWeight: int = LenWeight
        # Displaying tables
        print()
        HorizontalBorder: str = "|" + "-" * LenghtName + "|"
        HorizontalBorder += "-" * LenghtType   + "|"
        HorizontalBorder += "-" * LenghtWeight + "|"
        for table, column in self.GeneratedTables:
            for tndex, line in enumerate(table):
                # Displaying the upper border
                if not tndex:
                    print(HorizontalBorder)
                # Creating a displayed string
                PrintLine: str = "| " + line
                PrintLine += " " * (LenghtName - len(line) - 1)
                PrintLine += f"| {column[tndex][0]}"
                PrintLine += " " * (LenghtType - len(column[tndex][0]) - 1)
                PrintLine += f"| {column[tndex][1]}"
                PrintLine += " " * (LenghtWeight - len(column[tndex][1])-1)
                PrintLine += "|"
                # Displaying string
                print(PrintLine)
                # Displaying the down border
                if not tndex:
                    print(HorizontalBorder)
        else:
            print(HorizontalBorder)
            print()
        return True

    def __user_input(self, message: str) -> str:
        """
        A system function that does not involve direct 
        interaction. It is used to maintain a uniform 
        type of information entered by the user.
        Arguments:
            message (str): explanation of required data.
        Returns:
            str: user input.
        """
        request: str = input(message)
        if "," in request or "(" in request:
            return request
        if request == request.upper():
            return request
        else:
            return request.capitalize()

    def _author(self) -> str:
        """
        The copyrighted function returns the 
        name of the author of the program.
        Returns:
            str: Name of the author.
        """
        return "NikitaE30"

    def _license(self) -> str:
        """
        The copyrighted function returns the 
        name of the license under which the 
        program is distributed.
        Returns:
            str: Name of the license.
        """
        return "GNU General Public License v3.0"

    def _version(self) -> str:
        """
        The copyrighted function returns the 
        current version of the program.
        Returns:
            str: Program version.
        """
        return "1.2.4"

    def _clearing_the_console(self) -> bool:
        """
        A system function that does not involve direct 
        interaction. It is used to clean up the console.
        Returns:
            bool: confirmation of completion.
        """
        if self.PlatformOS == "linux":
            os.system("clear")
        elif self.PlatformOS == "win32":
            os.system("cls")
        return True 
