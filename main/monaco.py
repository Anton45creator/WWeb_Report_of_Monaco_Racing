from datetime import datetime, timedelta


def build_report(data, asc=True):
    """Return list of drivers results:
        [
         {'driver': 'Sebastian Vettel',
            'car': 'FERRARI',
            'start': Timestamp('2018-05-24 12:02:58.917000'),
            'end': Timestamp('2018-05-24 12:04:03.332000'),
            'time': Timedelta('0 days 00:01:04.415000'),
            'result': '1:04.415'
            'position': 1},
         {'driver': 'Valtteri Bottas',
             'car': 'MERCEDES',
             'start': Timestamp('2018-05-24 12:00:00'),
             'end': Timestamp('2018-05-24 12:01:12.434000'),
             'time': Timedelta('0 days 00:01:12.434000'),
             'result': '1:12.434'
             'position': 2},]"""

    # Reading data and columns filling

    empty_datetime = datetime(1, 1, 1, 0, 0)
    empty_timedelta = timedelta(0)

    drivers = {}

    for line in data['abb'].splitlines():
        values = line.split('_')
        if len(values) < 3:
            continue

        key = values[0]
        drivers[key] = {
            'key': values[0],
            'driver': values[1],
            'car': values[2],
            'start': empty_datetime,
            'end': empty_datetime,
            'time': empty_timedelta,
            'position': 0,
            'disqualifid': False}

    fill_driver_datetime(drivers, data['start'], 'start')

    fill_driver_datetime(drivers, data['end'], 'end')

    fill_driver_time_result(drivers)

    # Make report

    report = []

    for driver in drivers.values():
        report.append(driver)

    report = sorted(report, key=lambda k: k['time'])

    set_driver_position(report)

    # Sorting by settings
    if asc:
        report = sorted(report, key=lambda k: k['position'], reverse=False)
    else:
        report = sorted(report, key=lambda k: k['position'], reverse=True)

    return report


def set_driver_position(report):
    """
    Sets the position of drivers depending on the qualification.
    """
    position = 0
    for record in report:
        if not record['disqualifid']:
            position += 1
            record['position'] = position
        else:
            record['position'] = position + 1


def extract_disqualified(report: list):
    """
    Sorts drivers by lists depending on the qualification completion.
    """
    disqualified = []
    qualified = []
    for record in report:
        if record['disqualifid']:
            disqualified.append(record)
        else:
            qualified.append(record)

    return qualified, disqualified


def fill_driver_datetime(drivers, data_string, field_name):
    """
    Fills in the date and time.
    """
    for line in data_string.splitlines():
        values = line.split('_')
        if len(values) < 3:
            continue

        value_date = values[1]
        value_time = ''.join((values[2], '000'))

        value = ' '.join((value_date, value_time))
        value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')

        key = values[0]
        drivers[key][field_name] = value


def fill_driver_time_result(drivers):
    """
    Calculates the result of the driver's time.
    """
    dis_time = timedelta(days=30)
    dis_result = 'Disqualifid'

    for key, driver in drivers.items():
        if driver['end'] <= driver['start']:
            driver['time'] = dis_time
            driver['result'] = dis_result
            driver['disqualifid'] = True
        else:
            time = driver['end'] - driver['start']
            driver['time'] = time

            minutes = (time.seconds // 60) % 60
            seconds = time.seconds % 60
            ms = time.microseconds

            driver['result'] = f'{minutes}:{str(seconds).zfill(2)}.{str(ms)[:3]}'


def report_qualification(report):
    """
    :param report: List of parameters.
    :return: Qualification results.
    """
    if len(report):
        qualified, disqualified = extract_disqualified(report)

        print(
            f'{"N": <3} | {"DRIVER": <20} | '
            f'{"CAR": <30} | {"BEST LAP": <30}')
        print('-' * 70)

        for record in qualified:
            print(
                f'{str(record["position"]) + ".": <3} | '
                f'{record["driver"]: <20} | {record["car"]: <30} | '
                f'{record["result"]}')
        print('-' * 70)
        if len(disqualified):
            for record in disqualified:
                print(
                    f'{str(record["position"]) + ".": <3} | '
                    f'{record["driver"]: <20} | {record["car"]: <30} | '
                    f'{record["result"]}')


def report_driver(report, driver):
    """
    :param report: List of parameters.
    :param driver: "Driver's name".
    :return: Driver information and results.
    """
    records = [x for x in report if x["driver"] == driver]
    if len(records):
        record = records[0]

        message = f"""
                Key: {record["key"]}
                Driver: {record["driver"]}
                Car: {record["car"]}
                Position: {record["position"]}

                Best lap:
                    start - {record["start"].strftime('%Y-%m-%d %H:%M:%S.%f')
        [:-3]}
                    end - {record["end"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}
                    result: {record["result"]}"""

        print(message.replace('\t', ''))
    else:
        print('Driver not found!')


def print_report(report, driver):
    """
    Output for "build_report" function
    """

    if driver is None:
        report_qualification(report)

    else:
        report_driver(report, driver)
