import pandas as pd
from validation import Validation


def main():

    orgs_df = pd.read_csv('orgs.csv')
    users_df = pd.read_csv('users.csv')
    classes_df = pd.read_csv('classes.csv')
    courses_df = pd.read_csv('courses.csv')
    academic_sessions_df = pd.read_csv('academic_sessions.csv')

    data_record_status = pd.DataFrame({'id' : [],'action' : [],'description' : []})

    val = Validation()

    # academic session table
    
    #validate sourceId to exclude null values
    data_record_status, academic_sessions_df_val = val.validate_empty(academic_sessions_df,'sourcedId','sourcedId',data_record_status,'academic_sessions_df')

    #validate sourceId to exclude non unique values
    data_record_status, academic_sessions_df_val = val.validate_non_unique(academic_sessions_df_val,'sourcedId','sourcedId',data_record_status,'academic_sessions_df')

    #normalize startDate to format YYYY-MM-DD
    data_record_status, academic_sessions_df_val = val.normalize_validate_date(academic_sessions_df,'startDate','sourcedId',data_record_status,'academic_sessions_df')

    #normalize endDate to format YYYY-MM-DD
    data_record_status, academic_sessions_df_val = val.normalize_validate_date(academic_sessions_df_val,'endDate','sourcedId',data_record_status,'academic_sessions_df')

    #validate dates to exclude end date greater than start date
    data_record_status, academic_sessions_df_val = val.validate_date(academic_sessions_df_val,'startDate','endDate','sourcedId',data_record_status,'academic_sessions_df')

    # orgs
    
    #validate sourceId to exclude null values
    data_record_status, orgs_df_val = val.validate_empty(orgs_df,'sourcedId','sourcedId',data_record_status,'orgs_df')

    #validate sourceId to exclude non unique values
    data_record_status, orgs_df_val = val.validate_non_unique(orgs_df_val,'sourcedId','sourcedId',data_record_status,'orgs_df')

    # users_df

    #validate sourceId to exclude null values
    data_record_status, users_df_val = val.validate_empty(users_df,'sourcedId','sourcedId',data_record_status,'users_df')

    #validate sourceId to exclude non unique values
    data_record_status, users_df_val = val.validate_non_unique(users_df_val,'sourcedId','sourcedId',data_record_status,'users_df')
   
    #validate email to exclude 
    data_record_status, users_df_val = val.validate_email(users_df_val,'email','sourcedId',data_record_status,'users_df')

    #validate orgSourcedId to exclude bad references
    data_record_status, users_df_val = val.validate_orgs_id(dataFrame=users_df_val, orgs_df=orgs_df_val, col='orgSourcedId', sId='sourcedId',status_df=data_record_status, filename='users_df')


    #courses_df
    
    #validate sourceId to exclude null values
    data_record_status, courses_df_val = val.validate_empty(courses_df,'sourcedId','sourcedId',data_record_status,'courses_df')

    #validate sourceId to exclude non unique values
    data_record_status, courses_df_val = val.validate_non_unique(courses_df_val,'sourcedId','sourcedId',data_record_status,'courses_df')
    
    #validate course credit to accept decimal values
    data_record_status, courses_df_val = val.validate_course_credit(courses_df_val,'courseCredit','sourcedId',data_record_status,'courses_df')

    #validate orgSourcedId to exclude bad references
    data_record_status, courses_df_val = val.validate_orgs_id(dataFrame=courses_df_val, orgs_df=orgs_df_val, col='orgSourcedId', sId='sourcedId',status_df=data_record_status, filename='courses_df')

    print(data_record_status['description'])

if __name__ == "__main__":
    main()




