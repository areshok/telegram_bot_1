import unittest


class CustomTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.report_file = open("custom_test_report.txt", "w")

    def addSuccess(self, test):
        super().addSuccess(test)
        self.report_file.write(f"Тест {test._testMethodName} УСПЕШНО выполнен\n")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.report_file.write(f"Тест {test._testMethodName} завершился с НЕУДАЧЕЙ: {err[1]}\n")

    def addError(self, test, err):
        super().addError(test, err)
        self.report_file.write(f"Тест {test._testMethodName} завершился с ОШИБКОЙ: {err[1]}\n")

    def stopTestRun(self):
        super().stopTestRun()
        self.report_file.close()