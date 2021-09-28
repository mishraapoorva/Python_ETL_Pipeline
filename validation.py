import pandas as pd
import numpy as np
from validate_email import validate_email


class Validation():

    def __init__(self) -> None:
        pass

    def validate_empty(self, dataFrame, col, sId, status_df, filename='Unknown_file'):
        '''
        check for empty value in the dataframe with column
        '''
        try:

            df = dataFrame[dataFrame[col].isnull()]
            row_status = {}
            # print(df)
            if not df.empty:
                for index, row in df.iterrows():
                    desc = 'FileName_'+ filename + ' RowNumber_' + str(index)
                    row_status = {
                        'id': row[sId], 'action': 'Rejected - Empty', 'description': desc}
                    status_df = status_df.append(row_status, ignore_index=True)
                print(f"validate_empty_values run Succesfully!!")
                dataFrame = dataFrame[np.invert(dataFrame[col].isnull())]

                return status_df, dataFrame
            print(f"validate_empty run Succesfully!!")
            return status_df, dataFrame

        except Exception as e:
            print(f"Error in the validate_empty")
            print(f'Error - {e}')

    def validate_non_unique(self, dataFrame, col, sId, status_df, filename='Unknown_file'):
        '''
        check for empty value in the dataframe with column
        '''
        try:
            df = dataFrame[dataFrame.duplicated(subset=[col])]
            row_status = {}
            # print(df)
            if not df.empty:
                for index, row in df.iterrows():
                    desc = 'FileName_'+filename + '_RowNumber_' + \
                        str(index) + '_Column_' + col
                    row_status = {
                        'id': row[sId], 'action': 'Rejected - NOT UNIQUE', 'description': desc}
                    status_df = status_df.append(
                        row_status, ignore_index=True)
                dataFrame = dataFrame[np.invert(
                    dataFrame.duplicated(subset=[col]))]
                return status_df, dataFrame
            return status_df, dataFrame

        except Exception as e:
            print(f"Error in the validate_non_unique")
            print(f'Error - {e}')

    def validate_email(self, dataFrame, col, sId, status_df, filename='Unknown_file'):
        '''
        check for empty value in the dataframe with column
        '''
        try:
            df = dataFrame[np.invert(dataFrame[col].apply(validate_email))]
            row_status = {}
            # print(df)
            if not df.empty:
                for index, row in df.iterrows():
                    desc = 'FileName_'+filename + '_RowNumber_' + \
                        str(index) + '_Column_' + col
                    row_status = {
                        'id': row[sId], 'action': 'Rejected - NOT UNIQUE', 'description': desc}
                    status_df = status_df.append(
                        row_status, ignore_index=True)
                dataFrame = dataFrame[dataFrame[col].apply(validate_email)]
                return status_df, dataFrame
            return status_df, dataFrame

        except Exception as e:
            print(f"Error in the validate_email")
            print(f'Error - {e}')

    def validate_orgs_id(self, dataFrame, orgs_df, col, sId, status_df, filename='Unknown_file'):
        '''
        check for empty value in the dataframe with column
        '''
        try:
            if str(orgs_df['sourcedId'].dtype) == "object":
                orgs_df['sourcedId'] = orgs_df['sourcedId'].apply(
                    lambda x: int(x.strip("'")))
            if str(dataFrame[col].dtype) == "object":
                dataFrame[col] = dataFrame[col].apply(
                    lambda x: int(x.strip("'")))

            df = dataFrame[np.invert(
                dataFrame[col].isin(orgs_df['sourcedId']))]
            row_status = {}
            if not df.empty:
                for index, row in df.iterrows():
                    desc = 'FileName_'+filename + '_RowNumber_' + \
                        str(index) + '_Column_' + col
                    row_status = {
                        'id': row[sId], 'action': 'Rejected - INVALID ORG REF', 'description': desc}
                    status_df = status_df.append(
                        row_status, ignore_index=True)
                dataFrame = dataFrame[dataFrame[col].isin(orgs_df['sourcedId'])]
                return status_df, dataFrame
            return status_df, dataFrame

        except Exception as e:
            print(f"Error in the validate_orgs_id")
            print(f'Error - {e}')

    def validate_course_credit(self, dataFrame, col, sId, status_df, filename='Unknown_file'):
        '''
        check for empty value in the dataframe with column
        '''
        try:
            df_fixed = dataFrame[dataFrame[col].str.contains("'", regex=False)]

            for index, row in df_fixed.iterrows():
                desc = 'FileName_'+filename + '_RowNumber_' + \
                    str(index) + '_Column_' + col
                row_status = {
                    'id': row[sId], 'action': 'Fixed - removed Quotes', 'description': desc}
                status_df = status_df.append(row_status, ignore_index=True)


            if str(dataFrame[col].dtype) == "object":
                dataFrame[col] = dataFrame[col].apply(lambda x: x.strip("'"))
        #print(dataFrame[col])

            for index, row in dataFrame.iterrows():
                try:
                    dataFrame[col][index] = float(dataFrame[col][index])
                except Exception as e:
                    print(f"Error in cleaning needs to rejected - {e}")
                    desc = 'FileName_'+filename + '_RowNumber_' + \
                        str(index) + '_Column_' + col
                    row_status = {
                        'id': row[sId], 'action': 'Rejected - INVALID CREDIT', 'description': desc}
                    status_df = status_df.append(row_status, ignore_index=True)
                    dataFrame = dataFrame.drop(index)
            return status_df, dataFrame

        except Exception as e:
            print(f"Error in the validate_course_credit")
            print(f'Error - {e}')

    def normalize_validate_date(self, dataFrame, col, sId, status_df, filename='Unknown_file'):
        '''
        check for valid dates in the dataframe on date
        '''
        try:
            df = dataFrame.copy(deep=True)
            dataFrame[col] = pd.to_datetime(dataFrame[col], errors='coerce')
            dataFrame[col] = dataFrame[col].dt.date
            row_status = {}
            df_rejected = df[dataFrame[col].isnull()]
            dataFrame = dataFrame[np.invert(dataFrame[col].isnull())]
            if not df_rejected.empty:
                for index, row in df_rejected.iterrows():
                    desc = 'FileName_'+filename + ' RowNumber_' + str(index)
                    row_status = {
                        'id': row[sId], 'action': 'Rejected - INVALID DATE', 'description': desc}
                    status_df = status_df.append(
                        row_status, ignore_index=True)
                return status_df, dataFrame
            return status_df, dataFrame

        except Exception as e:
            print(f"Error in the normalize_validate_date")
            print(f'Error - {e}')


    def validate_date(self, dataFrame, start, end, sId, status_df, filename='Unknown_file'):
        '''
        check for valid dates in the dataframe on date
        '''
        try:
            df = dataFrame.copy(deep=True)
            date_df = (dataFrame[end] - dataFrame[start]).astype(int)
            df_rejected = dataFrame[date_df<0]
            row_status = {}
            if not df_rejected.empty:
                for index, row in df_rejected.iterrows():
                    desc = 'FileName_'+filename + ' RowNumber_' + str(index) + 'start date is greater than end date'
                    row_status = {
                        'id': row[sId], 'action': 'Rejected_invalid_Date', 'description': desc}
                    status_df = status_df.append(
                        row_status, ignore_index=True)
                dataFrame = dataFrame[date_df>0]
                return status_df, dataFrame
            return status_df, dataFrame

        except Exception as e:
            print(f"Error in the validate_date")
            print(f'Error - {e}')

