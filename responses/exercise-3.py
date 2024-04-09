#David Lichtman

# write your code here

#read in table_history dataset

import pandas as pd

def main():
    table_history=pd.read_csv("table-history.csv")

    status_changes=pd.read_csv("status-changes.csv")

    print(table_history.head())

    #strategy: create multiple tables for customer_type, last_billed_date, etc. by pulling apart changes column
    #though need to keep table_history_id and customer_id and postdate tied to new tables when expanded
    changes=table_history['changes'].str.split('@#@#@#', expand=True)
    print(changes.head())
    #add new changes column to original table history

    mod_table_history=table_history.join(changes)

    print(mod_table_history)

    #stacks attribute strings into 1 column
    concatenated_dfs = []
    for col in changes.columns:
        join_col=table_history.iloc[:,0:3].join(changes[col])
        if len(join_col.columns)>0:
            print(join_col)
            concatenated_dfs.append(join_col)
    
    result_df = pd.concat(concatenated_dfs, axis=0)
    #print(result_df)

    result_df=result_df.iloc[:,0:4].reset_index()
    print(result_df)


    #now break apart the attribute strings

    changes_split=result_df[0].str.split('-\^!\^!\^-', expand=True)
    print(changes_split)

    id_tags=result_df.iloc[:,0:4]
    print(id_tags)

    full_attributes=id_tags.join(changes_split)
    full_attributes.rename(columns={0:"attribute",1:"old_value",2:"new_value"}, inplace=True)
    filtered_1=full_attributes[full_attributes['attribute'].notnull()]
    filtered_2=filtered_1[filtered_1['customer_id']==1634015]
    print(filtered_2)

    relevant_attributes=full_attributes[full_attributes['attribute'].isin(['current_status','customer_type','membershp_form_of_payment'])] #,'membership_form_of_payment','customer_type'])]
    
    print(status_changes)

    membership_starts=full_attributes.query("old_value=='GUEST' & new_value=='MEMBER'")
    print(membership_starts)

    
    #join (pandas merge) tables together 

    joined_status_and_history_attributes=status_changes.merge(full_attributes,
                                                              how='left',
                                                              left_on=['customer_id','postdate'],
                                                              right_on=['customer_id','postdate']
                                                              )
    
    #print(joined_status_and_history_attributes[joined_status_and_history_attributes.customer_id==1670321])

    print(joined_status_and_history_attributes)

    #how to determine which status changes match with which statuses when I'm just joining on customer id?
    #maybe need to do more preprocessing on full_attributes table

    #membership start clues: customer_type Guest to Member

    #membership end clues: customer_type Member to Guest or Punch Card,
    #                   current_status OK to Frozen/Terminated,
    #                   membership_form_of_payment = Prepaid




if __name__ == "__main__":
    main()