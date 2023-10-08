import TablesFromNikita


if __name__ == "__main__":
    core = TablesFromNikita.Brain()
    while 1:
        FunctionUnderTest: str = input("Specify the function for the test (or Help/Exit): ")
        FunctionUnderTest: str = FunctionUnderTest.capitalize()
        if FunctionUnderTest == "help":
            print()
            print("The following functions are available for testing:")
            print("    1. ManualTrainingModel")
            print("    2. TrainedTables")
            print("    3. AutomaticTrainingModel")
            print("    4. UseModel")
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
        if FunctionUnderTest == "Exit":
            print("Completion of testing")
            break

