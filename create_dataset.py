from dotenv import load_dotenv
from langsmith import Client
import os

load_dotenv()

client = Client()

dataset_name = "Reviewly"

inputs = [
    "Does the description seems accurate?",
    "Does the location seems safe?",
    "Does the location seems nice?",
    "Are the reviews positive?",
    "Are any of the reviews negative?",
    "Are any of the reviews innacurate compared to the listing and what the other reviews say?",
    "What can be improved from the listing?",
    "Do any of the reivews mention things are not on the listing?",
    "is there any data missing from the listing?",
    "Is there any language that is not clear?",
]


outputs = [
    "The description is accurate",
    "The location is safe",
    "The location is nice",
    "Most reviews are positive",
    "None of reviews are negative",
    "Most reviews are consistent with the listing and other reviews",
    "There is one reviews that is not consistent with the listing and other reviews",
    "There is no data missing from the listing",
    "There is no language that is not clear",
]

#Store inputs and outputs in a dataset
dataset = client.create_dataset(
    dataset_name = dataset_name, 
    description = "First basic set of questions and answers about reviews.", 
)

client.create_examples(
    inputs=[{"question": q} for q in inputs],
    outputs=[{"answer": a} for a in outputs],
    dataset_id=dataset.id,
)

client.create_dataset(dataset_name, inputs=inputs)