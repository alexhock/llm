import asyncio
from collections.abc import Callable
import logging
import os
import random
from datetime import datetime
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff
import os
import asyncio
from openai import AsyncAzureOpenAI


class APICaller:

    def __init__(self, num_concurrent: int, api_func: Callable):
        self.api_func = api_func
        self.num_concurrent = num_concurrent
        self.call_timing = []

    def get_url(self):
        return random.choice(self.urls)

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    async def call_api(self, idx: int, messages: dict, semaphore: asyncio.Semaphore):
        try: 
            async with semaphore:  # Acquire a semaphore slot before making the API call, this throttles the concurrency
                start = datetime.now()
                result = await self.api_func(idx, messages)
                #if 'usage' in result:
                #    self.usage += result['usage']['total_tokens']
        except Exception as e:
            logging.error("API call failed for %s: %s", messages, e)
            raise e
            #return None
        finally:
            duration = (datetime.now() - start).total_seconds()
            self.call_timing.append(duration)
            if idx % 20 == 0:
                logging.info("Call %s completed in %s seconds", idx, duration)

        return result

    async def send(self, requests):
        semaphore = asyncio.Semaphore(self.num_concurrent)  
        tasks = []
        for idx, item in enumerate(requests):
            task = asyncio.create_task(self.call_api(idx, item, semaphore))
            tasks.append(task)
        return await asyncio.gather(*tasks, return_exceptions=True)


async def ask_llm(idx, messages, model="gpt-4-32k", max_tokens=256):

    response = None
    client = AsyncAzureOpenAI(  
        api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version = os.getenv("OPENAI_API_VERSION"),
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    response = await client.chat.completions.create(
        model=model, 
        messages=messages, 
        max_tokens=max_tokens
    )

    return (idx, response)


async def get_embeddings(idx, text, model="text-embedding-ada-002", max_tokens=4096):

    client = AsyncAzureOpenAI(  
        api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version = os.getenv("OPENAI_API_VERSION"),
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    response = await client.embeddings.create(
        model=model,
        input=text
    )

    return (idx, response)


def main():

    os.environ["AZURE_OPENAI_API_KEY"] = ""
    os.environ["OPENAI_API_VERSION"] = "2023-05-15"
    os.environ["AZURE_OPENAI_ENDPOINT"] = ""

    # parallel async LLM completion calls
    llm_caller = APICaller(5, ask_llm)
    messages = [
        {
            "role": "system",
            "content": "Hello, how can I help you today?"
        },
        {
            "role": "user",
            "content": "I need help with my computer."
        }
    ]

    responses = llm_caller.send(messages)

    # parallel async embeddings
    embedding_caller = APICaller(5, get_embeddings)
    text = "I need help with my computer."
    responses = embedding_caller.send(text)

    # TODO tests
    # examples
    # round robin
    # split client from function call
    # track timings, and output for analysis add wait times on throughput allowance

if __name__ == "__main__":
    asyncio.run(main())