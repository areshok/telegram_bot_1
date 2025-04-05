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

class TestExample(unittest.TestCase):
    def test_success(self):
        self.assertEqual(1, 1)

    def test_failure(self):
        self.assertEqual(1, 2)

    def test_error(self):
        raise ValueError("Произошла ошибка")



if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=CustomTestResult, verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExample)
    runner.run(suite)

    print("Отчет сохранен в файл custom_test_report.txt")