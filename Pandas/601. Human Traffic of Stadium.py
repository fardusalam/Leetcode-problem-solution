import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:

    #fingding the rows with >= 100 people
    stadium = stadium[stadium['people']>=100]

    # creating new column for difference between id's
    stadium['diff'] = stadium['id'].diff()

    # Identifing new seqences
    stadium['new_sequence'] = (stadium['diff'] > 1) | stadium['diff'].isna()

    # new sequence value
    stadium['sequence_id'] = stadium['new_sequence'].cumsum()

    #finding consequtive id's length
    consequtive_length = stadium.groupby('sequence_id').size()


    #if no consequtive sequence have than return empty dataframe
    if consequtive_length.empty:
        return pd.DataFrame(columns = ['id', 'visit_date', 'people'])
    
    else:
        # identifing max length of sequence
        longest_consequtive_id = consequtive_length.idxmax()

        if consequtive_length[longest_consequtive_id] < 3:
            return pd.DataFrame(columns = ['id', 'visit_date', 'people'])
        
        else:
            #find all consequtive sequences
            valid_sequence = consequtive_length[consequtive_length>=3].index
            stadium = stadium[stadium['sequence_id'].isin(valid_sequence)]
            return stadium[['id', 'visit_date', 'people']]


