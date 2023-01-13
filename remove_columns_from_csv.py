import pandas as pd

cols2keep = ['RegistraionId','TraineeID','Gender','ApprenticePostcode','BusinessRelationship','BusinessRelationshipDetails','GovernmentAssistance','IntensiveSupport','EmployerID','EmployerLegalName','ABN','EmployerTradingName','ANZSICCode','EmployerType','NumberOfEmployees','WorkplaceID','WorkplaceName','WORKPLACE_ADD1','WORKPLACE_ADD2','WORKPLACE_ADD3','WORKPLACE_SUBURB','WORKPLACE_POSTCODE','HoursPerWeek','ATSQualificationName','QualificationCode','QualificationName','CommencementDate','DurationDays','ProbationDate','ProbationPeriod','TypeOfApprenticeship','ANZSCOCode','ANZSCOName','NominalCompletionDate','SuspensionStartDate','SuspensionEndDate','ActualCompletiondate','TCStatus','TCSubStatus','RTOLegalName','RTOTOID']

for chunk in pd.read_csv('~/Desktop/VCDI_DPC_VRQA_20220808_clean.txt', chunksize=chunksize, usecols=cols2keep):
	chunk.to_csv('output.csv', mode='a', index=False)


# this page suggested dask, but didn't work for me
# https://stackoverflow.com/questions/38149288/delete-columns-from-very-large-csv-file-using-pandas-or-blaze
# import dask.dataframe as dd

# df = dd.read_csv('myfile.csv', usecols=['col1', 'col2', 'col3'])
# df.to_csv('output.csv', index=False)
