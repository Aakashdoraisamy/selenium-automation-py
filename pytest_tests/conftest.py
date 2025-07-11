def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata['Project Name'] = 'Selenium Automation Suite'
        config._metadata['Tested By'] = 'Aakash D'
        config._metadata['Browser'] = 'Chrome'
        config._metadata['Framework'] = 'pytest with Selenium'
        config._metadata['OS'] = 'Windows 10'

def pytest_html_report_title(report):
    report.title = "Selenium Automation Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["Tested by Aakash D", "UI Automation Summary Report"])
