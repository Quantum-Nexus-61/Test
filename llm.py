import os
import pickle
import time

import torch
from langchain.llms.base import LLM
from llama_index import (
    GPTListIndex,
    LLMPredictor,
    ServiceContext,
    SimpleDirectoryReader,
)
from transformers import pipeline


def timeit(func):
    """
    A utility decorator to time running time.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        args_str = ", ".join(map(str, args))
        print(f"[{(end - start):.8f} seconds]: {func.__name__}({args_str}) -> {result}")
        return result

    return wrapper


class LocalOPT(LLM):
    model_name = "facebook/opt-iml-1.3b"
    pipeline = pipeline(
        "text-generation",
        model=model_name,
        device="cpu",  # Change the device to CPU
        model_kwargs={"torch_dtype": torch.float32},  # Use float32 (CPU-friendly)
    )

    def _call(self, prompt: str, stop=None) -> str:
        response = self.pipeline(prompt, max_new_tokens=256)[0]["generated_text"]
        return response[len(prompt) :]

    @property
    def _identifying_params(self):
        return {"name_of_model": self.model_name}

    @property
    def _llm_type(self):
        return "custom"


# Define index as a global variable
index = None


@timeit
def create_index():
    print("Creating index")
    llm = LLMPredictor(llm=LocalOPT())
    service_context = ServiceContext.from_defaults(llm_predictor=llm)
    docs = SimpleDirectoryReader("news").load_data()
    try:
        index = GPTListIndex.from_documents(docs, service_context=service_context)
        print("Done creating index")
    except Exception as e:
        print("An error occurred while creating the index:", e)
    return index


@timeit
def execute_query(index, input_text):
    response = index.query(
        input_text,
        exclude_keywords=["petroleum"],
    )
    return response


# Summarization Function
def summarize_text(text, max_length=150):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)[
        0
    ]["summary_text"]
    return summary


if __name__ == "__main__":
    user_choice = "text"

    if user_choice == "text":
        input_text = "Python is a versatile and popular programming language. It is often used in web development, data analysis, and machine learning projects."
    elif user_choice == "file":
        file_path = input("Enter the path to the file to summarize: ")

        if not os.path.exists(file_path):
            print("File not found. Please try again.")
            exit()

        with open(file_path, "r") as file:
            input_text = file.read()
    else:
        print("Invalid input type. Please choose 'text' or 'file'.")

    if not os.path.exists("7_custom_opt.pkl"):
        print("No local cache of the model found, downloading from Hugging Face")
        index = create_index()

        # Saving the index using pickle
        with open("7_custom_opt.pkl", "wb") as file:
            pickle.dump(index, file)
    else:
        print("Loading the local cache of the model")

        # Loading the index from the saved pickle file
        with open("7_custom_opt.pkl", "rb") as file:
            index = pickle.load(file)

    response = execute_query(index, input_text)
    print(response)

    summarized_response = summarize_text(response)
    print("Summary:")
    print(summarized_response)