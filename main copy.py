import pandas as pd
from validation import Validation


def main():

    academic_sessions_df = pd.read_csv('academic_sessions.csv')
    orgs_df = pd.read_csv('orgs.csv')
    users_df = pd.read_csv('users.csv')
    classes_df = pd.read_csv('classes.csv')
    courses_df = pd.read_csv('courses.csv')

    data_record_status = pd.DataFrame({'id' : [],'action' : [],'description' : []})

    val = Validation()
    
    data_record_status = val.validation_check_empty(academic_sessions_df,'sourcedId','sourcedId',data_record_status,'academic_sessions_df')
    
    print(data_record_status)


if __name__ == "__main__":
    main()




