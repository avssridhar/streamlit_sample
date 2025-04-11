"""import pandas as pd
import random
from typing import Dict

# ------------------------------
# Step 1: Create Sample Data for Multiple Customers
# ------------------------------

age_bands = ['20-25', '26-30', '31-35']
employments = ['Salaried', 'Self Employed', 'Unemployed']
dpd_buckets = ['30+', '60+', '90+', '180+']
bureau_segments = ['High', 'Medium', 'Low']
wa_responses = ['High', 'Low', 'Clicked', 'Delivered']
sms_responses = ['High', 'Low']
ivr_responses = ['High', 'Low']
outbound_options = ['Yes', 'No']
intent_options = [True, False]

def generate_customer(i):
    return {
        'customer_id': f'CUST{i:03}',
        'Age_band': random.choice(age_bands),
        'Employment': random.choice(employments),
        'days_past_due': random.choice([30, 60, 90, 180]),
        'dpd_bucket': random.choice(dpd_buckets),
        'enr': random.randint(10000, 50000),
        'mobile_no': f'98{random.randint(10000000, 99999999)}',
        'bureau_segment': random.choice(bureau_segments),
        'wa_response': random.choice(wa_responses),
        'sms_response': random.choice(sms_responses),
        'ivr_response': random.choice(ivr_responses),
        'outbound_calling': random.choice(outbound_options),
        'intent_to_pay': random.choice(intent_options)
    }

customers_df = pd.DataFrame([generate_customer(i) for i in range(1, 16)])

# ------------------------------
# Step 2: Define Treatment Repository
# ------------------------------

treatment_repository = [
    {
        'state': {
            'dpd_bucket': '180+',
            'bureau_segment': 'Low',
            'wa_response': 'High',
            'intent_to_pay': True
        },
        'treatment': {
            'channel': 'WhatsApp',
            'tone': 'Empathetic',
            'time_to_trigger': '10 AM',
            'offer': '50% waiver if paid today',
            'message': 'We understand things get tough. Clear your dues today and get a 50% waiver. Let’s get back on track!'
        }
    },
    {
        'state': {
            'dpd_bucket': '90+',
            'bureau_segment': 'Medium',
            'wa_response': 'Low',
            'intent_to_pay': False
        },
        'treatment': {
            'channel': 'SMS',
            'tone': 'Urgent',
            'time_to_trigger': '2 PM',
            'offer': '25% waiver',
            'message': 'Act now to avoid further penalties. Pay today and get a 25% waiver.'
        }
    },
    {
        'state': {
            'dpd_bucket': '60+',
            'bureau_segment': 'High',
            'wa_response': 'Clicked',
            'intent_to_pay': True
        },
        'treatment': {
            'channel': 'Email',
            'tone': 'Informative',
            'time_to_trigger': '4 PM',
            'offer': '10% discount if paid in 3 days',
            'message': 'Good to see your interest. Pay in the next 3 days to save 10% on your dues.'
        }
    },
    {
        'state': {
            'dpd_bucket': '30+',
            'bureau_segment': 'High',
            'wa_response': 'Delivered',
            'intent_to_pay': False
        },
        'treatment': {
            'channel': 'IVR',
            'tone': 'Friendly',
            'time_to_trigger': '6 PM',
            'offer': 'Reminder only',
            'message': 'You missed your due date. Please pay soon to stay in good standing.'
        }
    },
    {
        'state': {
            'dpd_bucket': '180+',
            'bureau_segment': 'Medium',
            'wa_response': 'Clicked',
            'intent_to_pay': False
        },
        'treatment': {
            'channel': 'Outbound Call',
            'tone': 'Assertive',
            'time_to_trigger': '11 AM',
            'offer': '30% waiver + extended due date',
            'message': 'We’re calling to assist you with a 30% waiver and more time to pay. Let’s resolve this together.'
        }
    }
]

# ------------------------------
# Step 3: Matching Logic
# ------------------------------

def determine_state(row: Dict) -> Dict:
    return {
        'dpd_bucket': row['dpd_bucket'],
        'bureau_segment': row['bureau_segment'],
        'wa_response': row['wa_response'],
        'intent_to_pay': row['intent_to_pay']
    }

def get_treatment(state: Dict, treatment_repository) -> Dict:
    for entry in treatment_repository:
        if all(state.get(k) == v for k, v in entry['state'].items()):
            return entry['treatment']
    return {
        'channel': 'SMS',
        'tone': 'Neutral',
        'time_to_trigger': '2 PM',
        'offer': '10% waiver',
        'message': 'Pay now and save 10%!'
    }

# ------------------------------
# Step 4: Feedback Loop Logic
# ------------------------------

def feedback_loop(customer_id: str, updated_fields: Dict) -> Dict:
    global customers_df
    # Update the customer row in the DataFrame with new feedback fields
    customers_df.loc[customers_df['customer_id'] == customer_id, list(updated_fields.keys())] = list(updated_fields.values())
    
    # Get the updated row after changes
    updated_row = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()
    
    # Get the new state after feedback
    new_state = determine_state(updated_row)
    
    # Determine treatment based on the updated state
    return get_treatment(new_state, treatment_repository)

# Example feedback loop test
updated_fields = {'dpd_bucket': '60+', 'intent_to_pay': False}
customer_id = 'CUST001'
new_treatment = feedback_loop(customer_id, updated_fields)

print(f"Updated treatment for customer {customer_id}:\n{new_treatment}")
"""

import pandas as pd
import random
from typing import Dict

# ------------------------------
# Step 1: Create Sample Data for Multiple Customers
# ------------------------------

age_bands = ['20-25', '26-30', '31-35']
employments = ['Salaried', 'Self Employed', 'Unemployed']
dpd_buckets = ['30+', '60+', '90+', '180+']
bureau_segments = ['High', 'Medium', 'Low']
wa_responses = ['High', 'Low', 'Clicked', 'Delivered']
sms_responses = ['High', 'Low']
ivr_responses = ['High', 'Low']
outbound_options = ['Yes', 'No']
intent_options = [True, False]

def generate_customer(i):
    return {
        'customer_id': f'CUST{i:03}',
        'Age_band': random.choice(age_bands),
        'Employment': random.choice(employments),
        'days_past_due': random.choice([30, 60, 90, 180]),
        'dpd_bucket': random.choice(dpd_buckets),
        'enr': random.randint(10000, 50000),
        'mobile_no': f'98{random.randint(10000000, 99999999)}',
        'bureau_segment': random.choice(bureau_segments),
        'wa_response': random.choice(wa_responses),
        'sms_response': random.choice(sms_responses),
        'ivr_response': random.choice(ivr_responses),
        'outbound_calling': random.choice(outbound_options),
        'intent_to_pay': random.choice(intent_options)
    }

customers_df = pd.DataFrame([generate_customer(i) for i in range(1, 16)])

# ------------------------------
# Step 2: Define Treatment Repository
# ------------------------------

treatment_repository = [
    {
        'state': {
            'dpd_bucket': '180+',
            'bureau_segment': 'Low',
            'wa_response': 'High',
            'intent_to_pay': True
        },
        'treatment': {
            'channel': 'WhatsApp',
            'tone': 'Empathetic',
            'time_to_trigger': '10 AM',
            'offer': '50% waiver if paid today',
            'message': 'We understand things get tough. Clear your dues today and get a 50% waiver. Let’s get back on track!'
        }
    },
    {
        'state': {
            'dpd_bucket': '90+',
            'bureau_segment': 'Medium',
            'wa_response': 'Low',
            'intent_to_pay': False
        },
        'treatment': {
            'channel': 'SMS',
            'tone': 'Urgent',
            'time_to_trigger': '2 PM',
            'offer': '25% waiver',
            'message': 'Act now to avoid further penalties. Pay today and get a 25% waiver.'
        }
    },
    {
        'state': {
            'dpd_bucket': '60+',
            'bureau_segment': 'High',
            'wa_response': 'Clicked',
            'intent_to_pay': True
        },
        'treatment': {
            'channel': 'Email',
            'tone': 'Informative',
            'time_to_trigger': '4 PM',
            'offer': '10% discount if paid in 3 days',
            'message': 'Good to see your interest. Pay in the next 3 days to save 10% on your dues.'
        }
    },
    {
        'state': {
            'dpd_bucket': '30+',
            'bureau_segment': 'High',
            'wa_response': 'Delivered',
            'intent_to_pay': False
        },
        'treatment': {
            'channel': 'IVR',
            'tone': 'Friendly',
            'time_to_trigger': '6 PM',
            'offer': 'Reminder only',
            'message': 'You missed your due date. Please pay soon to stay in good standing.'
        }
    },
    {
        'state': {
            'dpd_bucket': '180+',
            'bureau_segment': 'Medium',
            'wa_response': 'Clicked',
            'intent_to_pay': False
        },
        'treatment': {
            'channel': 'Outbound Call',
            'tone': 'Assertive',
            'time_to_trigger': '11 AM',
            'offer': '30% waiver + extended due date',
            'message': 'We’re calling to assist you with a 30% waiver and more time to pay. Let’s resolve this together.'
        }
    }
]

# ------------------------------
# Step 3: Matching Logic
# ------------------------------

def determine_state(row: Dict) -> Dict:
    return {
        'dpd_bucket': row['dpd_bucket'],
        'bureau_segment': row['bureau_segment'],
        'wa_response': row['wa_response'],
        'intent_to_pay': row['intent_to_pay']
    }

def get_treatment(state: Dict, treatment_repository) -> Dict:
    for entry in treatment_repository:
        if all(state.get(k) == v for k, v in entry['state'].items()):
            return entry['treatment']
    return {
        'channel': 'SMS',
        'tone': 'Neutral',
        'time_to_trigger': '2 PM',
        'offer': '10% waiver',
        'message': 'Pay now and save 10%!'
    }

# ------------------------------
# Step 4: Feedback Loop Logic
# ------------------------------

def feedback_loop(customer_id: str, feedback: str) -> Dict:
    global customers_df
    # Get the customer row
    customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0]
    
    # Update the customer row based on feedback (just an example update, adjust as needed)
    if feedback == "WhatsApp Clicked":
        customers_df.loc[customers_df['customer_id'] == customer_id, 'wa_response'] = 'Clicked'
    elif feedback == "No Response":
        customers_df.loc[customers_df['customer_id'] == customer_id, 'wa_response'] = 'No Response'
    elif feedback == "IVR Success":
        customers_df.loc[customers_df['customer_id'] == customer_id, 'ivr_response'] = 'High'
    elif feedback == "SMS Ignored":
        customers_df.loc[customers_df['customer_id'] == customer_id, 'sms_response'] = 'Low'
    elif feedback == "Payment Made":
        customers_df.loc[customers_df['customer_id'] == customer_id, 'intent_to_pay'] = True
    
    # Get the updated row after changes
    updated_row = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()
    
    # Get the new state after feedback
    new_state = determine_state(updated_row)
    
    # Determine treatment based on the updated state
    return get_treatment(new_state, treatment_repository)

