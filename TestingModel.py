import TablesFromNikita


if __name__ == "__main__":
    core = TablesFromNikita.Brain()
    while 1:
        FunctionUnderTest: str = input("Specify the function for the test (or Help): ")
        FunctionUnderTest: str = FunctionUnderTest.capitalize()
        if FunctionUnderTest == "Help":
            print()
            print("The following functions are available for testing:")
            print("    1. ManualTrainingModel (manual model training);")
            print("    2. TrainedTables (trained tables);")
            print("    3. AutomaticTrainingModel (automatic model training);")
            print("    4. UseModel (launch the model);")
            print("    5. Exit (exit the program);")
            print("    6. Clear (Clear the console).")
            print("Specify the number or name of the function.")
            print()
        if FunctionUnderTest in ("1", "ManualTrainingModel"):
            core.ManualTrainingModel()
        if FunctionUnderTest in ("2", "TrainedTables"):
            core.TrainedTables()
        if FunctionUnderTest in ("3", "AutomaticTrainingModel"):
            core.AutomaticTrainingModel()
        if FunctionUnderTest in ("4", "UseModel"):
            core.CreatingTables()
        if FunctionUnderTest in ("5", "Exit"):
            print("Completion of testing")
            break
        if FunctionUnderTest in ("6", "Clear"):
            core._clearing_the_console()