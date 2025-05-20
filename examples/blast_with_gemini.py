"""BLAST with Gemini."""

import os
import time
import asyncio
from pathlib import Path
import shutil
from openai import OpenAI
from browser_use import Agent, Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.callbacks import get_openai_callback
from blastai.utils import estimate_llm_cost

# Task to perform
TASK = "제주도의 유명한 관광지 5곳을 소개해주세요."

async def run_with_browser_use_gemini() -> tuple[float, str, float]:
    """Run task with browser-use directly using Gemini."""
    # Create browser with settings matching BLAST's default_config.yaml
    config = BrowserConfig(
        headless=True  # From require_headless=false
    )
    browser = Browser(config=config)
    
    # Create agent with Gemini model
    agent = Agent(
        task=TASK,
        llm=ChatGoogleGenerativeAI(model="gemini-pro"),  # Using Gemini Pro
        use_vision=False,  # From allow_vision=false
        browser=browser  # Pass browser instance directly
    )
    
    start_time = time.time()
    try:
        # Run the agent
        history = await agent.run()
        
        end_time = time.time()
        await browser.close()
        return end_time - start_time, history.final_result(), 0.0  # Cost tracking not available for Gemini yet
    except Exception as e:
        await browser.close()
        raise e

def run_with_blast_gemini() -> tuple[float, str]:
    """Run task with BLAST using Gemini."""
    # To use Gemini with BLAST, we need to modify the constraints in the configuration
    # This requires modifying the blastai/config.py or using the Constraints class directly
    
    # For demonstration purposes, showing how to call BLAST service
    client = OpenAI(
        api_key="not-needed",
        base_url="http://127.0.0.1:8000"
    )
    
    start_time = time.time()
    response = client.responses.create(
        model="gemini-pro",  # This would require changing BLAST to support Gemini models
        input=TASK,
        stream=False
    )
    end_time = time.time()
    
    # Extract final result from response
    result = response.choices[0].message.content
    return end_time - start_time, result

async def main():
    """Run the Gemini example."""
    print("Starting Gemini task...")
    print(f"Task: {TASK}\n")
    
    # Run with browser-use and Gemini
    print("Running with browser-use and Gemini...")
    browser_use_time, browser_use_result, _ = await run_with_browser_use_gemini()
    print(f"browser-use Time: {browser_use_time:.2f}s")
    print("browser-use Result:")
    print(browser_use_result)
    
    # Note: Running with BLAST would require modifying BLAST's code to support Gemini
    # This example only demonstrates the browser-use part
    
if __name__ == "__main__":
    asyncio.run(main())
