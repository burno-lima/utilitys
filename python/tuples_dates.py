from datetime import date, datetime
import pandas as pd


def tuple_dates(data):
    """ Function to return list of two-year date tuples """
    tdy = data  # Ex: date.today() or date(2022,9,9)

    frist_day_month = datetime(tdy.year, tdy.month, 1)

    tuple_dates_start = (
        f"{tdy.replace(year= tdy.year - 2).strftime('%d/%m/%Y')}",
        f"{tdy.replace(day=30, year=tdy.year - 2).strftime('%d/%m/%Y')}"
    )  # start date

    tuple_dates_end = (
        f"{frist_day_month.date().strftime('%d/%m/%Y')}",
        f"{tdy.strftime('%d/%m/%Y')}"
    )  # end date

    years_two = tdy.replace(year=tdy.year - 2)  # two years retroactive

    start_years = date(2022,1,1) 

    monthStart = pd.date_range(years_two, periods=23, freq='MS').strftime("%d/%m/%Y")
    monthEnd = pd.date_range(years_two.replace(month=tdy.month + 1), periods=23, freq='M').strftime("%d/%m/%Y")
    # monthEnd = pd.date_range(years_two, periods=8, freq='M').strftime("%d/%m/%Y")

    list_tuple_dates = [(s, e) for s, e in zip(monthStart, monthEnd)]

    list_tuple_dates.insert(0, tuple_dates_start)

    list_tuple_dates.append(tuple_dates_end)

    return list_tuple_dates


def tuple_moth(data):
    """Function to return a month's date tuple list"""
    tdy = data
    
    oh_one_month = tdy.replace(month=tdy.month -1).strftime('%d/%m/%Y')

    tuple_month = [(
        f"{oh_one_month}",
        f"{tdy.strftime('%d/%m/%Y')}"
    )]

    return tuple_month


if __name__ == '__main__':
    dts = tuple_dates(date.today())
    print(dts)
